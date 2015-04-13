#!/usr/bin/env python
""" This is a setup. """

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

VERSION = '0.2.1'

setup(
    name='nexmomessage',
    version=VERSION,
    description='A Python wrapper for the Nexmo API',
    author='Olivier Cortès',
    author_email='contact@oliviercortes.com',
    license='BSD',
    url='https://github.com/Karmak23/libpynexmo',
    keywords=['Nexmo', 'Python'],
    packages=['nexmomessage'],
    install_requires=[
        'phonenumbers',
    ],
)
