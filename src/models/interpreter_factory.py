from models.interpreter_config import InterpreterConfig
from models.script_type import ScriptType


class InterpreterFactory:
    """
    A factory class for creating InterpreterConfig instances based on ScriptConfig objects
    """

    @staticmethod
    def get_interpreter_config(script_type: ScriptType) -> InterpreterConfig:
        """
        Returns a new instance of InterpreterConfig for the given script type.

        :param script_type: The script type.
        :return: A new InterpreterConfig instance.
        :raises ValueError: If the script type is not supported.
        """
        if script_type == ScriptType.KOTLIN:
            path, options = 'kotlinc', ['-script']
        elif script_type == ScriptType.SWIFT:
            path, options = '/usr/bin/env', ['swift']
        else:
            raise ValueError('Undefined script type.')
        return InterpreterConfig(path, options)
