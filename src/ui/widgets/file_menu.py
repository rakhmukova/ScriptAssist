from PyQt6.QtCore import pyqtSignal
from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QMenu, QWidget

from models.file_util import FileUtil
from models.script_config import ScriptConfig
from models.script_type_options import ScriptTypeOptions


class FileMenu(QMenu):
    """
    A menu for file-related actions, such as opening and saving scripts.
    """

    script_config_changed = pyqtSignal(ScriptConfig)
    save_clicked = pyqtSignal()
    save_as_clicked = pyqtSignal()

    def __init__(self, parent: QWidget):
        super().__init__('File', parent)
        self.__create_actions()

    def __create_actions(self):
        open_action = QAction('Open', self)
        open_action.setShortcut('Ctrl+O')
        open_action.triggered.connect(self.__on_open)
        self.addAction(open_action)

        save_action = QAction('Save', self)
        save_action.setShortcut('Ctrl+S')
        save_action.triggered.connect(self.__on_save)
        self.addAction(save_action)

        save_as_action = QAction('Save As', self)
        save_as_action.triggered.connect(self.__on_save_as)
        self.addAction(save_as_action)

    def __on_open(self):
        extensions = ScriptTypeOptions.get_available_script_extensions()
        file_path = FileUtil.browse_file(self.parentWidget(), 'Select File', '../example_scripts',
                                         ';;'.join(extensions))
        if file_path:
            script_config = ScriptConfig(file_path)
            self.script_config_changed.emit(script_config)

    def __on_save(self):
        self.save_clicked.emit()

    def __on_save_as(self):
        self.save_as_clicked.emit()
