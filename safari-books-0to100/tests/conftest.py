"""Conftest module."""
# pylint: disable=W0621,C0116,R0903,E0401,W0703,W1201,missing-function-docstring,E0401,C0114,W0511,W1203,C0200,C0103,W1203,W0613

import logging
import os
from unittest import mock

import pytest

from configs.config import ConfigMap
from factories.factory_provider import CONFIG_FILE
from tests.moke.persist_fs import PersistFS as persist_fs


@pytest.fixture(scope="session", autouse=True)
def callattr_ahead_of_alltests():
    logging.basicConfig(format="%(levelname)s:%(message)s", level=logging.INFO)
    yield


@pytest.fixture
def wip():
    logging.info("~" * 88)


@pytest.fixture
def http_url():
    yield "https://learning.oreilly.com/library/view/the-pragmatic-programmer/9780135956977/"


@pytest.fixture
def http_url_isbn():
    yield "9780135956977"


@pytest.fixture
def http_url_2():
    yield "https://www.oreilly.com/library/view/data-pipelines-pocket/9781492087823/"


@pytest.fixture
def dir_name():
    return "https:§§cloud.google.com§docs"

@pytest.fixture
def get_test_path():
    os_path_dirname = os.path.dirname(os.path.abspath(__file__))
    yield os_path_dirname


@pytest.fixture
def get_resource_path(get_test_path):
    yield get_test_path + "/resources"


@pytest.fixture
def get_repo_path(get_resource_path):
    yield get_resource_path + "/books"


@pytest.fixture
def get_map_yaml_path(get_resource_path):
    yield get_resource_path + "/map.yaml"
@pytest.fixture
def get_unsupported_map_yaml_path(get_resource_path):
    yield get_resource_path + "/unsupported_map.yaml"
@pytest.fixture
def get_full_path_map_yaml_path(get_resource_path):
    yield get_resource_path + "/full_path_map.yaml"

@pytest.fixture
def mock_map_yaml_env_vars(get_map_yaml_path):
    with mock.patch.dict(os.environ, {CONFIG_FILE: get_map_yaml_path}):
        yield
@pytest.fixture
def mock_unsupported_map_yaml_env_vars(get_unsupported_map_yaml_path):
    with mock.patch.dict(os.environ, {CONFIG_FILE: get_unsupported_map_yaml_path}):
        yield
@pytest.fixture
def mock_get_full_path_map_yaml_env_vars(get_full_path_map_yaml_path):
    with mock.patch.dict(os.environ, {CONFIG_FILE: get_full_path_map_yaml_path}):
        yield


@pytest.fixture
def get_args_create_meta_book_processor():
    return ["runme.sh", "create_meta_book"]
@pytest.fixture
def get_args_refresh_toc_processor():
    return ["runme.sh", "refresh_toc"]
@pytest.fixture
def get_args_help_processor():
    return ["runme.sh", "help"]
@pytest.fixture
def get_args_unsupported_processor():
    return ["runme.sh", "something"]
