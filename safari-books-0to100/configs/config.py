"""Config:"""


# pylint: disable=W0621,C0116,R0903,E0401,W0703,W1201,missing-function-docstring,E0401,C0114,W0511,W1203,C0200,C0103,W1203


class Config:
    """Config"""

    def __init__(self, map_yaml_path, persist_fs):
        """persist_fs_load_file: f()  to load file as dict[]"""
        self.map_yaml_path = map_yaml_path
        self.persist_fs = persist_fs

    def __repr__(self):
        """repr"""
        return f"map_yaml_path:{self.map_yaml_path}"

    @property
    def load(self):
        """load yaml file"""
        return self.persist_fs.load_file(self.map_yaml_path)

    @property
    def get_type(self):
        """Returns config type."""
        return self.load["type"]


class ConfigMap(Config):
    """ConfigMap specific to  actual impl"""

    @property
    def get_books_path(self):
        """T Returns path."""
        tmp = self.load["configs"]["books_path"]
        return (
            tmp
            if self.persist_fs.is_relative_path(tmp)
            else self.persist_fs.abs_path(tmp)
        )

    @property
    def get_download_engine_path(self):
        """T Returns path."""
        return self.load["configs"]["download_engine_path"]

    @property
    def get_download_engine_books_path(self):
        """T Returns path."""
        return self.load["configs"]["download_engine_books_path"]

    @property
    def get_oreilly_username(self):
        """T Returns path."""
        return self.load["configs"]["oreilly_username"]

    @property
    def get_oreilly_userpassword(self):
        """T Returns path."""
        return self.load["configs"]["oreilly_userpassword"]
