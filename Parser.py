from .Token import Token
from .TokenType import TokenType
from viewscript.ast import *


class Parser:
    def __init__(self, tokens: list[Token]):
        self.tokens = tokens
        self.pos = 0

    def parse(self) -> None:
        while not self.match(TokenType.EOF):
            try:
                self.statement().exec()
            except Exception as e:
                pos = self.pos
                if pos >= len(self.tokens):
                    pos -= 1

                raise Exception(e.args[0], self.tokens[pos])

    def statement(self) -> Statement:
        if self.look_match(1, TokenType.ASSIGN):
            return self.assignment()
        if self.match(TokenType.LET):
            return self.let()
        if self.match(TokenType.PRINT):
            return PrintStatement(self.expression())
        if self.match(TokenType.FUNC):
            return self.function()

        raise Exception('Syntax error.')

    def let(self) -> Statement:
        name = self.consume(TokenType.WORD).value
        self.consume(TokenType.ASSIGN)

        return LetStatement(name, self.expression())

    def assignment(self) -> Statement:
        name = self.consume(TokenType.WORD).value
        self.consume(TokenType.ASSIGN)

        return AssignmentStatement(name, self.expression())

    def function(self) -> Statement:
        name = self.consume(TokenType.WORD).value
        self.consume(TokenType.ORB)

        params = {}
        while not self.match(TokenType.CRB):
            arg_name = self.consume(TokenType.WORD).value
            arg_value = None

            if self.match(TokenType.ASSIGN):
                arg_value = self.expression()
            self.match(TokenType.COMMA)

            params[arg_name] = arg_value

        return FunctionStatement(name, params, self.statement())

    def expression(self) -> Expression:
        return self.additive()

    def additive(self) -> Expression:
        result = self.multiplicative()

        while True:
            if self.match(TokenType.PLUS):
                result = BinaryExpression(result, self.multiplicative(), '+')
                continue
            if self.match(TokenType.MINUS):
                result = BinaryExpression(result, self.multiplicative(), '-')
                continue
            break

        return result

    def multiplicative(self) -> Expression:
        result = self.unary()

        while True:
            if self.match(TokenType.STAR):
                result = BinaryExpression(result, self.unary(), '*')
                continue
            if self.match(TokenType.SLASH):
                result = BinaryExpression(result, self.unary(), '/')
                continue
            break

        return result

    def unary(self) -> Expression:
        result = self.primary()

        if self.match(TokenType.PLUS):
            return result
        if self.match(TokenType.MINUS):
            return UnaryExpression(result)

        return result

    def primary(self) -> Expression:
        current = self.get(0)

        if self.match(TokenType.NUMBER):
            if '.' in current.value:
                return ValueExpression(float(current.value))
            return ValueExpression(int(current.value))
        if self.match(TokenType.WORD):
            return VariableExpression(current.value)
        if self.match(TokenType.TEXT):
            return ValueExpression(current.value)

        raise Exception('Expected expression.')

    def look_match(self, rel_pos: int, token_type: TokenType) -> bool:
        return self.get(rel_pos).type == token_type

    def match(self, token_type: TokenType) -> bool:
        current = self.get(0)
        if current.type != token_type:
            return False
        self.pos += 1
        return True

    def consume(self, token_type: TokenType) -> Token:
        current = self.get(0)
        if current.type != token_type:
            raise Exception('Syntax error.')
        self.pos += 1
        return current

    def get(self, rel_pos: int) -> Token:
        position = self.pos + rel_pos
        if position >= len(self.tokens):
            return Token(TokenType.EOF, '\0', 0, 0)
        return self.tokens[position]
