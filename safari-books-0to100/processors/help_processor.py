"""RefreshMapProcessor:
refresh meta_book in toc
"""
# pylint: disable=W0621,C0116,R0903,E0401,W0703,W1201,missing-function-docstring,E0401,C0114,W0511,W1203,C0200,C0103,W1203
import logging

VERSION = "__version__ = "


class HelpProcessor:
    """HelpProcessor"""

    def __init__(self, supported_processor, persist_fs):
        """init"""
        self.supported_processor = supported_processor
        self.persist_fs = persist_fs


    def get_version(self ,change_log_relative_path):
        """read file and return the version"""
        txt = self.persist_fs.read_file(change_log_relative_path)
        version = max(sorted(filter(lambda f: VERSION in f, txt)))
        logging.debug(f"v. {version}")
        return version.strip()

    def process(self):
        """Get version."""
        logging.debug(self.supported_processor)
        return self.get_version(
            self.persist_fs.dir_name(__file__) + "/../../changelog.md"
        )
