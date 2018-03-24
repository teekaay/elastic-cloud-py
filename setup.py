# -*- coding: utf-8 -*-
from os.path import join, dirname
from setuptools import setup, find_packages
import sys

VERSION = (1, 1, 2)
__version__ = VERSION
__versionstr__ = '.'.join(map(str, VERSION))

f = open(join(dirname(__file__), 'README.rst'))
long_description = f.read().strip()
f.close()

install_requires = open(join(dirname(__file__), 'requirements.txt')).read().split('\n')
tests_require = open(join(dirname(__file__), 'requirements.dev.txt')).read().split('\n')

setup(
    name = 'elastic_cloud',
    description = "Python client for Elastic Cloud",
    license="Apache License, Version 2.0",
    url = "https://github.com/teekaay/elastic-cloud-py",
    long_description = long_description,
    version = __versionstr__,
    author = "Thomas Klinger",
    author_email = "thomas.klinger@protonmail.com",
    packages=find_packages(
        where='.',
        exclude=('test*', )
    ),
    classifiers = [
        "Development Status :: 1 - Experimental",
        "License :: OSI Approved :: Apache Software License",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
    ],
    install_requires=install_requires,

    extras_require={
        'develop': tests_require + ["sphinx", "sphinx_rtd_theme"]
    },
)