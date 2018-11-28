#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import os
import glob

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("pre_gen_project")

IGNORE_FILES = [".*.swp"]


def remove_ignore_files():
    for file_regex in IGNORE_FILES:
        logger.info("Removing files %s", file_regex)
        for file_name in glob.glob('../**/{}'.format(file_regex), recursive=True):
            os.remove(file_name)


if __name__ == "__main__":
    remove_ignore_files()
