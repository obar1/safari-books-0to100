"""PersistFS:
deal with FS
mocked in Test
"""
# pylint: disable=W0621,C0116,R0903,E0401,W0703,W1201,missing-function-docstring,E0401,C0114,W0511,W1203,C0200,C0103,W1203
import os
from pathlib import Path
from shutil import copyfile
from typing import List
import yaml


class PersistFS:
    """persist_fs."""

    @staticmethod
    def list_dirs(path) -> List[str]:
        return os.listdir(path) if Path(path).is_dir() else []

    @staticmethod
    def dir_name(filename):
        return os.path.dirname(os.path.abspath(filename))

    @staticmethod
    def load_file(config_file):
        with open(config_file, mode="r", encoding="UTF-8") as stream:
            return yaml.safe_load(stream)

    @staticmethod
    def write_file(filename, txt):
        with open(filename, mode="w", encoding="UTF-8") as outfile:
            return outfile.write("".join(txt))

    @classmethod
    def create_file(cls, filename):
        return cls.write_file(filename, [])

    @staticmethod
    def make_dirs(path):
        if os.path.isdir(path):
            return None
        return os.makedirs(path, 0o777, False)

    @staticmethod
    def read_file(filename) -> List[str]:
        with open(filename, mode="r", encoding="UTF-8") as file_:
            lines = file_.readlines()
            return lines

    @staticmethod
    def delete_folder(path):
        return os.rmdir(path)

    @staticmethod
    def copy_file_to(file_path, path_to):
        return copyfile(file_path, path_to)

    @staticmethod
    def abs_path(path):
        return os.path.abspath(path)

    @staticmethod
    def is_relative_path(path):
        if str(path).startswith("./"):
            return True
        return False

    @staticmethod
    def abs_path_join(path, relative_path):
        return os.path.join(path, relative_path)
