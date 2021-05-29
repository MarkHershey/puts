#!/usr/bin/env bash

check-manifest || exit 1

python setup.py sdist bdist_wheel || exit 1

# python -m twine upload dist/* || exit 1