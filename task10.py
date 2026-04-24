# -*- coding: utf-8 -*-
import sys

from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget


class Window(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Task 10 — Простейший GUI на PyQt5")
        self.resize(420, 160)

        self.label = QLabel("Привет! Это PyQt5.")
        self.button = QPushButton("Нажми меня")
        self.button.clicked.connect(self.on_click)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.button)
        self.setLayout(layout)

    def on_click(self) -> None:
        self.label.setText("Кнопка нажата!")


def main() -> None:
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
