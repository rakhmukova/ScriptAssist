from typing import Optional

from models.script_type import ScriptType


class ScriptTypeOptions:
    """
    A class for storing options related to script type.
    """

    __SCRIPT_TYPE_TO_EXTENSION_OPTION = {
        ScriptType.KOTLIN.value: 'Kotlin Files (*.kts)',
        ScriptType.SWIFT.value: 'Swift Files (*.swift)'
    }

    __EXTENSION_TO_SCRIPT_TYPE = {
        '.kts': ScriptType.KOTLIN,
        '.swift': ScriptType.SWIFT,
    }

    @staticmethod
    def get_extension_option(script_type_name: any) -> Optional[str]:
        """
        Get the file extension option for a given script type.

        :param script_type_name: the script type.
        :return: the file extension option.
        """
        if script_type_name in ScriptTypeOptions.__SCRIPT_TYPE_TO_EXTENSION_OPTION:
            return ScriptTypeOptions.__SCRIPT_TYPE_TO_EXTENSION_OPTION.get(script_type_name)
        return ''

    @staticmethod
    def get_script_type(extension: str) -> ScriptType:
        """
        Get the script type for a given file extension.

        :param extension: the file extension.
        :return: the script type.
        """
        if extension in ScriptTypeOptions.__EXTENSION_TO_SCRIPT_TYPE:
            return ScriptTypeOptions.__EXTENSION_TO_SCRIPT_TYPE.get(extension)
        return ScriptType.UNDEFINED

    @staticmethod
    def get_available_script_type_names() -> list[any]:
        """
        Get a list of available script type names.

        :return: the list of available script type names.
        """
        return [script_type.value for script_type in ScriptType
                if script_type is not ScriptType.UNDEFINED]

    @staticmethod
    def get_available_script_extensions() -> list[str]:
        """
        Get a list of available script file extensions.

        :return: the list of available script file extensions.
        """
        return [ScriptTypeOptions.get_extension_option(script_type_value) for script_type_value
                in ScriptTypeOptions.get_available_script_type_names()]
