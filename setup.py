#!/usr/bin/env python

import setuptools
from io import open

version = open('VERSION', 'r', encoding='utf-8').read().strip()
long_description = open('README.md', 'r', encoding='utf-8').read()

setuptools.setup(
    name = "Autocurry",
    version = version,
    description = 'Automatic currying using a decorator',
    long_description = long_description,
    long_description_content_type = "text/markdown",
    author = 'Felix Bruckmeier',
    author_email = 'felix.m.bruckmeier@gmail.com',
    url = 'https://github.com/felixbr/autocurry',
    download_url = 'https://github.com/felixbr/autocurry/tarball/%s' % version,
    packages = setuptools.find_packages(),
    keywords = ['functional', 'currying'],
    license = 'BSD',
    install_requires = []
)