#!/usr/bin/env sh

cd ..
pip3 install pytest
python -m pytest 001-assignment/tests/test_worksheet.py
