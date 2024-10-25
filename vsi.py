from viewscript import Lexer, Parser, start
from viewscript.std import Variables

with open('main.vs', 'r') as f:
    code = f.read()
    lines = [i.strip() for i in code.split('\n')]
    lexer = Lexer(code)

tokens = lexer.lex()
parser = Parser(tokens)

try:
    parser.parse()
except Exception as e:
    token = e.args[1]
    print(f'Error({token.line}:{token.col}): {e.args[0]}\n' + f'{token.line}. {lines[token.line - 1]}')

if __name__ == '__main__':
    w_title = Variables.get('w_title').as_str()
    w_width = Variables.get('w_width').as_int()
    w_height = Variables.get('w_height').as_int()
    layout_file = Variables.get('f_layout').as_str()

    start(layout_file, w_title, (w_width, w_height))
