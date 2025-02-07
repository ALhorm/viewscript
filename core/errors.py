from core.tokens import Token
from sys import exit


class Error:
    def __init__(self, token: Token):
        self.token = token
        self.type = self.__class__.__name__
        self.text = 'Base error.'

    def call(self):
        print(f'\n\033[31m{self.type}({self.token.pos.ln}:{self.token.pos.col}): {self.text}')
        exit()


class InvalidNumberError(Error):
    def __init__(self, token: Token):
        super().__init__(token)
        self.text = f'invalid number {self.token.value}.'


class TypeConversionError(Error):
    def __init__(self, token: Token = ...):
        super().__init__(token)
        self.text = 'conversion is not possible.'


class MathError(Error):
    def __init__(self, token: Token = ...):
        super().__init__(token)
        self.text = 'it is impossible to perform a mathematical operation.'


class IdentifierError(Error):
    def __init__(self, token: Token):
        super().__init__(token)
        self.text = f'identifier was expected, but was received {self.token.value}'


class VariableTypeError(Error):
    def __init__(self, var_typename: str, typename: str, token: Token):
        super().__init__(token)
        self.text = f'variable type mismatch (should be {typename}, but received {var_typename}).'


class VariableOverrideError(Error):
    def __init__(self, var_name: str, token: Token):
        super().__init__(token)
        self.text = f'cannot override the constant ({var_name}) value.'


class NonexistentVariableError(Error):
    def __init__(self, var_name: str, token: Token):
        super().__init__(token)
        self.text = f'variable {var_name} doesn\'t exist.'


class VariableExistsError(Error):
    def __init__(self, var_name: str, token: Token):
        super().__init__(token)
        self.text = f'variable {var_name} already exists.'


class UnexpectedTokenError(Error):
    def __init__(self, token: Token):
        super().__init__(token)
        self.text = f'unexpected token ({token.value}).'


class ReturnException(Exception):
    def __init__(self, value, *args):
        super().__init__(*args)
        self.value = value
