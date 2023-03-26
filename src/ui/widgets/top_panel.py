from PyQt6.QtGui import QPixmap, QIcon
from PyQt6.QtWidgets import QWidget, QHBoxLayout, QLabel, QPushButton, QToolTip


class TopPanel(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName('topPanel')
        self.setFixedHeight(30)

        layout = QHBoxLayout()
        layout.setContentsMargins(2, 0, 10, 0)
        self.setLayout(layout)

        self.script_name_label = QLabel()
        self.script_name_label.setObjectName('scriptLabel')

        self.run_button = self.init_button('resources/images/run_green.png', 'runButton', 'Run script')
        self.stop_button = self.init_button('resources/images/stop_darkred.png', 'stopButton', 'Stop script')
        self.edit_config_button = self.init_button('resources/images/edit_config.png', 'editConfigButton',
                                                   'Edit configuration')

        layout.addWidget(self.script_name_label)
        layout.addStretch()
        layout.addWidget(self.run_button)
        layout.addWidget(self.stop_button)
        layout.addWidget(self.edit_config_button)

    @staticmethod
    def init_button(image_path, button_name, tooltip):
        button = QPushButton()
        pixmap = QPixmap(image_path)
        button.setIcon(QIcon(pixmap))
        button.setObjectName(button_name)

        button.setToolTip(tooltip)
        button.setMouseTracking(True)
        button.enterEvent = lambda event: QToolTip.showText(button.mapToGlobal(button.rect().bottomLeft()),
                                                            tooltip)
        button.leaveEvent = lambda event: QToolTip.hideText()
        return button
