"""CreateMetaBookProcessor:
create a new meta_book on fs from http address
"""
# pylint: disable=W0621,C0116,R0903,E0401,W0703,W1201,missing-function-docstring,E0401,C0114,W0511,W1203,C0200,C0103,W1203

from configs.config import ConfigMap
from models.meta_book import MetaBook


class CreateMetaBookProcessor:
    """CreateMetaBookProcessor."""

    def __init__(self, config_map: ConfigMap, persist_fs, http_url: str,process_fs):
        """init"""
        self.http_url = http_url
        self.persist_fs = persist_fs
        self.process_fs=process_fs
        self.config_map = config_map

    def process(self):
        """Process the meta_book"""
        meta_book: MetaBook = MetaBook(self.config_map, self.persist_fs, self.process_fs, self.http_url)
        meta_book.write()

