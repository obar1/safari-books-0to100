# pylint: disable=W0621,C0116,R0903,E0401,W0703,W1201,missing-function-docstring,E0401,C0114,W0511,W1203,C0200,C0103,W1203,W0613
from factories.sb_factory import SBFactory
from processors.help_processor import HelpProcessor, VERSION
from tests.moke.persist_fs import PersistFS as persist_fs
from tests.moke.process_fs import ProcessFS as process_fs

CURR_VERSION = "0.2"


def test_process(get_config_map, get_args_help_processor,):
    actual: HelpProcessor = SBFactory(get_config_map, persist_fs, process_fs).get_processor(
        get_args_help_processor
    )
    for p in actual:
        assert p.process()== f'{VERSION}"{CURR_VERSION}"'
