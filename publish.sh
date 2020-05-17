#!/usr/bin/env sh

# see https://packaging.python.org/tutorials/packaging-projects

# install tools
python3 -m pip install --user --upgrade setuptools wheel
python3 -m pip install --user --upgrade twine

# create distribution
python3 setup.py sdist bdist_wheel

# validate distribution
python3 -m twine check dist/*

# upload to repository
python3 -m twine upload dist/*