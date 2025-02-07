from core.errors import Error, UnexpectedTokenError
from core.lexer import Lexer
from core.tokens import Token, TokenType, TKeyword, TPlus, TMinus, TStar, TSlash, TNumber, TString, T_EOF, Position, \
    T_OR_BKT, T_CR_BKT, TOr, TAnd, TEqual, TNotEqual, TGreater, TGreaterEqual, TLess, TLessEqual, T_CC_BKT, T_OC_BKT, \
    TExPoint, TIdentifier, TAssign, TComma, TModGet, TRef
from core.ast import *


class Parser:
    def __init__(self, tokens: list[Token]):
        self.tokens = tokens
        self.pos = 0
        self.current_token = tokens[0]
        self.public_statements = []

    def parse(self) -> list[Statement]:
        statements = []

        while not self.match(T_EOF):
            statements.append(self.statement())

        return statements

    def next(self):
        self.pos += 1

        if self.pos >= len(self.tokens):
            return Token(T_EOF, '\0', Position(-1, -1, -1))

        self.current_token = self.tokens[self.pos]

    def match(self, type_: TokenType, keyword: str = ...) -> bool:
        check = self.current_token.type == type_

        if type_ == TKeyword:
            check = self.current_token.value == keyword

        if not check:
            return False

        self.next()
        return True

    def match_pos(self, pos: int, type_: TokenType, keyword: str = ...) -> bool:
        position = self.pos + pos

        if position >= len(self.tokens):
            return False

        token = self.tokens[position]

        return token.value == keyword if type_ == TKeyword else token.type == type_

    def must(self, type_: TokenType, keyword: str = ..., errc: Error = ...) -> Token:
        check = self.current_token.type == type_

        if errc is ...:
            errc = UnexpectedTokenError(self.current_token)
        if type_ == TKeyword:
            check = self.current_token.value == keyword
        if not check:
            errc.call()

        token = self.current_token
        self.next()
        return token

    def statement(self) -> Statement:
        if self.match(TKeyword, 'if'):
            return self.if_stmt()
        if self.match(TKeyword, 'let'):
            return self.let_stmt()
        if self.match(TKeyword, 'ret'):
            return ReturnStatement(self.expression())
        if self.match(TKeyword, 'mod'):
            return self.mod_stmt()
        if self.match_pos(1, TModGet):
            return ModGetStatement(self.mod_get_expr())
        if self.match(TKeyword, 'loadlib'):
            return self.loadlib_stmt()
        if self.match(TKeyword, 'pub'):
            return self.pub_stmt()

        return FunctionCallStatement(self.fn_call_expr())

    def block_stmt(self) -> Statement:
        statements = []

        while not self.match(T_CC_BKT):
            statements.append(self.statement())

        return BlockStatement(statements)

    def block_or_stmt(self) -> Statement:
        if self.match(T_OC_BKT):
            return self.block_stmt()

        return self.statement()

    def if_stmt(self) -> Statement:
        if_exprs = [self.expression()]
        if_stmts = [self.block_or_stmt()]

        while self.match(TKeyword, 'elif'):
            if_exprs.append(self.expression())
            if_stmts.append(self.block_or_stmt())

        else_stmt = self.block_or_stmt() if self.match(TKeyword, 'else') else None
        return IfStatement(if_exprs, if_stmts, else_stmt)

    def let_stmt(self) -> Statement:
        is_const = self.match(TExPoint)

        if self.match(TKeyword, 'fn'):
            return self.fn_let_stmt(is_const)

        name = self.must(TIdentifier).value
        self.must(TAssign)

        return LetStatement(name, self.expression(), is_const)

    def fn_let_stmt(self, is_const: bool) -> Statement:
        params = {}

        self.must(T_OR_BKT)
        while not self.match(T_CR_BKT):
            p_name = self.must(TIdentifier).value
            p_value = None

            if self.match(TAssign):
                p_value = self.expression()

            self.match(TComma)
            params[p_name] = p_value

        name = self.must(TIdentifier).value
        self.must(TAssign)

        return FunctionLetStatement(name, params, self.block_or_stmt(), is_const)

    def mod_stmt(self) -> Statement:
        name = self.must(TIdentifier).value
        statements = []

        self.must(T_OC_BKT)
        while not self.match(T_CC_BKT):
            statement = self.statement()

            if isinstance(statement, FunctionLetStatement) or isinstance(statement, LetStatement):
                statements.append(statement)

        return ModStatement(name, statements)

    def loadlib_stmt(self) -> Statement:
        statements = None
        lib_name = None

        if self.match_pos(0, TString):
            file = self.current_token.value
            self.next()
            lexer = Lexer(file)
            parser = Parser(lexer.lex())
            parser.parse()
            statements = parser.public_statements
        else:
            lib_name = self.must(TIdentifier).value

        return LoadlibStatement(lib_name, statements)

    def pub_stmt(self) -> Statement:
        statement = self.statement()
        self.public_statements.append(statement)
        return statement

    def expression(self) -> Expression:
        return self.or_expr()

    def or_expr(self) -> Expression:
        result = self.and_expr()

        while True:
            if self.match(TOr):
                result = LogicalExpression(result, self.and_expr(), '||')
                continue
            break

        return result

    def and_expr(self) -> Expression:
        result = self.eq_expr()

        while True:
            if self.match(TAnd):
                result = LogicalExpression(result, self.eq_expr(), '&&')
                continue
            break

        return result

    def eq_expr(self) -> Expression:
        result = self.gr_ls_expr()

        if self.match(TEqual):
            return LogicalExpression(result, self.gr_ls_expr(), '==')
        if self.match(TNotEqual):
            return LogicalExpression(result, self.gr_ls_expr(), '!=')

        return result

    def gr_ls_expr(self) -> Expression:
        result = self.add_expr()

        while True:
            if self.match(TGreater):
                result = LogicalExpression(result, self.add_expr(), '>')
                continue
            if self.match(TGreaterEqual):
                result = LogicalExpression(result, self.add_expr(), '>=')
                continue
            if self.match(TLess):
                result = LogicalExpression(result, self.add_expr(), '<')
                continue
            if self.match(TLessEqual):
                result = LogicalExpression(result, self.add_expr(), '<=')
                continue
            break

        return result

    def add_expr(self) -> Expression:
        result = self.mul_expr()

        while True:
            if self.match(TPlus):
                result = BinaryExpression(result, self.mul_expr(), '+')
                continue
            if self.match(TMinus):
                result = BinaryExpression(result, self.mul_expr(), '-')
                continue
            break

        return result

    def mul_expr(self) -> Expression:
        result = self.unary_expr()

        while True:
            if self.match(TStar):
                result = BinaryExpression(result, self.unary_expr(), '*')
                continue
            if self.match(TSlash):
                result = BinaryExpression(result, self.unary_expr(), '/')
                continue
            break

        return result

    def unary_expr(self) -> Expression:
        if self.match(TMinus):
            return UnaryExpression(self.mod_get_expr())

        return self.mod_get_expr()

    def mod_get_expr(self) -> Expression:
        if self.match_pos(1, TModGet):
            mod_name = self.must(TIdentifier).value
            self.must(TModGet)
            gl_name = self.current_token.value

            return ModGetExpression(mod_name, gl_name, self.fn_call_expr())

        return self.fn_call_expr()

    def fn_call_expr(self) -> Expression | FunctionCallExpression:
        result = self.primary_expr()

        if self.match(T_OR_BKT):
            args = {}
            i = 0

            while not self.match(T_CR_BKT):
                is_assign = self.match_pos(1, TAssign)
                a_name = self.current_token.value if is_assign else i

                if is_assign:
                    self.next()
                    self.next()

                args[a_name] = self.expression()
                self.match(TComma)
                i += 1

            return FunctionCallExpression(result, args)

        return result

    def primary_expr(self) -> Expression | str:
        value = self.current_token.value

        if self.match(TNumber) or self.match(TString):
            return ValueExpression(value)
        if self.match(TKeyword, 'true'):
            return ValueExpression(True)
        if self.match(TKeyword, 'false'):
            return ValueExpression(False)
        if self.match(T_OR_BKT):
            result = self.expression()
            self.must(T_CR_BKT)
            return result
        if self.match_pos(0, TIdentifier):
            name = self.current_token.value
            self.next()

            if self.match_pos(0, T_OR_BKT):
                return name

            return IdentifierExpression(name)
        if self.match(TRef):
            return RefExpression(self.must(TIdentifier).value)
