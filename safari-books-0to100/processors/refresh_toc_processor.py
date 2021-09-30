"""RefreshMapProcessor:
refresh meta_books in map
"""
# pylint: disable=W0621,C0116,R0903,E0401,W0703,W1201,missing-function-docstring,E0401,C0114,W0511,W1203,C0200,C0103,W1203

from configs.config import ConfigMap
from models.meta_book import MetaBook
from models.toc import Toc


class RefreshTocProcessor:
    """RefreshMapProcessor"""

    def __init__(self, config_map: ConfigMap, persist_fs, process_fs):
        """init"""
        self.config_map = config_map
        self.persist_fs = persist_fs
        self.process_fs = process_fs

    def process(self):
        """Scan the repo and for each meta_book add it to  the map, save the toc file."""
        dirs = self.persist_fs.list_dirs(self.config_map.get_books_path)
        valid_dirs = [dir_ for dir_ in dirs if MetaBook.is_valid_ebook_path(dir_)]
        meta_books = Toc.build_from_dirs(
            self.config_map, self.persist_fs, self.process_fs, valid_dirs
        )
        toc: Toc = Toc(self.config_map, self.persist_fs, meta_books)
        toc.write()
