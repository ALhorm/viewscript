from dataclasses import dataclass
from typing import NewType, Self
import string


TokenType = NewType('TokenType', str)

TNumber = TokenType('Number')
TString = TokenType('String')
TKeyword = TokenType('Keyword')
TIdentifier = TokenType('Identifier')
TPlus = TokenType('Plus')
TMinus = TokenType('Minus')
TStar = TokenType('Star')
TSlash = TokenType('Slash')
TAssign = TokenType('Assign')
TExPoint = TokenType('ExPoint')
TComma = TokenType('Comma')
TOr = TokenType('Or')
TAnd = TokenType('And')
TEqual = TokenType('Equal')
TNotEqual = TokenType('NotEqual')
TGreater = TokenType('Greater')
TGreaterEqual = TokenType('GreaterEqual')
TLess = TokenType('Less')
TLessEqual = TokenType('LessEqual')
TModGet = TokenType('ModGet')
TRef = TokenType('Ref')
T_OR_BKT = TokenType('ORB')
T_CR_BKT = TokenType('CRB')
T_OC_BKT = TokenType('OCB')
T_CC_BKT = TokenType('CCB')
T_EOF = TokenType('EOF')

KEYWORDS = [
    'let', 'true', 'false', 'if', 'elif', 'else', 'fn', 'ret', 'mod', 'loadlib', 'pub'
]

OPERATORS = {
    '+': TPlus,
    '-': TMinus,
    '*': TStar,
    '/': TSlash,
    '=': TAssign,
    '!': TExPoint,
    ',': TComma,
    '||': TOr,
    '&&': TAnd,
    '==': TEqual,
    '!=': TNotEqual,
    '>': TGreater,
    '>=': TGreaterEqual,
    '<': TLess,
    '<=': TLessEqual,
    '::': TModGet,
    '&': TRef,
    '(': T_OR_BKT,
    ')': T_CR_BKT,
    '{': T_OC_BKT,
    '}': T_CC_BKT
}

LETTERS = string.ascii_letters + '_$'
LETTERS_DIGITS = LETTERS + string.digits
CHARS = '+-*/=!,|&:(){}<>'


@dataclass
class Position:
    id: int
    ln: int
    col: int

    def next(self, current_char: str):
        self.id += 1
        self.col += 1

        if current_char == '\n':
            self.ln += 1
            self.col = 1

    def copy(self) -> Self:
        return Position(self.id, self.ln, self.col)


@dataclass
class Token:
    type: TokenType
    value: str | int | float
    pos: Position
