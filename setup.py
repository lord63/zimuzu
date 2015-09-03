#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

import zimuzu

try:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst')
except (IOError, ImportError):
    with open('README.md') as f:
        long_description = f.read()

setup(
    name='zimuzu',
    version=zimuzu.__version__,
    description='Do sign for ZIMUZU: http://www.zimuzu.tv',
    long_description=long_description,
    url='https://github.com/lord63/zimuzu',
    author='lord63',
    author_email='lord63.j@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Operating System :: POSIX',
        'Operating System :: POSIX :: Linux',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
    ],
    keywords='zimuzu sign',
    packages=['zimuzu'],
    install_requires=[
        'click>=4.0',
        'requests>=2.7.0',
    ],
    include_package_data=True,
    entry_points={
        'console_scripts':[
            'zimuzu=zimuzu.cli:cli']
    }
)
