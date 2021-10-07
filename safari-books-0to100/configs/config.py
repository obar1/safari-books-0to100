"""Config:"""


# pylint: disable=W0621,C0116,R0903,E0401,W0703,W1201,missing-function-docstring,E0401,C0114,W0511,W1203,C0200,C0103,W1203
from exceptions.errors import NotRelativeBooksPath, UnsupportedConfigMap
from repository.persist_fs import PREFIX_RELATIVE_FOLDER

SAFARI_BOOKS = "safari-books"
CONFIG_FILE = "CONFIG_FILE"


class Config:
    """Config"""

    def __init__(self, map_yaml_path, persist_fs):
        """persist_fs_load_file: f()  to _load file as dict[]"""
        self.map_yaml_path = map_yaml_path
        self.persist_fs = persist_fs

    def __repr__(self):
        """repr"""
        return f"map_yaml_path:{self.map_yaml_path}"

    @property
    def _load(self):
        """_load yaml file"""
        return self.persist_fs.load_file(self.map_yaml_path)

    @property
    def get_type(self):
        """Returns config type."""
        return self._load["type"]


class ConfigMap(Config):
    """ConfigMap specific to actual impl"""

    def __init__(self, map_yaml_path, persist_fs):
        super().__init__(map_yaml_path, persist_fs)
        self.is_valid_type(self.get_type, SAFARI_BOOKS)
        self.is_valid_books_path(self.get_books_path)

    @property
    def get_books_path(self):
        """T Returns path."""
        return str(self._load["configs"]["books_path"]).rstrip(PREFIX_RELATIVE_FOLDER)

    @property
    def get_download_engine_path(self):
        """T Returns path."""
        return self._load["configs"]["download_engine_path"]

    @property
    def get_download_engine_books_path(self):
        """T Returns path."""
        return self._load["configs"]["download_engine_books_path"]

    @property
    def get_oreilly_username(self):
        """T Returns path."""
        return self._load["configs"]["oreilly_username"]

    @property
    def get_oreilly_userpassword(self):
        """T Returns path."""
        return self._load["configs"]["oreilly_userpassword"]

    def is_valid_books_path(self, books_path):
        if self.persist_fs.is_relative_path(books_path):
            return books_path
        raise NotRelativeBooksPath(
            f"the books_path {books_path} should start with {PREFIX_RELATIVE_FOLDER}"
        )

    @staticmethod
    def is_valid_type(type_, safari_books_type):
        if type_ is None or type_ != safari_books_type:
            raise UnsupportedConfigMap(f"the {type_} should be {SAFARI_BOOKS}")
