"""ProcessFS:
deal with Process
mocked in Test
"""
# pylint: disable=W0621,C0116,R0903,E0401,W0703,W1201,missing-function-docstring,E0401,C0114,W0511,W1203,C0200,C0103,W1203
import logging
import os
import re
from typing import List

import yaml


from repository.process_fs import ProcessFS as _ProcessFS


class ProcessFS(_ProcessFS):
    """Process_fs."""

    @classmethod
    def get_img(cls, dir_img,  http_url_img):
        logging.info(f"get_img  {dir_img} {http_url_img}")

    @classmethod
    def get_epub(cls, config_map, dir_epub, isbn):
        logging.info(f"get_epub  {dir_epub} {isbn}")
