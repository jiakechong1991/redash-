#!/usr/bin/env python
"""
CLI to manage redash.
"""

from redash.cli import manager

if __name__ == '__main__':
    # ﻿./manage.py database create_tables  使用的方式
    manager()
