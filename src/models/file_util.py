import os
from typing import Optional

from PyQt6.QtWidgets import QFileDialog, QWidget


class FileUtil:
    @staticmethod
    def browse_file(parent: QWidget = None, caption: str = '', directory: str = '',
                    file_type: str = 'All Files (*)') -> str:
        """Open a file dialog to select a file.

        :param directory: The default directory to browse files in.
        :param caption: The caption for the file dialog.
        :param parent: The parent widget for the file dialog.
        :param file_type: The file types to be shown in the dialog.
        :return: The selected file's path.
        """
        file_path, _ = QFileDialog.getOpenFileName(parent, caption, directory, file_type)
        return file_path

    @staticmethod
    def save_file(parent: QWidget = None, caption: str = '', directory: str = '',
                  file_type: str = 'All Files (*)') -> str:
        """Open a file dialog to save a file.

        :param directory: The default directory to save files in.
        :param caption: The caption for the file dialog.
        :param parent: The parent widget for the file dialog.
        :param file_type: The file types to be shown in the dialog.
        """
        file_name, _ = QFileDialog.getSaveFileName(parent, caption, directory, file_type)
        if file_name and not os.path.exists(file_name):
            # Create a file manually
            try:
                with open(file_name, 'a'):
                    pass
            except IOError:
                return ''
        return file_name

    @staticmethod
    def upload_file(file_path: str) -> Optional[str]:
        """Read the contents of a file and return them as a string.

        :param file_path: The path of the file to read.
        :return: The contents of the file as a string, or None if an error occurred.
        """
        try:
            with open(file_path, 'r') as f:
                script_content = f.read()
            return script_content
        except IOError:
            return None

    @staticmethod
    def save_to_file(file_path: str, content: str) -> bool:
        """Save the given content to the specified file.

        :param file_path: The path of the file to write to.
        :param content: The content to be written to the file.
        :return: True if the content was saved successfully, or False if an error occurred.
        """
        try:
            with open(file_path, 'w') as f:
                f.write(content)
            return True
        except IOError:
            return False
