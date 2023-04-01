import pytest


from models.error_info import ErrorInfo
from models.error_info_extractor import ErrorInfoExtractor


class TestErrorInfo:
    def test_invalid_file_locations(self):
        """
        Test that ValueError is raised when invalid file locations are passed to ErrorInfo constructor.
        """
        error_message = ' error message'
        invalid_locations = [
            '~',
            './directory',
            '~/path/to/file',
            '../path/to/file.swift',
            '/path/to/file.kts:1'
            'path/to/file.swift:20:1'
        ]

        for invalid_location in invalid_locations:
            with pytest.raises(ValueError) as e:
                ErrorInfo(invalid_location, error_message)
                assert str(e.value) == f'Invalid file location format: {invalid_location}'

    def test_extract_errors(self):
        """
        Test that ErrorInfoExtractor correctly extracts ErrorInfo objects from stderr output.
        """
        stderr = './file-1.swift:1:2: error message\n../path/to/file 2.kts:5:6001: warning ' \
                 'message\n~/path2/to/file_3.py:20:36: note message\n'
        expected_errors = [
            ErrorInfo('./file-1.swift:1:2:', ' error message\n'),
            ErrorInfo('../path/to/file 2.kts:5:6001:', ' warning message\n'),
            ErrorInfo('~/path2/to/file_3.py:20:36:', ' note message\n')
        ]

        actual_errors = ErrorInfoExtractor.extract_errors(stderr)

        assert len(actual_errors) == 3
        for i in range(3):
            assert actual_errors[i].file_location == expected_errors[i].file_location
            assert actual_errors[i].description == expected_errors[i].description
