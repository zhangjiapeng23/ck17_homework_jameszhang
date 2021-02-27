#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @author: James Zhang
# @data  : 2021/2/7

import setuptools

setuptools.setup(
    name="pytest-encode-jameszhang", # Replace with your own username
    version="0.0.1",
    author="james zhang",
    author_email="18373230129@163.com",
    description="A small example package",
    long_description="test test",
    long_description_content_type="text/markdown",
    url="",
    packages=['pytest_encode'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        'pytest'
    ],
    entry_points={
        'pytest11': [
            'pytest-encode = pytest_encode',
        ]
    },

)