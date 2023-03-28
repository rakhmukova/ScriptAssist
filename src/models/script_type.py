from enum import Enum


class ScriptType(Enum):
    """
    An enum class that defines supported script types.
    """
    KOTLIN = 'Kotlin'
    SWIFT = 'Swift'
    UNDEFINED = 'Undefined'
