# pylint: disable=W0621,C0116,R0903,E0401,W0703,W1201,missing-function-docstring,E0401,C0114,W0511,W1203,C0200,C0103,W1203
import logging

from models.meta_book import MetaBook
from tests.moke.persist_fs import PersistFS as persist_fs
from tests.moke.process_fs import ProcessFS as process_fs


def test_init(get_config_map, http_url):
    actual = MetaBook(get_config_map, persist_fs, process_fs, http_url)
    assert actual.isbn == '9780135956977'
    assert actual.contents_path == './books/9780135956977'
    assert actual.dir_pdf == './books/9780135956977/9780135956977.pdf'
    assert actual.dir_epub == './books/9780135956977/9780135956977.epub'
    assert actual.dir_img == './books/9780135956977/9780135956977.png'


def test_write(get_config_map, http_url):
    actual = MetaBook(get_config_map, persist_fs, process_fs, http_url)
    logging.info(actual)


def test_build_from_dir(get_config_map):
    assert MetaBook.build_from_dir(get_config_map, persist_fs, process_fs,
                                   './books/9780135956977').isbn == '9780135956977'


def test_is_valid_ebook_path():
    dirs = ['0123456789', 'books', 'ABC']
    actual = [dir_ for dir_ in dirs if MetaBook.is_valid_ebook_path(dir_)]
    assert actual == ['0123456789']



def test_get_epub_path(get_config_map, http_url, http_url_isbn):
    actual = MetaBook(get_config_map, persist_fs, process_fs, http_url).get_epub_path()
    from pprint import pprint
    pprint(actual)
    assert str(actual).endswith(http_url_isbn + MetaBook.epub_suffix)
