# pylint: disable=W0613,W0621,C0116,R0903,E0401,W0703,W1201,missing-function-docstring,E0401,C0114,W0511,W1203,C0200,C0103,W1203

import pytest

from configs.config import ConfigMap, Config, SAFARI_BOOKS
from exceptions.errors import NotRelativeBooksPath, UnsupportedConfigMap
from tests.moke.persist_fs import PersistFS as persist_fs


def test_load(get_map_yaml_path):
    Config(get_map_yaml_path, persist_fs)


def test_get_type(get_map_yaml_path):
    actual = Config(get_map_yaml_path, persist_fs)
    assert actual.get_type == SAFARI_BOOKS


def test_load_config_map_pass(get_map_yaml_path):
    ConfigMap(get_map_yaml_path, persist_fs)


def test_load_config_map_fail_0(get_unsupported_map_yaml_path):
    with pytest.raises(UnsupportedConfigMap):
        ConfigMap(get_unsupported_map_yaml_path, persist_fs)


def test_load_config_map_fail_1(get_full_path_map_yaml_path):
    with pytest.raises(NotRelativeBooksPath):
        ConfigMap(get_full_path_map_yaml_path, persist_fs)
