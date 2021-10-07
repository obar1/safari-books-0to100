"""Some Exceptions"""


# pylint: disable=W0235,W0621,C0116,R0903,E0401,W0703,W1201,missing-function-docstring,E0401,C0114,W0511,W1203,C0200,C0103,W1203


class NotURLFormatError(Exception):
    """NotURLFormatError"""

    def __init__(self, message):
        # Call the base class constructor with the parameters it needs
        super().__init__(message)


class NotRelativeBooksPath(Exception):
    """NotRelativeBooksPath
    to enforce path like './somepath'
    """

    def __init__(self, message):
        # Call the base class constructor with the parameters it needs
        super().__init__(message)


class UnsupportedConfigMap(Exception):
    """UnsupportedConfigMap"""

    def __init__(self, message):
        # Call the base class constructor with the parameters it needs
        super().__init__(message)


class UnsupportedOptionError(Exception):
    """UnsupportedOptionError"""

    def __init__(self, message):
        # Call the base class constructor with the parameters it needs
        super().__init__(message)
