from src.models.script_config import ScriptConfig
from src.models.script_runner import ScriptRunner


class RunnerFactory:
    """
    A factory class for creating ScriptRunner instances based on ScriptConfig objects
    """
    @staticmethod
    def get_runner(config: ScriptConfig) -> ScriptRunner:
        """
        Returns a new instance of ScriptRunner for the given script config.

        :param config: The script config to use.
        :return: A new ScriptRunner instance.
        :raises ValueError: If the script type is not supported.
        """
        interpreter_path, interpreter_options = RunnerFactory._get_interpreter_config(config.script_type)
        return ScriptRunner(interpreter_path, interpreter_options, config.path, config.parameters)

    @staticmethod
    def _get_interpreter_config(script_type: str) -> (str, list):
        """
        Returns the interpreter path and options for the given script type.

        :param script_type: The script type to use.
        :return: A tuple containing the interpreter path and options.
        :raises ValueError: If the script type is not supported.
        """
        if script_type == 'Kotlin':
            interpreter_path = 'kotlinc'
            interpreter_options = ['-script']
        elif script_type == 'Swift':
            interpreter_path = '/usr/bin/env'
            interpreter_options = ['swift']
        else:
            raise ValueError(f'Unsupported script type: {script_type}')
        return interpreter_path, interpreter_options
