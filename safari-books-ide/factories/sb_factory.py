"""SBFactory:
factory with implemented functionality
"""
# pylint: disable=W0621,C0116,R0903,E0401,W0703,W1201,missing-function-docstring,E0401,C0114,W0511,W1203,C0200,C0103,W1203
import logging

from configs.config import ConfigMap
from processors.create_meta_book_processor import CreateMetaBookProcessor
from processors.help_processor import HelpProcessor
from processors.refresh_toc_processor import RefreshTocProcessor


class SBFactory:
    """SBFactory class."""

    SUPPORTED_PROCESSOR = [
        "create_meta_book",
        "help",
    ]

    def __init__(self, config_map: ConfigMap, persist_fs, process_fs):
        """init"""
        self.config_map = config_map
        self.persist_fs = persist_fs
        self.process_fs = process_fs

    def get_processor(self, args):
        """get the processor"""
        logging.info(f"args {args}")
        cmd = args[1]
        if cmd == "create_meta_book":
            return self.create_meta_book_processor(args[2])
        if cmd == "refresh_toc":
            return self.refresh_toc_processor()
        if cmd == "help":
            return self.help_processor()
        logging.info(self.SUPPORTED_PROCESSOR)
        raise ValueError(f"{cmd} not supported")

    def create_meta_book_processor(self, http_url):
        """create_meta_book_processor"""
        return CreateMetaBookProcessor(self.config_map, self.persist_fs, http_url, self.process_fs)

    def help_processor(self):
        """version_processor"""
        return HelpProcessor(self.SUPPORTED_PROCESSOR)

    def refresh_toc_processor(self):
        """refresh_map_processor"""
        return RefreshTocProcessor(self.config_map, self.persist_fs, self.process_fs)
