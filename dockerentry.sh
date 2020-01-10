#!/usr/bin/env sh
/workdir/fetch-docs.py
/usr/local/bin/mkdocs serve -a "0.0.0.0:8000"
