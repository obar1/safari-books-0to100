# pylint: disable=W0621,C0116,R0903,E0401,W0703,W1201,missing-function-docstring,E0401,C0114,W0511,W1203,C0200,C0103,W1203
from pprint import pprint

import pytest

from configs.config import ConfigMap
from factories.sb_factory import SBFactory
from tests.moke.persist_fs import PersistFS as persist_fs
from tests.moke.process_fs import ProcessFS as process_fs


@pytest.fixture
def get_config_map(get_map_yaml_path):
    return ConfigMap(get_map_yaml_path, persist_fs)

def test_get_processor(get_config_map, get_args_unsupported_processor):
    SBFactory(get_config_map, persist_fs, process_fs)