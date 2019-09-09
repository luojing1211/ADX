#!/usr/bin/python


from distutils.core import setup
import os

setup(
    name='adx',
    version='0.1',
    author='ADX Team',
    packages=['adx', 'adx.adx_table', 'adx.parser'],
    description='Astronomical Data Indexing Package',
    long_description=open('README.md').read(),
)
