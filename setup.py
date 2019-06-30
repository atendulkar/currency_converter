#!/usr/bin/python3
from __future__ import with_statement

from setuptools import setup, find_packages


with open('README.md') as fl:
    LONG_DESCRIPTION = fl.read()

with open('LICENSE.txt') as fl:
    LICENSE = fl.read()

setup(
    name='currency_converter',
    version='1.0.0',
    author='Ashwin Tendulkar',
    author_email='ashwin.tendulkar@gmail.com',
    description='Currency converter for finding exchange rates.',
    url='https://github.com/atendulkar/currency_converter.git',
    long_description=LONG_DESCRIPTION,
    license=LICENSE,
    packages=find_packages(),
    install_requires=[
              'requests',
          ],
    classifiers=[
                 "Programming Language :: Python :: 3.7",
                 "Operating System :: OS Independent"
                ]
)
