import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from src.lexer import lex

class TestLexer(unittest.TestCase):
    def test_lexer(self):
        code = "x = 10;"
        tokens = lex(code)
        expected_tokens = [
            {"type": "IDENTIFICADOR", "value": "x"},
            {"type": "ASIGNACION", "value": "="},
            {"type": "NUMERO_ENTERO", "value": "10"},
            {"type": "DELIMITADOR", "value": ";"},
        ]
        self.assertEqual(tokens, expected_tokens)

if __name__ == "__main__":
    unittest.main()