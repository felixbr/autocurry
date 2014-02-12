#!/usr/bin/env python

from distutils.core import setup

setup(
    name="Autocurry",
    version=open('VERSION').read().strip(),
    author='Felix Bruckmeier',
    author_email='felix.m.bruckmeier@gmail.com',

    description='Automatic currying using a decorator',
    long_description=open('README.md').read(),
    url='https://github.com/felixbr/autocurry',
    license='BSD',

    packages=['autocurry']
)