"""Unit tests."""
# pylint: disable=W0621,C0116,R0903,E0401,W0703,W1201,missing-function-docstring,E0401,C0114,W0511,W1203,C0200,C0103,W1203
import pytest
from repository.process_fs import ProcessFS as process_fs
from main import run_main

def skip_this():
    return False

@pytest.mark.skipif(skip_this(), reason="skipped")
def test_run_main(mock_secret_yaml_env_vars,
                  get_args_create_meta_book_processor,
                  get_args_help_processor, http_url, http_url_2, get_args_refresh_toc_processor
                  ):
    """logical seq"""
    process_fs.DEBUG_Y_N=False
    run_main(get_args_create_meta_book_processor + [http_url])
    run_main(get_args_create_meta_book_processor + [http_url_2])
    run_main(get_args_refresh_toc_processor)
    run_main(get_args_help_processor)
