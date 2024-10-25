from PySide6.QtWidgets import QApplication
from .App import Window
from .widgets import *
import sys

app = QApplication(sys.argv)
window = Window()

def convert_layout(file: str):
    with open(file, 'r') as f:
        lines = [i.strip() for i in f.readlines()]

    name = ''
    props = {}
    for line in lines:
        if line == ';':
            widget = globals()[name](props)
            window.add_widget(widget.render())

            name = ''
            props = {}
            continue

        line = line.split(':')

        if len(name) == 0:
            name = line[0]
            continue

        prop = ' '.join(line[1:]).strip()
        props[line[0]] = prop

def start(layout_file: str, w_title: str, w_size: tuple[int, int]):
    window.setWindowTitle(w_title)
    window.resize(*w_size)
    convert_layout(layout_file)
    window.show()
    sys.exit(app.exec())
