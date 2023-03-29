import os
import pytest

from models.file_util import FileUtil


class TestFileUtil:
    """
    A collection of test cases for the FileUtil class.
    """

    @pytest.fixture
    def fixture_file_content(self) -> str:
        """
        Fixture that returns the content to be used for test files.
        """
        return 'some content'

    @pytest.fixture
    def fixture_nonexistent_path(self) -> str:
        """
        Fixture that returns a path to a nonexistent file.
        """
        file_path = 'nonexistent_file.txt'
        return file_path

    @pytest.fixture
    def fixture_new_path(self) -> str:
        """
        Fixture that yields a path to a new test file.
        """
        file_path = 'new_file.txt'
        yield file_path
        os.remove(file_path)

    @pytest.fixture
    def fixture_existing_path(self, tmp_path: str, fixture_file_content: str) -> str:
        """
        Fixture that yields a path to an existing test file.
        """
        file_path = tmp_path / 'test_file.txt'
        with open(file_path, 'w') as f:
            f.write(fixture_file_content)
        yield str(file_path)
        os.remove(file_path)

    def test_upload_file(self, fixture_existing_path: str, fixture_file_content: str) -> None:
        """
        Test the upload_file method of the FileUtil class with an existing file path.
        """
        script_content = FileUtil.upload_file(fixture_existing_path)
        assert script_content == fixture_file_content

    def test_upload_file_not_found(self, fixture_nonexistent_path: str) -> None:
        """
        Test the upload_file method of the FileUtil class with a nonexistent file path.
        """
        script_content = FileUtil.upload_file(fixture_nonexistent_path)
        assert script_content is None

    def test_save_to_file(self, fixture_existing_path: str, fixture_file_content: str) -> None:
        """
        Test the save_to_file method of the FileUtil class with an existing file path.
        """
        FileUtil.save_to_file(fixture_existing_path, fixture_file_content)
        self.check_content_is_saved(fixture_existing_path, fixture_file_content)

    def test_save_to_file_create_new(self, fixture_new_path: str, fixture_file_content: str) -> None:
        """
        Test the save_to_file method of the FileUtil class with a new file path.
        """
        FileUtil.save_to_file(fixture_new_path, fixture_file_content)
        self.check_content_is_saved(fixture_new_path, fixture_file_content)

    @staticmethod
    def check_content_is_saved(path: str, content: str) -> None:
        """
        Helper function to check that the content is correctly saved to a file.
        """
        try:
            with open(path, 'r') as f:
                saved_content = f.read()
                assert saved_content == content
        except IOError:
            assert False
