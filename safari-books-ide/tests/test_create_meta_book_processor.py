# pylint: disable=W0621,C0116,R0903,E0401,W0703,W1201,missing-function-docstring,E0401,C0114,W0511,W1203,C0200,C0103,W1203
from factories.sb_factory import SBFactory
from processors.create_meta_book_processor import CreateMetaBookProcessor
from tests.moke.persist_fs import PersistFS as persist_fs
from tests.moke.process_fs import ProcessFS as process_fs


def test_process(get_config_map, get_args_create_meta_book_processor, http_url):
    actual: CreateMetaBookProcessor = SBFactory(get_config_map, persist_fs, process_fs).get_processor(
        get_args_create_meta_book_processor + [http_url])
    actual.process()
