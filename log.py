#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    log.py
    ~~~~~~

    log module

    :author:    lightless <root@lightless.me>
    :homepage:  None
    :license:   GPL-3.0, see LICENSE for more details.
    :copyright: Copyright (c) 2017 lightless. All rights reserved
"""

import os
import logging
import logging.handlers

COLOR_MAP = {
    'DEBUG': 'cyan',
    'INFO': 'green',
    'WARNING': 'yellow',
    'ERROR': 'red',
    'CRITICAL': 'red,bg_white',
}


class ColoredFormatter(logging.Formatter):

    def __init__(self, fmt, datefmt):
        super(ColoredFormatter, self).__init__(fmt, datefmt)

    def parse_color(self, level_name):
        color_name = COLOR_MAP.get(level_name, "")
        print("color name: {}".format(color_name))
        if not color_name:
            return ""

        if color_name == "cyan":
            return "\033[36m"
        else:
            return "no found color!"

    def format(self, record):
        record.log_color = self.parse_color(record.levelname)
        message = super(ColoredFormatter, self).format(record) + "\033[0m"

        return message


def _get_logger(log_to_file=True, log_filename="default.log", log_level="DEBUG"):

    _logger = logging.getLogger(__name__)

    stdout_handler = logging.StreamHandler()
    stdout_handler.setFormatter(
        ColoredFormatter(
            fmt='%(log_color)s[%(asctime)s] [%(levelname)s] [%(threadName)s] [%(filename)s:%(lineno)d] %(message)s',
            datefmt="%Y-%m-%d %H:%M:%S",
        )
    )
    _logger.addHandler(stdout_handler)

    if log_to_file:
        _tmp_path = os.path.dirname(os.path.abspath(__file__))
        _tmp_path = os.path.join(_tmp_path, "../logs/{}".format(log_filename))
        file_handler = logging.handlers.TimedRotatingFileHandler(_tmp_path, when="midnight", backupCount=30)
        file_formatter = logging.Formatter(
            fmt='[%(asctime)s] [%(levelname)s] [%(threadName)s] [%(filename)s:%(lineno)d] %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S',
        )
        file_handler.setFormatter(file_formatter)
        _logger.addHandler(file_handler)

    _logger.setLevel(log_level)
    return _logger


logger = _get_logger(log_to_file=False)
