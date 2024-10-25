from PySide6.QtWidgets import QWidget, QLabel, QSizePolicy

from .Widget import Widget

class Label(Widget):
    def __init__(self, props: dict[str, str]):
        super().__init__(props)
        self.text = props['text']

    def render(self) -> QWidget:
        label = QLabel()
        label.setText(self.text)

        return label
