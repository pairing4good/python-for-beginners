#!/usr/bin/env sh

pip3 install pytest
python -m pytest $1-assignment/tests/test_worksheet.py
