from src.models.script_runner import ScriptRunner


class RunnerFactory:
    @staticmethod
    def get_runner(config):
        script_type = config.script_type
        if script_type == 'Kotlin':
            interpreter_path = 'kotlinc'
            interpreter_options = ['-script']
        elif script_type == 'Swift':
            interpreter_path = '/usr/bin/env'
            interpreter_options = ['swift']
        else:
            raise ValueError(format)

        return ScriptRunner(interpreter_path, interpreter_options, config.path, config.parameters)
