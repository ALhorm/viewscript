from os.path import abspath
from core.datatypes import Str
from core.globals import Globals, Variable
from core.lexer import Lexer
from core.parser import Parser
from core import start

file = 'main.vs'
Globals.set_var('__file__', Variable(Str(abspath(file)), True))

lexer = Lexer(file)
parser = Parser(lexer.lex())
statements = parser.parse()

for statement in statements:
    statement.execute()

if __name__ == '__main__':
    w_title = Globals.get_var('w_title').value.as_str()
    w_width = Globals.get_var('w_width').value.as_int()
    w_height = Globals.get_var('w_height').value.as_int()
    layout_file = Globals.get_var('f_layout').value.as_str()

    start(layout_file, w_title, (w_width, w_height))
