from PyQt6.QtWidgets import QLabel


class ScriptStatusLabel(QLabel):
    """
    A label widget that displays the status of a running script.

    This widget can display three different status messages:
    - "Ready" (default message)
    - "Running..."
    - "Finished with exit code X" (where X is the exit code of the script)

    Use the methods `show_ready_status()`, `show_run_status()`, and `show_finish_status()`
    to set the appropriate message and styling.

    Inherits from QLabel.
    """

    def __init__(self):
        """
        Constructs a new ScriptStatusLabel object.

        This widget is initially set to display "Ready" with black text.
        """
        super().__init__()

        self.setObjectName('runIndicationLabel')

    def show_finish_status(self, exit_code: int):
        """
        Sets the widget's text to "Finished with exit code X" and applies dark red styling
        in case exit code is not zero.

        :param exit_code: The exit code of the script.
        """
        if exit_code != 0:
            self.setStyleSheet('color: darkred')
        self.setText(f'Finished with exit code {exit_code}')

    def show_run_status(self):
        """
        Sets the widget's text to "Running..." and applies black styling.
        """
        self.setText('Running...')
        self.setStyleSheet('color: black')

    def show_ready_status(self):
        """
        Sets the widget's text to "Ready" and applies black styling.
        """
        self.setText('Ready')
        self.setStyleSheet('color: black')
