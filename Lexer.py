from .Token import Token
from .TokenType import TokenType

class Lexer:
    def __init__(self, code: str):
        self.code = code
        self.length = len(code)
        self.pos = 0
        self.line = 1
        self.col = 1
        self.tokens = []
        self.operators = {
            '+': TokenType.PLUS,
            '-': TokenType.MINUS,
            '*': TokenType.STAR,
            '/': TokenType.SLASH,
            '=': TokenType.ASSIGN,
            ',': TokenType.COMMA,
            '(': TokenType.ORB,
            ')': TokenType.CRB
        }
        self.chars = '+-*/=,()'

    def lex(self) -> list[Token]:
        while self.pos < self.length:
            current = self.peek(0)

            if current.isdigit():
                self.lex_number()
            elif current in self.chars:
                self.lex_operator()
            elif current.isalpha() or current == '_':
                self.lex_word()
            elif current == '"':
                self._next()
                self.lex_text()
            else:
                self._next()
                if current == '\n':
                    self.line += 1
                    self.col = 1

        return self.tokens

    def lex_number(self):
        current = self.peek(0)
        result = ''

        while current.isdigit() or current == '.':
            if '.' in result and current == '.':
                raise Exception('Incorrect float number.', self.line, self.col, result)

            result += current
            current = self._next()

        self.add_token(TokenType.NUMBER, result)

    def lex_operator(self):
        current = self.peek(0)
        result = ''

        while True:
            if result + current not in self.operators and result:
                self.add_token(self.operators[result], result)
                return

            result += current
            current = self._next()

    def lex_word(self) -> None:
        result = ''
        current = self.peek(0)

        while True:
            if not (current.isalpha() or current.isdigit()) and current != '_':
                break

            result += current
            current = self._next()

        match result:
            case 'let':
                self.add_token(TokenType.LET, result)
            case 'print':
                self.add_token(TokenType.PRINT, result)
            case 'func':
                self.add_token(TokenType.FUNC, result)
            case _:
                self.add_token(TokenType.WORD, result)

    def lex_text(self) -> None:
        result = ''
        current = self.peek(0)

        while True:
            if current == '\\':
                current = self._next()
                match current:
                    case '"':
                        current = self._next()
                        result += '"'
                        continue
                    case 'n':
                        current = self._next()
                        result += 'n'
                        continue
                    case 't':
                        current = self._next()
                        result += 't'
                        continue

                result += '\\'
                continue
            if current == '"':
                break

            result += current
            current = self._next()
        self._next()

        self.add_token(TokenType.TEXT, result)

    def add_token(self, _type: TokenType, value: str):
        self.tokens.append(Token(_type, value, self.line, self.col))

    def peek(self, rel_pos: int) -> str:
        pos = self.pos + rel_pos
        if pos >= self.length:
            return '\0'
        return self.code[pos]

    def _next(self) -> str:
        self.pos += 1
        self.col += 1
        return self.peek(0)
