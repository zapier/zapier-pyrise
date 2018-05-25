#!/usr/bin/env python
#from distutils.core import setup
from setuptools import setup


setup(name="pyrise",
      version='0.5.3.zapier',
      description="Python wrapper for 37Signals Highrise",
      long_description="A work in progress, but one that will be awesome when finished. Pyrise gives you class objects that work a lot like Django models, making the whole experience of integrating with Highrise just a little more awesome and Pythonic.",
      license="MIT License",
      author="Jason Ford",
      author_email="jason@feedmagnet.com",
      url="http://github.com/feedmagnet/pyrise",
      py_modules=['pyrise'],
      install_requires = ['httplib2', 'requests', 'six'],
      keywords= "python 37signals highrise api wrapper feedmagnet",
      classifiers=[
         "Development Status :: 5 - Production/Stable",
         "License :: OSI Approved :: MIT License",
         "Programming Language :: Python",
         "Programming Language :: Python :: 2.7",
         "Programming Language :: Python :: 3",
         "Programming Language :: Python :: 3.5",
         "Programming Language :: Python :: 3.6",
      ],
)
