"""
PersistFS:
fs handling ops
"""
# pylint: disable=W0621,C0116,R0903,E0401,W0703,W1201,missing-function-docstring,E0401,C0114,W0511,W1203,C0200,C0103,W1203

import logging
from typing import List

from repository.persist_fs import PersistFS as _PersistFS


class PersistFS(_PersistFS):
    """persist_fs."""

    @staticmethod
    def list_dirs(path) -> List[str]:
        logging.debug(f"list_dirs {path}")
        if path == "./books":
            return ["ABC (9781948580793)", "CDF (9780135956977)"]
        if path == "./safaribooks.git/Books":
            return [
                "The Concise Coaching Handbook (9781948580793)",
                "The Pragmatic Programmer (9780135956977)",
            ]
        raise ValueError(f"{path} not supported")



    @staticmethod
    def write_file(filename, txt):
        logging.debug(f"write_file {filename} {txt}")

    @classmethod
    def create_file(cls, filename):
        logging.debug(f"create_file {filename}")
        return cls.write_file(filename, [])

    @staticmethod
    def make_dirs(path):
        logging.debug(f"make_dirs {path}")

    @staticmethod
    def read_file(filename) -> List[str]:
        logging.debug(f"read {filename}")
        if filename.endswith("readme.md"):
            return """
        # https:§§cloud.google.com§docs\n
                \n
        > https://cloud.google.com/docs\n

https://cloud.google.com/products\n
                """.split(
                "\n"
            )
        raise ValueError(f"{filename} not supported")

    @staticmethod
    def delete_folder(path):
        logging.debug(f"delete_folder {path}")

    @staticmethod
    def copy_file_to(file_path, path_to):
        logging.debug(f"copy_file_to {file_path} {path_to}")
