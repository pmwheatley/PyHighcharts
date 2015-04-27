#!/usr/bin/env python

from distutils.core import setup

setup(name='PyHighcharts',
      version='1.0',
      description='A convenient wrapper for Highchart generation',
      author='fidyeates',
      author_email='fidyeates@unknown.com',
      url='https://github.com/fidyeates/PyHighcharts',
      packages=['highcharts'],
      package_data={'highcharts': ['templates/*.tmp']}
     )