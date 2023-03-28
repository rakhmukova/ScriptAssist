from PyQt6.QtGui import QPixmap, QIcon
from PyQt6.QtWidgets import QWidget, QHBoxLayout, QLabel, QPushButton, QToolTip

from models.script_config import ScriptConfig


class TopPanel(QWidget):
    """
    A widget that displays a top panel with script information and buttons for running and stopping the script.
    """

    def __init__(self, parent=None):
        """
        Initializes the top panel widget.

        :param parent: Optional parent widget.
        """
        super().__init__(parent)
        self.setObjectName('topPanel')
        self.setFixedHeight(30)

        layout = QHBoxLayout()
        layout.setContentsMargins(2, 0, 10, 0)
        self.setLayout(layout)

        self.script_name_label = QLabel()
        self.script_name_label.setObjectName('scriptLabel')

        self.run_button = self.__init_button('resources/images/run_green.png', 'runButton', 'Run script')
        self.stop_button = self.__init_button('resources/images/stop_darkred.png', 'stopButton', 'Stop script')
        self.edit_config_button = self.__init_button('resources/images/edit_config.png', 'editConfigButton',
                                                     'Edit configuration')

        layout.addWidget(self.script_name_label)
        layout.addStretch()
        layout.addWidget(self.run_button)
        layout.addWidget(self.stop_button)
        layout.addWidget(self.edit_config_button)

    @staticmethod
    def __init_button(image_path: str, button_name: str, tooltip: str) -> QPushButton:
        button = QPushButton()
        pixmap = QPixmap(image_path)
        button.setIcon(QIcon(pixmap))
        button.setObjectName(button_name)

        button.setToolTip(tooltip)
        button.setMouseTracking(True)
        button.enterEvent = lambda event: QToolTip.showText(button.mapToGlobal(button.rect().bottomLeft()), tooltip)
        button.leaveEvent = lambda event: QToolTip.hideText()
        return button

    def on_config_changed(self, config: ScriptConfig):
        """
        Update the script name label when the configuration has changed.

        :param config: The updated script configuration.
        :type config: ScriptConfig
        """
        file_name = config.path.split('/')[-1]
        self.script_name_label.setText(file_name)
