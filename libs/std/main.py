from core import Globals, Function, Void, Variable, Str, Int, Float, Bool


class Print(Function):
    def __init__(self):
        super().__init__({
            'a': Variable(Void(), True),
            'end': Variable(Str('\n'), True)
        }, True)

    def fn_main(self):
        print(self.get_param('a').as_str(), end=self.get_param('end').as_str())


class Input(Function):
    def __init__(self):
        super().__init__({
            'prompt': Variable(Str(''), True)
        }, True)

    def fn_main(self):
        input_ = input(self.get_param('prompt').as_str())
        return Str(input_)


class Type(Function):
    def __init__(self, type_: str):
        super().__init__({
            'v': Variable(Void(), True)
        }, True)
        self.type = type_

    def fn_main(self):
        value = self.get_param('v')

        if self.type == 'int':
            return Int(value.as_int())
        if self.type == 'float':
            return Float(value.as_float())
        if self.type == 'str':
            return Str(value.as_str())
        if self.type == 'bool':
            return Bool(value.as_bool())


class TypeofFunction(Function):
    def __init__(self):
        super().__init__({
            'v': Variable(Void(), True)
        }, True)

    def fn_main(self):
        typename = self.get_param('v').typename
        return Str(typename)


class CmptFunction(Function):
    def __init__(self):
        super().__init__({
            'v': Variable(Void(), True),
            't': Variable(Void(), True)
        }, True)

    def fn_main(self):
        return Bool(self.get_param('v').typename == self.get_param('t').typename)


class WindowFunction(Function):
    def __init__(self):
        super().__init__({
            'layout': Variable(Void(), True),
            'title': Variable(Str('ViewScript Program'), True),
            'width': Variable(Int(700), True),
            'height': Variable(Int(500), True)
        }, True)

    def fn_main(self):
        Globals.set_var('f_layout', Variable(self.get_param('layout'), True))
        Globals.set_var('w_title', Variable(self.get_param('title'), True))
        Globals.set_var('w_width', Variable(self.get_param('width'), True))
        Globals.set_var('w_height', Variable(self.get_param('height'), True))


def main():
    Globals.set_fn('print', Print())
    Globals.set_fn('input', Input())
    Globals.set_fn('int', Type('int'))
    Globals.set_fn('float', Type('float'))
    Globals.set_fn('str', Type('str'))
    Globals.set_fn('bool', Type('bool'))
    Globals.set_fn('typeof', TypeofFunction())
    Globals.set_fn('cmpt', CmptFunction())
    Globals.set_fn('window', WindowFunction())
