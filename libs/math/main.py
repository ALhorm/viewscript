from core import Globals, Function, Variable, Void, number, Module, Float
import math


class Abs(Function):
    def __init__(self):
        super().__init__({
            'x': Variable(Void(), True)
        }, True)

    def fn_main(self):
        result = abs(self.get_param('x').as_num())
        return number(result)


class Log(Function):
    def __init__(self):
        super().__init__({
            'x': Variable(Void(), True),
            'b': Variable(Void(), True)
        }, True)

    def fn_main(self):
        return Float(math.log(self.get_param('x').as_float(), self.get_param('b').as_float()))


def main():
    Globals.set_mod('math', Module({
        'pi': Variable(Float(math.pi), True),
        'e': Variable(Float(math.e), True)
    }, {
        'abs': Abs(),
        'log': Log()
    }))
