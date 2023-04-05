class ErrorLocation:
    """
    A class to represent a location where the error occurred.
    """

    def __init__(self, file_path: str, line_number: int, column_number: int):
        self.__file_path = file_path
        self.__line_number = line_number
        self.__column_number = column_number

    @property
    def file_path(self) -> str:
        """
        Get the file path where the error occurred.

        :return: The file path where the error occurred.
        """
        return self.__file_path

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

    def __str__(self) -> str:
        """
        Return a string representation of the ErrorLocation object.

        :return: A string representation of the ErrorLocation object.
        """
        return f'{self.__file_path}:{self.__line_number}:{self.__column_number}'

    @classmethod
    def from_string(cls, string: str) -> 'ErrorLocation':
        """
        Create a new ErrorLocation object from a string.

        :param string: The string representation of the ErrorLocation object.
        :return: A new ErrorLocation object.
        :raises ValueError: If the string has an invalid format.
        """
        parts = string.split(':')
        if len(parts) != 3:
            raise ValueError(f'Invalid ErrorLocation string: {string}')

        file_path, line_number, column_number = parts
        line_number = int(line_number)
        column_number = int(column_number)
        return cls(file_path, line_number, column_number)
