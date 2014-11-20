#!/usr/bin/env python

from setuptools import setup
from io import open

version = open('VERSION', 'r', encoding='utf-8').read().strip()

setup(
    name = "Autocurry",
    packages = ['autocurry'],
    version = version,
    description = 'Automatic currying using a decorator',
    long_description = open('README.md', 'r', encoding='utf-8').read(),
    author = 'Felix Bruckmeier',
    author_email = 'felix.m.bruckmeier@gmail.com',
    url = 'https://github.com/felixbr/autocurry',
    download_url = 'https://github.com/felixbr/autocurry/tarball/%s' % version,
    keywords = ['functional', 'currying'],
    license = 'BSD',
    install_requires = []
)