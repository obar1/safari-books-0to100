"""Validator:
gen validator
"""


# pylint: disable=W0621,C0116,R0903,E0401,W0703,W1201,missing-function-docstring,E0401,C0114,W0511,W1203,C0200,C0103,W1203
from exceptions.errors import NotURLFormatError


class Validator:
    """Validator"""

    @classmethod
    def is_valid_http(cls, txt: str):
        """is_valid_http
        basic validation
        """
        if not txt.strip().startswith("https://"):
            raise NotURLFormatError(f"on {txt}")
        return True
