from .TokenType import TokenType

class Token:
    def __init__(self, _type: TokenType, value: str, line: int, col: int):
        self.type = _type
        self.value = value
        self.line = line
        self.col = col - len(value)

        if _type is TokenType.TEXT:
            self.col -= 2

    def __str__(self):
        return f'Token({self.type}: {self.value}, line: {self.line}, col: {self.col})'
