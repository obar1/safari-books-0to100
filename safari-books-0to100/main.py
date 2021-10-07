"""MAIN:
main
"""
# pylint: disable=W0621,C0116,R0903,E0401,W0703,W1201,missing-function-docstring,E0401,C0114,W0511,W1203,C0200,C0103,W1203

import logging
import sys
from typing import List

from exceptions.errors import UnsupportedOptionError
from factories.factory_provider import FactoryProvider
from factories.sb_factory import SBFactory
from repository.persist_fs import PersistFS as persist_fs
from repository.process_fs import ProcessFS as process_fs


def run_main(argv: List[str]):
    try:
        factory: SBFactory = FactoryProvider(persist_fs, process_fs).provide()
        for p in factory.get_processor(argv):
            p.process()
    except UnsupportedOptionError:
        logging.critical(f"check the help / params {sys.argv} ")
    except ModuleNotFoundError:
        logging.critical("??? have you installed all the dep")
    except Exception as e:
        logging.critical(f"check the help / params {sys.argv}  ... {e}")


if __name__ == "__main__":
    logging.basicConfig(format="%(levelname)s:%(message)s", level=logging.DEBUG)
    run_main(sys.argv)
