"""Toc:
toc md with list of meta_book as found in fs
"""
# pylint: disable=C0301,W0621,C0116,R0903,E0401,W0703,W1201,missing-function-docstring,E0401,C0114,W0511,W1203,C0200,C0103,W1203
from typing import List

from configs.config import ConfigMap
from models.meta_book import MetaBook


class Toc:
    """Toc is a list of meta_books"""

    def __init__(
        self, config_map: ConfigMap, persist_fs, process_fs, meta_books: List[MetaBook]
    ):
        """init"""
        self.config_map = config_map
        self.readme_md = config_map.get_books_path + "/toc.md"
        self.persist_fs = persist_fs
        self.process_fs = process_fs
        self.meta_books = meta_books

    def __repr__(self):
        """repr"""
        return f"Toc {self.readme_md}, {self.meta_books}"

    @staticmethod
    def __repr_flatten(meta_books: List[MetaBook]) -> str:
        """transform as
        1. <0596007124> ![`img`](../books/0596007124/0596007124.png) :o: [`pdf`](../books/0596007124/0596007124.pdf) :o: [`epub`](../books/0596007124/0596007124.epub) :o: [`json`](../books/0596007124/0596007124.json)
        """
        flatten_meta_book = (
            lambda s: f"""| <span style="color:blue">**{s.isbn}**</span>	|  ![`img`]({s.dir_img}) 	| [`epub`]({s.dir_epub})  	|  [`pdf`]({s.dir_pdf}) 	| {s.read_json()}	|"""
        )
        flattened_meta_book = list(map(flatten_meta_book, meta_books))
        return "\n".join(flattened_meta_book)

    @classmethod
    def build_from_dirs(
        cls, config_map, persist_fs, process_fs, dirs: List[str]
    ) -> List[MetaBook]:
        """from a list of dirs created return the a MetaBook
        m> org http is lost
        """
        return [
            MetaBook.build_from_dir(config_map, persist_fs, process_fs, curr_dir)
            for curr_dir in dirs
            if curr_dir is not None
        ]

    def write(self):
        """write as

        # ./books/toc.md

        table
        """
        txt = []
        txt.append(
            f"""
# TOC
## `{len(self.meta_books)}` books
### {self.process_fs.get_now()}
|  ISBN 	|   	|   	|   	|  `json-contents` 	|
|---	|---	|---	|---	|---	|
{self.__repr_flatten(self.meta_books)}
        """
        )
        return self.persist_fs.write_file(self.readme_md, txt)
