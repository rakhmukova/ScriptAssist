import pytest
from models.script_type import ScriptType
from models.interpreter_factory import InterpreterFactory


class TestInterpreterFactory:
    """
    A collection of test cases for the InterpreterFactory class.
    """

    def test_get_interpreter_config_kotlin(self):
        """
        Test that get_interpreter_config returns the expected InterpreterConfig for Kotlin scripts.
        """
        script_type = ScriptType.KOTLIN
        interpreter_config = InterpreterFactory.get_interpreter_config(script_type)
        assert interpreter_config.path == 'kotlinc'
        assert interpreter_config.options == ['-script']

    def test_get_interpreter_config_swift(self):
        """
        Test that get_interpreter_config returns the expected InterpreterConfig for Swift scripts.
        """
        script_type = ScriptType.SWIFT
        interpreter_config = InterpreterFactory.get_interpreter_config(script_type)
        assert interpreter_config.path == '/usr/bin/env'
        assert interpreter_config.options == ['swift']

    def test_get_interpreter_config_invalid(self):
        """
        Test that get_interpreter_config raises a ValueError for an unsupported script type.
        """
        script_type = ScriptType.UNDEFINED
        with pytest.raises(ValueError):
            InterpreterFactory.get_interpreter_config(script_type)
