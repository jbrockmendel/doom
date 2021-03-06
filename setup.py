#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
from setuptools import setup, find_packages

import versioneer
cmdclass = versioneer.get_cmdclass()


# Note this will fail if an appropriate MANIFEST.in file is not present.
with open('requirements.txt') as requirements_f:
    REQUIREMENTS = requirements_f.readlines()

REQUIREMENTS = [x for x in REQUIREMENTS if not x.startswith('#')]

py2only = [x.split(';')[0] for x in REQUIREMENTS
           if re.search('python_version.*2', x)]
REQUIREMENTS = [x for x in REQUIREMENTS
                if not re.search('python_version.*2', x)]


with open('README.md', 'rb') as fd:
    LONG_DESCRIPTION = fd.read().decode('utf-8')


setup(name='doom',
      version=versioneer.get_version(),
      packages=find_packages(include=['doom', 'doom.*']),
      description='',
      long_description=LONG_DESCRIPTION,
      url='https://github.com/jbrockmendel/doom',
      license='MIT',
      cmdclass=cmdclass,

      author='Brock Mendel',
      author_email='jbrockmendel@gmail.com',

      py_modules=['compat', 'fslib', 'lning', 'utils', 'sysinfo'],
      install_requires=REQUIREMENTS,
      extras_require={':python_version == "2.7"': py2only},

      entry_points={
          'console_scripts': ['get_local_ip=doom.sysinfo.get_local_ip:script']
      },

      test_suite="tests",
      keywords=[],

      classifiers=[])
