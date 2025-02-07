from core import Globals, Function, Void, Variable, Int, Float, Module
import random


class Range(Function):
    def __init__(self):
        super().__init__({
            'min': Variable(Void(), True),
            'max': Variable(Void(), True)
        }, True)

    def fn_main(self):
        min_ = self.get_param('min')
        max_ = self.get_param('max')

        if min_.typename == 'int':
            return Int(random.randint(min_.as_int(), max_.as_int()))

        return Float(random.uniform(min_.as_float(), max_.as_float()))


def main():
    Globals.set_mod('rand', Module({}, {
        'range': Range()
    }))
