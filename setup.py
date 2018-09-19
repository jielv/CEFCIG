#!/usr/bin/env python

"""Description
Setup script for CEFCIG -- Computational Epigenetic Framework for Cell Identity Gene Discovery
@author:  Bo Xia
@contact: bxia@houstonmethodist.org
"""

import sys
from setuptools import setup, find_packages

# Use build_ext from Cython if found
command_classes = {}

try:
    from numpy import get_include as numpy_get_include

    numpy_include_dir = [numpy_get_include()]
except:
    numpy_include_dir = []
    sys.stderr.write("CRITICAL:Numpy must be installed!\n")
    sys.exit(1)


def main():
    if float(sys.version[:3]) < 2.7 or float(sys.version[:3]) >= 2.8:
        sys.stderr.write("CRITICAL: Python version must be 2.7!\n")
        sys.exit(1)

    setup(name="CEFCIG",
          version="1.0.1",
          description="Computational Epigenetic Framework for Cell Identity Gene Discovery",
          author='Bo Xia',
          author_email='bxia@houstonmethodist.org',
          include_package_data=True,
          packages=find_packages(),  # include all packages under src
          package_dir={'': 'src'},  # tell distutils packages are under src
          package_data={
              'data': ['*.pkl'],
          },
          license='MIT',
          scripts=['bin/CEFCIG',
                   ],
          install_requires=[
              'numpy>=1.13',
              'scipy',
              'pandas',
              'rpy2',
              'matplotlib',
              'pickle',
              'sklearn',
              'traceback',
          ],
          )


if __name__ == '__main__':
    main()