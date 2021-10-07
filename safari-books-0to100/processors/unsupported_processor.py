"""RefreshMapProcessor:
refresh meta_book in toc
"""
# pylint: disable=W0621,C0116,R0903,E0401,W0703,W1201,missing-function-docstring,E0401,C0114,W0511,W1203,C0200,C0103,W1203

from exceptions.errors import UnsupportedOptionError


class UnsupportedProcessor:
    """UnsupportedProcessor"""

    def __init__(self, cmd):
        self.cmd = cmd

    def process(self):
        """Get version."""
        raise UnsupportedOptionError(f"UnsupportedProcessor {self.cmd}")
