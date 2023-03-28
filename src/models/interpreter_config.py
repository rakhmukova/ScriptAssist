class InterpreterConfig:
    """
    A configuration class for an interpreter.
    """
    def __init__(self, path: str, options: list[str] = None):
        """
        Initializes a new instance of the InterpreterConfig class.

        :param path: The path of the interpreter executable.
        :param options: The list of command-line options to pass to the interpreter.
        """
        if options is None:
            options = []

        self.path = path
        self.options = options

    @property
    def path(self) -> str:
        """
        Gets the path to the interpreter.

        :return: The path to the interpreter.
        """
        return self.__path

    @path.setter
    def path(self, new_path: str):
        """
        Sets the path to the interpreter.

        :param new_path: The new path to the interpreter.
        """
        self.__path = new_path

    @property
    def options(self) -> list[str]:
        """
        Gets the list of command-line options to pass to the interpreter

        :return: The list of command-line options to pass to the interpreter.
        """
        return self.__options

    @options.setter
    def options(self, new_options: list[str]):
        """
        Sets the command-line options to pass to the interpreter.

        :param new_options: The new list of command-line options to pass to the interpreter.
        """
        self.__options = new_options
