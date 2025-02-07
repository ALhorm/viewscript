from core.tokens import (Token, Position, TNumber, T_EOF, TString, LETTERS_DIGITS, KEYWORDS, TKeyword, TIdentifier,
                         LETTERS, OPERATORS, CHARS, TokenType)
from core.errors import InvalidNumberError


class Lexer:
    def __init__(self, file: str):
        with open(file, 'r') as f:
            self.code = f.read()
        self.lines = self.code.split('\n')
        self.pos = Position(0, 1, 1)
        self.current_char = self.code[0]

    def lex(self) -> list[Token]:
        tokens = []

        while self.pos.id < len(self.code):
            if self.current_char.isdigit():
                tokens.append(self.number())
            if self.current_char == '"' or self.current_char == '\'':
                tokens.append(self.string(self.current_char))
            if self.current_char in LETTERS:
                tokens.append(self.identifier())
            if self.current_char in CHARS:
                tokens.append(self.operator())
            else:
                self.next()

        tokens.append(Token(T_EOF, 'EOF', self.pos))

        return tokens

    def next(self):
        self.pos.next(self.current_char)

        if self.pos.id >= len(self.code):
            return

        self.current_char = self.code[self.pos.id]

    def number(self) -> Token:
        number = ''
        position = self.pos.copy()

        while self.current_char.isdigit() or self.current_char == '.':
            if self.current_char == '.' and '.' in number:
                InvalidNumberError(Token(TNumber, number, self.pos.copy())).call()

            number += self.current_char
            self.next()

        return Token(TNumber, float(number) if '.' in number else int(number), position)

    def string(self, quote: str) -> Token:
        string = ''
        position = self.pos.copy()
        self.next()

        while self.current_char != quote:
            string += self.current_char
            self.next()

        self.next()

        return Token(TString, string, position)

    def identifier(self) -> Token:
        iden = ''
        position = self.pos.copy()

        while self.current_char in LETTERS_DIGITS:
            iden += self.current_char
            self.next()

        return Token(TKeyword if iden in KEYWORDS else TIdentifier, iden, position)

    def operator(self) -> Token:
        operator = ''
        position = self.pos.copy()

        while True:
            if operator + self.current_char not in OPERATORS and operator:
                return Token(OPERATORS[operator], operator, position)

            operator += self.current_char
            self.next()
