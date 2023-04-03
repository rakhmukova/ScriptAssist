from PyQt6.QtCore import QRegularExpression

from models.error_info import ErrorInfo


class ErrorInfoExtractor:
    @staticmethod
    def extract_errors(stderr: str) -> list[ErrorInfo]:
        """
        Extracts errors from a given error string.

        :param stderr: The error string to extract errors from.
        :return: A list of ErrorInfo objects representing the errors found in the input string.
        """
        error_locations = ErrorInfoExtractor.__find_file_locations(stderr)
        errors = ErrorInfoExtractor.__split_errors(stderr, error_locations)
        return errors

    @staticmethod
    def __find_file_locations(error_text: str) -> list[tuple[int, int]]:
        """
        Finds the locations of file names in a given error string.

        :param error_text: The error string to find file locations in.
        :return: A list of tuples representing the start and end indices of file locations found in the input string.
        """
        file_locations = []
        regex = QRegularExpression(ErrorInfo.FILE_LOCATION_PATTERN)
        match_iterator = regex.globalMatch(error_text)
        while match_iterator.hasNext():
            match = match_iterator.next()
            start_index = match.capturedStart()
            end_index = match.capturedEnd()
            file_locations.append((start_index, end_index))

        return file_locations

    @staticmethod
    def __split_errors(error_text: str, file_locations: list[tuple[int, int]]) -> list[ErrorInfo]:
        """
        Splits a given error string into ErrorInfo objects.

        :param error_text: The error string to split.
        :param file_locations: A list of tuples representing the start and end indices of file locations
        in the error string.
        :return: A list of ErrorInfo objects representing the
        errors found in the input string.
        """
        errors = []
        file_locations.append((len(error_text), 0))
        for i in range(0, len(file_locations) - 1):
            start_index, end_index = file_locations[i]
            next_start_index, _ = file_locations[i + 1]
            file_location = error_text[start_index:end_index]
            error_description = error_text[end_index:next_start_index].split('\n', 1)[0]
            errors.append(ErrorInfo(file_location, error_description))

        return errors
