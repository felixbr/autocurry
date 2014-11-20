#!/usr/bin/env python

from distutils.core import setup

version = open('VERSION').read().strip()

setup(
    name="Autocurry",
    packages=['autocurry'],
    version=version,
    description='Automatic currying using a decorator',
    long_description=open('README.md').read(),
    author='Felix Bruckmeier',
    author_email='felix.m.bruckmeier@gmail.com',
    url='https://github.com/felixbr/autocurry',
    download_url='https://github.com/felixbr/autocurry/tarball/%s' % version,
    keywords=['functional', 'currying'],
    license='BSD',
)