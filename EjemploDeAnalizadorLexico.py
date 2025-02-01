import re

TOKEN_TYPES = [
    ('NUMBER', r'\d+(\.\d*)?'),  # Números enteros y reales
    ('STRING', r'"[^"]*"'),  # Cadenas de caracteres
    ('IDENTIFIER', r'[a-zA-Z_]\w*'),  # Identificadores (nombres de variables)
    ('ASSIGN', r'='),  # Asignación
    ('PLUS', r'\+'),  # Operación aritmética +
    ('MINUS', r'-'),  # Operación aritmética -
    ('TIMES', r'\*'),  # Operación aritmética *
    ('DIVIDE', r'/'),  # Operación aritmética /
    ('EQ', r'=='),  # Operación lógica ==
    ('NEQ', r'!='),  # Operación lógica !=
    ('LT', r'<'),  # Operación lógica <
    ('GT', r'>'),  # Operación lógica >
    ('IF', r'if'),  # Palabra clave if
    ('THEN', r'then'),  # Palabra clave then
    ('ELSE', r'else'),  # Palabra clave else
    ('WHITESPACE', r'\s+'),  # Espacios en blanco
]

# Función para generar tokens
def tokenize(code):
    tokens = []
    while code:
        match = None
        for token_type, pattern in TOKEN_TYPES:
            regex = re.compile(pattern)
            match = regex.match(code)
            if match:
                text = match.group(0)
                if token_type != 'WHITESPACE':  # Ignorar espacios en blanco
                    tokens.append((token_type, text))
                code = code[len(text):]
                break
        if not match:
            raise SyntaxError(f'Unexpected character: {code[0]}')
    return tokens

# Ejemplo de uso
code = 'if x == 10 then y = "hello" else y = 20 = for i = 1 to 10 do sum = sum + i'
tokens = tokenize(code)
for token in tokens:
    print(token)