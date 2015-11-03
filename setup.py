#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pip.req import parse_requirements
from setuptools import setup, find_packages

version = '0.1'

long_description = (
    open('README.md').read())

install_reqs = parse_requirements('requirements.txt')
reqs = [str(ir.req) for ir in install_reqs]

setup(name='salt-lint',
      version=version,
      description="Lint your salt sls files",
      long_description=long_description,
      classifiers=[
          'Programming Language :: Python',
          'Programming Language :: Cython',
          'Programming Language :: Python :: 2.6',
          'Programming Language :: Python :: 2.7',
          'Environment :: Console',
          'Intended Audience :: Developers',
          'Intended Audience :: Information Technology',
          'Intended Audience :: System Administrators',
          'Operating System :: POSIX :: Linux',
          'Topic :: System :: Clustering',
          'Topic :: System :: Distributed Computing',
      ],
      keywords='salt lint',
      author='Johan van den Dorpe',
      author_email='',
      url='https://github.com/johanek/salt-lint.git',
      license='MIT',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=reqs,
      entry_points={
          'console_scripts': [
              'salt-lint = saltlint.saltlint:main']})
