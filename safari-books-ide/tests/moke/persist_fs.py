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

    relative_path_starts_with = "./"
    HTTPS_ = ":§§"

    @classmethod
    def list_dirs(cls, path) -> List[str]:
        logging.info(f"list_dirs {path}")
        if path=="./safaribooks.git/Books":
            return ['The Concise Coaching Handbook (9781948580793)', 'The Pragmatic Programmer (9780135956977)']
        raise ValueError(f"{path} not supported")

    @classmethod
    def get_dir_name(cls, filename):
        logging.info(f"get_dir_name {filename}")
        return None

    @classmethod
    def load_file(cls, config_file):
        logging.info(f"load_file {config_file}")
        if config_file.endswith("unsupported_map.yaml"):
            return {"type": "not_a_map", "lib": {"path": "./repo"}}
        if config_file.endswith("map.yaml"):
            return {
                "type": "safari-books",
                "configs": { "books_path": "./books", "download_engine_path": './safaribooks.git/safaribooks.py',"download_engine_books_path": "./safaribooks.git/Books","oreilly_username":'username','oreilly_userpassword':'userpassword'  },
            }
        raise ValueError(f"{config_file} not supported")

    @classmethod
    def write_file(cls, filename, txt):
        logging.info(f"write_file {filename} {txt}")
        return None

    @classmethod
    def create_file(cls, filename):
        logging.info(f"create_file {filename}")
        return cls.write_file(filename,[])

    @classmethod
    def make_dirs(cls, path):
        logging.info(f"make_dirs {path}")
        return None

    @classmethod
    def read_file(cls, filename) -> List[str]:
        logging.info(f"read {filename}")
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

    @classmethod
    def delete_folder(cls, path):
        logging.info(f"delete_folder {path}")
        return None


    @classmethod
    def copy_file_to(cls, file_path, path_to):
        logging.info(f"copy_file_to {file_path} {path_to}")
        return None