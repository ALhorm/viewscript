from PySide6.QtWidgets import QWidget


class Widget:
    def __init__(self, props: dict[str, str]):
        self.props = props

    def render(self) -> QWidget:
        raise NotImplementedError
