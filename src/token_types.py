

class TokenTypes:
    PALABRA_CLAVE = "PALABRA_CLAVE"  # if, else, then, etc.
    IDENTIFICADOR = "IDENTIFICADOR"  # Nombres de variables
    NUMERO_ENTERO = "NUMERO_ENTERO"  # Números enteros
    NUMERO_REAL = "NUMERO_REAL"      # Números reales
    CADENA = "CADENA"                # Cadenas de texto
    OPERADOR_ARITMETICO = "OPERADOR_ARITMETICO"  # +, -, *, /
    OPERADOR_LOGICO = "OPERADOR_LOGICO"          # ==, !=, <, >, <=, >=
    DELIMITADOR = "DELIMITADOR"      # ;, (, ), {, }
    ASIGNACION = "ASIGNACION"        # =
    ESPACIO = "ESPACIO"              # Espacios y saltos de línea (ignorar)
    COMENTARIO = "COMENTARIO"        # Comentarios
    DESCONOCIDO = "DESCONOCIDO"      # Tokens no reconocidos
    OPERADOR_LOGICO_ESTRICTO = "OPERADOR_LOGICO_ESTRICTO"  # ==, !=
    OPERADOR_LOGICO_COMPARACION = "OPERADOR_LOGICO_COMPARACION"  # <, >, <=, >=
