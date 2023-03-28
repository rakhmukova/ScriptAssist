from PyQt6.QtWidgets import QApplication

from ui.dialogues.start_dialog import StartDialog
from ui.mainwindow import MainWindow

if __name__ == '__main__':
    app = QApplication([])
    with open("resources/styles.qss", "r") as file:
        app.setStyleSheet(file.read())

    start_dialog = StartDialog()
    if start_dialog.exec():
        start_config = start_dialog.get_script_config()
        main_window = MainWindow(start_config)
        main_window.show()
        app.exec()
