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
