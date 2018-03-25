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

install_requires = [
    'elasticsearch==6.1.1'
]

develop_requires = [
    'nose',
    'flake8'
]

docs_requires = [
    'sphinx',
    'sphinx_rtd_theme'
]

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
        "Development Status :: 3 - Alpha",
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

    entry_points = {
        'console_scripts': [
            'elastic-cloud = elastic_cloud.cli:main']
    },

    extras_require={
        'develop': develop_requires,
        'docs': docs_requires
    },

    keywords='elastic-cloud elastic'
)