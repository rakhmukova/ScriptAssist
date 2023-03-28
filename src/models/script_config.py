import os

from models.script_type import ScriptType


class ScriptConfig:
    """
    Represents a script configuration, including its path, script type, and parameters.
    """

    _EXTENSION_TO_SCRIPT_TYPE = {
        '.kts': ScriptType.KOTLIN,
        '.swift': ScriptType.SWIFT,
    }

    def __init__(self, path: str = '', parameters: list[str] = None):
        """
        Creates a new ScriptConfig instance.

        :param path: The path to the script file.
        :param parameters: Any additional parameters to pass to the script.
        """
        if parameters is None:
            parameters = []

        self.path = path
        self.parameters = parameters

    @property
    def path(self) -> str:
        """
        Gets the path to the script file.

        :return: The path to the script file.
        """
        return self.__path

    @path.setter
    def path(self, new_path: str):
        """
        Sets the path to the script file.

        :param new_path: The new path to the script file.
        """
        self.__path = new_path
        self.__script_type = self.__define_script_type(new_path)

    @property
    def script_type(self) -> ScriptType:
        """
        Gets the script type.

        :return: The script type.
        """
        return self.__script_type

    @property
    def parameters(self) -> list:
        """
        Gets the additional parameters to pass to the script.

        :return: The additional parameters to pass to the script.
        """
        return self.__parameters

    @parameters.setter
    def parameters(self, new_parameters: list[str]):
        """
        Sets the additional parameters to pass to the script.

        :param new_parameters: The new additional parameters to pass to the script.
        """
        self.__parameters = new_parameters

    def __define_script_type(self, path: str) -> ScriptType:
        """
        Determines the script type based on the file extension.

        :param path: The path to the script file.
        :return: The script type.
        """
        _, ext = os.path.splitext(path)
        if ext in self._EXTENSION_TO_SCRIPT_TYPE:
            return self._EXTENSION_TO_SCRIPT_TYPE[ext]

        return ScriptType.UNDEFINED
