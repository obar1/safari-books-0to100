"""ProcessFS:
deal with Process
mocked in Test
"""
# pylint: disable=W0621,C0116,R0903,E0401,W0703,W1201,missing-function-docstring,E0401,C0114,W0511,W1203,C0200,C0103,W1203
import logging
import shlex
import subprocess
from subprocess import PIPE, run

from configs.config import ConfigMap


class ProcessFS:
    """Process_fs."""

    DEBUG_Y_N = True

    @classmethod
    def debug_y_n(cls):
        DEBUG_ME = 'echo'
        DEBUG_ME_NOT = ''
        return DEBUG_ME if cls.DEBUG_Y_N else DEBUG_ME_NOT

    @classmethod
    def get_img(cls, dir_img, http_url_img):
        logging.info(f"get_img  {dir_img} {http_url_img}")
        cmd = f"{cls.debug_y_n()} curl -o  {dir_img}  {http_url_img}"
        subprocess.call(shlex.split(cmd))

    @classmethod
    def get_epub(cls, config_map: ConfigMap, dir_epub, isbn):
        logging.info(f"get_epub {dir_epub} {isbn}")
        cls.download_epub(config_map, isbn)

    @classmethod
    def download_epub(cls, config_map, isbn):
        logging.info(f"download_epub {isbn}")
        cmd = f"{cls.debug_y_n()} python {config_map.get_download_engine_path} --cred {config_map.get_oreilly_username}:{config_map.get_oreilly_userpassword} {isbn}"
        result = run(shlex.split(cmd), stdout=PIPE, stderr=PIPE, universal_newlines=True)
        logging.info(result.stdout)
        logging.info(result.stderr)
        assert result.returncode == 0
