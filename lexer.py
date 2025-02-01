import re
from collections import defaultdict

TOKEN_TYPES = [
    ('IF', r'\bif\b'),
    ('THEN', r'\bthen\b'),
    ('ELSE', r'\belse\b'),
    ('FOR', r'\bfor\b'),
    ('TO', r'\bto\b'),
    ('DO', r'\bdo\b'),
    ('NUMBER', r'\d+(\.\d*)?'),
    ('STRING', r'"[^"]*"'),
    ('IDENTIFIER', r'[a-zA-Z_]\w*'),
    ('ASSIGN', r'='),
    ('PLUS', r'\+'),
    ('MINUS', r'-'),
    ('TIMES', r'\*'),
    ('DIVIDE', r'/'),
    ('EQ', r'=='),
    ('NEQ', r'!='),
    ('LT', r'<'),
    ('GT', r'>'),
    ('WHITESPACE', r'\s+'),
]

def tokenize_with_count(code):
    tokens = []
    token_count = defaultdict(int)

    while code:
        match = None
        for token_type, pattern in TOKEN_TYPES:
            regex = re.compile(pattern)
            match = regex.match(code)
            if match:
                text = match.group(0)
                if token_type != 'WHITESPACE':  
                    tokens.append((token_type, text))
                    token_count[token_type] += 1  
                code = code[len(text):]
                break
        if not match:
            raise SyntaxError(f'Unexpected character: {code[0]!r} near "{code[:10]}"')

    return tokens, dict(token_count)