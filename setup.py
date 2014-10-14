#!/usr/bin/env python
# -*- coding: utf-8 -*-

from boiseopensourcedemo import __version__
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

requirements = [
    # TODO: put package requirements here
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='boiseopensourcedemo',
    version=__version__,
    description='Boise Open Source Demo',
    long_description=readme + '\n\n' + history,
    author='Jeremy Robin',
    author_email='jeremy@talentpair.com',
    url='https://github.com/robustican/boiseopensourcedemo',
    packages=[
        'boiseopensourcedemo',
    ],
    package_dir={'boiseopensourcedemo':
                 'boiseopensourcedemo'},
    include_package_data=True,
    install_requires=requirements,
    license="BSD",
    zip_safe=False,
    keywords='boiseopensourcedemo',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ],
    test_suite='tests',
    tests_require=test_requirements
)