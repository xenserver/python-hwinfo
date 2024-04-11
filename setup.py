#!/usr/bin/env python3

from setuptools import setup, find_packages

setup(
    name='python-hwinfo',
    author='Rob Dobson',
    author_email = 'rob@rdobson.co.uk',
    version = '0.1.7',
    description = 'Library for parsing hardware info on Linux OSes.',
    url = 'https://github.com/rdobson/python-hwinfo',
    packages=find_packages(),
    package_dir={'': '.'},  # Use the current directory as the package source directory
    entry_points = {
        'console_scripts': [
            'hwinfo = hwinfo.tools.inspector:main',
        ]
    },
    install_requires = [
        'prettytable',
    ],
    )
