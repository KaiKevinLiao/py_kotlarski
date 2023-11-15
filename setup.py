# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='pykotlarski',
    version='0.1.0',
    description='A python implementation of Korlarski deconvolution',
    long_description=readme,
    author='Kai Liao',
    author_email='kl84@rice.edu',
    url='https://github.com/KaiKevinLiao/py_kotlarski',
    license=license,
    packages=find_packages()
)