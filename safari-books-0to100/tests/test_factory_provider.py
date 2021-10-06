# pylint: disable=W0621,C0116,R0903,E0401,W0703,W1201,missing-function-docstring,E0401,C0114,W0511,W1203,C0200,C0103,W1203,W0613
import pytest

from factories.factory_provider import FactoryProvider
from factories.sb_factory import SBFactory
from tests.moke.persist_fs import PersistFS as persist_fs
from tests.moke.process_fs import ProcessFS as process_fs


@pytest.fixture
def get_factory_provider(mock_map_yaml_env_vars):
    return FactoryProvider(persist_fs, process_fs)


def test_provide__pass(get_factory_provider):
    actual = get_factory_provider.provide()
    assert isinstance(actual, SBFactory)


@pytest.fixture
def get_unsupported_factory_provider(mock_unsupported_map_yaml_env_vars):
    return FactoryProvider(persist_fs, process_fs)


def test_provide__unsupported(get_unsupported_factory_provider):
    with pytest.raises(NotImplementedError):
        get_unsupported_factory_provider.provide()
