import pytest
from PyQt6.QtCore import QCoreApplication

from models.file_util import FileUtil
from models.interpreter_config import InterpreterConfig
from models.interpreter_factory import InterpreterFactory
from models.script_config import ScriptConfig
from models.script_runner import ScriptRunner
from models.script_type import ScriptType


class TestScriptRunner:
    @classmethod
    def setup_class(cls):
        """
        Set up the QApplication object to enable Qt event loop
        """
        cls.app = QCoreApplication.instance() or QCoreApplication([])

    @pytest.fixture
    def default_script_config(self) -> ScriptConfig:
        """
        Fixture that returns the default ScriptConfig instance.
        """
        return ScriptConfig('script.swift')

    @pytest.fixture
    def swift_interpreter_config(self, default_script_config) -> InterpreterConfig:
        """
        Fixture that returns an InterpreterConfig instance for the Swift interpreter.
        """
        return InterpreterFactory.get_interpreter_config(ScriptType.SWIFT)

    @pytest.fixture
    def kotlin_interpreter_config(self, default_script_config) -> InterpreterConfig:
        """
        Fixture that returns an InterpreterConfig instance for the Kotlin interpreter.
        """
        return InterpreterFactory.get_interpreter_config(ScriptType.KOTLIN)

    def test_run_script(self, tmpdir, kotlin_interpreter_config):
        """
        Test the run method of the ScriptRunner class with a Kotlin script.
        """
        script_path = str(tmpdir.join('script.kts'))
        script_content = """
        println("Hello, world!")
        """
        FileUtil.save_to_file(script_path, script_content)

        data = ''

        def handle_stdout(signal_data):
            nonlocal data
            data += signal_data

        runner = ScriptRunner(kotlin_interpreter_config, ScriptConfig(script_path))
        runner.stdout_received.connect(handle_stdout)
        runner.run()
        runner.process.waitForFinished()

        assert data == 'Hello, world!\n'

    def test_cancel_script(self, tmpdir, swift_interpreter_config, default_script_config):
        """
        Test the cancel method of the ScriptRunner class with a Swift script.
        """
        script_path = str(tmpdir.join('script.swift'))
        script_content = """
        while true {
            print("This is an infinite loop!")
        }
        """
        FileUtil.save_to_file(script_path, script_content)

        exit_code = None

        def handle_finish(signal_exit_code):
            nonlocal exit_code
            exit_code = signal_exit_code

        script_config = ScriptConfig(script_path)
        runner = ScriptRunner(swift_interpreter_config, script_config)
        runner.finished.connect(handle_finish)
        runner.run()

        runner.cancel()

        assert exit_code == 15

    def test_missing_script(self, swift_interpreter_config):
        """
        Test that the ScriptRunner raises a ValueError if the script file does not exist.
        """
        with pytest.raises(ValueError):
            script_runner = ScriptRunner(swift_interpreter_config, ScriptConfig('nonexistent_script.swift'))
            script_runner.run()

    def test_missing_interpreter(self, default_script_config):
        """
        Test that the ScriptRunner raises a ValueError if the interpreter path does not exist.
        """
        with pytest.raises(ValueError):
            script_runner = ScriptRunner(InterpreterConfig('nonexistent_interpreter'), default_script_config)
            script_runner.run()
