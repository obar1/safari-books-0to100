# pylint: disable=W0621,C0116,R0903,E0401,W0703,W1201,missing-function-docstring,E0401,C0114,W0511,W1203,C0200,C0103,W1203
import logging

from configs.config import ConfigMap
from models.meta_book import MetaBook
from tests.moke.persist_fs import PersistFS as persist_fs
from tests.moke.process_fs import ProcessFS as process_fs


def test_init(get_map_yaml_path, http_url):
    actual = MetaBook(ConfigMap(get_map_yaml_path, persist_fs), persist_fs, process_fs, http_url)
    assert str(actual.isbn).endswith("9780135956977")
    assert str(actual.contents_path).endswith("/repo/9780135956977")
    assert str(actual.dir_pdf).endswith("/repo/9780135956977/9780135956977.pdf")
    assert str(actual.dir_epub).endswith("/repo/9780135956977/9780135956977.epub")
    assert str(actual.dir_img).endswith("/repo/9780135956977/9780135956977.png")


def test_write(get_map_yaml_path, http_url):
    actual = MetaBook(ConfigMap(get_map_yaml_path, persist_fs), persist_fs, process_fs, http_url)
    logging.info(actual)


def test_build_from_dir(get_map_yaml_path):
    assert (
        MetaBook.build_from_dir(
            ConfigMap(get_map_yaml_path, persist_fs), persist_fs, process_fs, "./books/9780135956977"
        ).isbn
        == "9780135956977"
    )


def test_is_valid_ebook_path():
    dirs = ["0123456789", "books", "ABC"]
    actual = [dir_ for dir_ in dirs if MetaBook.is_valid_ebook_path(dir_)]
    assert actual == ["0123456789"]


def test_get_epub_path(get_map_yaml_path, http_url, http_url_isbn):
    actual = MetaBook(ConfigMap(get_map_yaml_path, persist_fs), persist_fs, process_fs, http_url).get_epub_path()
    assert str(actual).endswith(http_url_isbn + MetaBook.epub_suffix)
