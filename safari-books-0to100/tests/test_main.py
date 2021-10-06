"""Unit tests."""
# pylint: disable=R0913,W0613,W0613:,W0621,C0116,R0903,E0401,W0703,W1201,missing-function-docstring,E0401,C0114,W0511,W1203,C0200,C0103,W1203
import pytest

from main import run_main
from repository.process_fs import ProcessFS as process_fs


def skip_this():
    return False

process_fs.DEBUG_Y_N = True

@pytest.mark.skipif(skip_this(), reason="skipped")
def test_run_main(
        mock_map_yaml_env_vars,
    get_args_create_meta_book_processor,
    get_args_help_processor,
    http_url,
    http_url_2,
    get_args_refresh_toc_processor,
):
    """logical seq"""
    run_main(get_args_create_meta_book_processor + [http_url])
    run_main(get_args_create_meta_book_processor + [http_url_2])
    run_main(get_args_refresh_toc_processor)
    run_main(get_args_help_processor)


@pytest.mark.skipif(skip_this(), reason="skipped")
def test_run_main_full_path(
    mock_get_full_path_map_yaml_env_vars,
    get_args_create_meta_book_processor,
    get_args_help_processor,
    http_url,
    http_url_2,
    get_args_refresh_toc_processor,
):
    """logical seq"""
    process_fs.DEBUG_Y_N = True
    run_main(get_args_create_meta_book_processor + [http_url])
    run_main(get_args_create_meta_book_processor + [http_url_2])
    run_main(get_args_refresh_toc_processor)
    run_main(get_args_help_processor)

