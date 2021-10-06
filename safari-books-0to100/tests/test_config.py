# pylint: disable=W0613,W0621,C0116,R0903,E0401,W0703,W1201,missing-function-docstring,E0401,C0114,W0511,W1203,C0200,C0103,W1203

import pytest

from configs.config import ConfigMap
from factories.factory_provider import FactoryProvider
from tests.moke.persist_fs import PersistFS as persist_fs
from tests.moke.process_fs import ProcessFS as process_fs


@pytest.fixture
def get_factory_provider(mock_map_yaml_env_vars):
    return FactoryProvider(persist_fs, process_fs)


def test_provide__pass(get_factory_provider):
    actual: ConfigMap = get_factory_provider.provide().config_map
    assert actual.get_books_path == "./repo"
    assert actual.get_download_engine_path == "./safaribooks.git/safaribooks.py"
    assert actual.get_download_engine_books_path == "./safaribooks.git/Books"
    assert actual.get_oreilly_username == "username"
    assert actual.get_oreilly_userpassword == "userpassword"
