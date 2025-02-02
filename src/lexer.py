import re
import sys
import os

# Asegúrate de que el directorio src esté en el sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from token_types import TokenTypes
from file_handler import read_file, write_file

# Especificaciones de tokens (expresiones regulares)
TOKEN_SPECS = [
    (TokenTypes.PALABRA_CLAVE, r"\b(if|else|then|for|case|break|while|return)\b"),  # Palabras clave
    (TokenTypes.IDENTIFICADOR, r"[a-zA-Z_][a-zA-Z0-9_]*"),  # Identificadores
    (TokenTypes.NUMERO_ENTERO, r"\b\d+\b"),  # Números enteros
    (TokenTypes.NUMERO_REAL, r"\b\d+\.\d+\b"),  # Números reales
    (TokenTypes.CADENA, r"\".*?\""),  # Cadenas de texto
    (TokenTypes.OPERADOR_ARITMETICO, r"[+\-*/]"),  # Operadores aritméticos
    (TokenTypes.OPERADOR_LOGICO_ESTRICTO, r"==|!="),  # Operadores lógicos (estrictos)
    (TokenTypes.OPERADOR_LOGICO_COMPARACION, r"<|>|<=|>="),  # Operadores lógicos (comparación)
    (TokenTypes.DELIMITADOR, r"[;(){}]"),  # Delimitadores
    (TokenTypes.ASIGNACION, r"="),  # Asignación
    (TokenTypes.ESPACIO, r"\s+"),  # Espacios y saltos de línea (ignorar)
    (TokenTypes.COMENTARIO, r"//.*?$|/\*.*?\*/"),  # Comentarios
]

# Función principal del lexer
def lex(code):
    tokens = []
    position = 0
    line = 1
    column = 1

    while position < len(code):
        match = None

        # Buscar coincidencias con los patrones de tokens
        for token_type, pattern in TOKEN_SPECS:
            regex = re.compile(pattern)
            match = regex.match(code, position)
            if match:
                value = match.group(0)
                if token_type != TokenTypes.ESPACIO and token_type != TokenTypes.COMENTARIO:
                    tokens.append({
                        "type": token_type,
                        "value": value,
                        "line": line,
                        "column": column
                    })
                position = match.end()

                # Actualizar la línea y la columna
                line += value.count('\n')
                column = len(value) - value.rfind('\n') - 1 if '\n' in value else column + len(value)
                break

        # Si no se encuentra un token válido, lanzar un error
        if not match:
            raise ValueError(f"Error léxico: carácter inesperado en posición {position} ('{code[position]}')")

    return tokens

# Punto de entrada del programa
if __name__ == "__main__":
    # Rutas de archivos
    input_file_path = "../input/example.txt"
    output_file_path = "../output/tokens.json"

    try:
        # Leer el archivo de entrada
        code = read_file(input_file_path)

        # Ejecutar el lexer
        tokens = lex(code)

        # Guardar los tokens en un archivo de salida
        write_file(output_file_path, tokens)

        print("✅ Análisis léxico completado. Tokens guardados en:", output_file_path)
    except Exception as e:
        print("❌ Error:", e)
