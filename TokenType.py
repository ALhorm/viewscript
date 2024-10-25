from enum import Enum

class TokenType(Enum):
    NUMBER = 'number'
    WORD = 'word'
    TEXT = 'text'

    LET = 'let'
    PRINT = 'print'
    FUNC = 'func'

    PLUS = '+'
    MINUS = '-'
    STAR = '*'
    SLASH = '/'
    ASSIGN = '='
    ORB = '('
    CRB = ')'
    COMMA = ','

    EOF = '\0'
