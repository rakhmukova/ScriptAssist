import os
from typing import List, Tuple

from PyQt6.QtCore import QRegularExpression, QRegularExpressionMatch

from models.error_location import ErrorLocation


class ErrorLocationFormatter:
    """
    A class for formatting error locations in an error string.
    """

    # valid only for Linux and macOS
    __ERROR_LOCATION_PATTERN = r'((~|\.\.|\.)?/[\w\d_\s.-]+(/[\w\d_\s.-]+)*.\w+):(\d+):(\d+):'

    @staticmethod
    def format_error_locations(stderr: str, script_path: str) -> str:
        """
        Returns a transformed version of the input error string with links to error locations.

        :param script_path: The current config script path.
        :param str stderr: The error string to transform.
        :return: The transformed error string with error location links.
        """
        error_locations_and_descriptions = ErrorLocationFormatter.__extract_error_locations(stderr)
        if not error_locations_and_descriptions:
            return stderr

        transformed_stderr = ''
        for error_location, error_description in error_locations_and_descriptions:
            # We can only link errors that occur in the script path.
            if ErrorLocationFormatter.__are_paths_same(script_path, error_location.file_path):
                transformed_stderr += ErrorLocationFormatter.__create_link(error_location)
            else:
                transformed_stderr += str(error_location)
            transformed_stderr += f'{error_description}<br>'

        return transformed_stderr

    @staticmethod
    def __extract_error_locations(stderr: str) -> List[Tuple[ErrorLocation, str]]:
        error_locations = []
        regex = QRegularExpression(ErrorLocationFormatter.__ERROR_LOCATION_PATTERN)
        match_iterator = regex.globalMatch(stderr)
        while match_iterator.hasNext():
            match = match_iterator.next()
            error_location = ErrorLocationFormatter.__extract_error_location(match)
            end_index = match.capturedEnd()
            next_start_index = match_iterator.peekNext().capturedStart() if match_iterator.hasNext() else len(stderr)
            error_description = stderr[end_index:next_start_index].split('\n', 1)[0]
            error_locations.append((error_location, error_description))
        return error_locations

    @staticmethod
    def __extract_error_location(match: QRegularExpressionMatch) -> ErrorLocation:
        file_path = match.captured(1)
        line_number = int(match.captured(4))
        column_number = int(match.captured(5))
        return ErrorLocation(file_path, line_number, column_number)

    @staticmethod
    def __create_link(error_location: ErrorLocation):
        link_text = str(error_location)
        return f'<a href="{link_text}">{link_text}:</a>'

    @staticmethod
    def __are_paths_same(first_path: str, second_path: str) -> bool:
        first_norm_path = os.path.normpath(second_path)
        second_norm_path = os.path.normpath(first_path)
        return first_norm_path == second_norm_path
