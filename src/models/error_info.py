import re


class ErrorInfo:
    """
    A class to represent information about an error.

    :param file_location: The file location where the error occurred.
    :param error_description: The description of the error.
    """

    # valid only for Linux and macOS
    FILE_LOCATION_PATTERN = r'(~|\.\.|\.)?/[\w\d_\s\.-]+(/[\w\d_\s\.-]+)*.\w+:\d+:\d+:'

    def __init__(self, file_location, error_description):
        self.file_location = file_location
        self.description = error_description

    @property
    def file_location(self) -> str:
        """
        Get the file location where the error occurred.

        :return: The file location where the error occurred.
        """
        return self.__file_location

    @file_location.setter
    def file_location(self, new_file_location: str):
        """
        Set the file location where the error occurred.

        :param new_file_location: The new file location.
        :raises ValueError: If the new file location is of invalid format.
        """
        if not re.match(ErrorInfo.FILE_LOCATION_PATTERN, new_file_location):
            raise ValueError(f'Invalid file location format: {new_file_location}')

        self.__file_location = new_file_location
        self.__line_number, self.__column_number = ErrorInfo.__extract_line_and_column(self.file_location)

    @property
    def description(self) -> str:
        """
        Get the description of the error.

        :return: The description of the error.
        """
        return self.__description

    @description.setter
    def description(self, new_description: str):
        """
        Set the description of the error.

        :param new_description: The new description.
        """
        self.__description = new_description

    @property
    def line_number(self) -> int:
        """
        Get the line number where the error occurred.

        :return: The line number where the error occurred.
        """
        return self.__line_number

    @property
    def column_number(self) -> int:
        """
        Get the column number where the error occurred.

        :return: The column number where the error occurred.
        """
        return self.__column_number

    @staticmethod
    def __extract_line_and_column(file_location: str) -> tuple[int, int]:
        """
        Extract the line number and column number from the file location string.

        :param file_location: The file location string.
        :return: A tuple containing the line number and column number.
        :raises ValueError: If the file location string has an invalid format.
        """
        pattern = re.compile(r':(\d+):(\d+):')
        match = pattern.search(file_location)
        if not match:
            raise ValueError(f'Invalid file location format: {file_location}')

        line_number = int(match.group(1))
        column_number = int(match.group(2))
        return line_number, column_number
