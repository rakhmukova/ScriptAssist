from PyQt6.QtWidgets import QApplication

from src.ui.mainwindow import MainWindow

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()

    with open("resources/styles.qss", "r") as file:
        app.setStyleSheet(file.read())

    window.show()
    app.exec()
