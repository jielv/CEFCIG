======================
INSTALL Guide For CEFCIG
======================

Please check the following instructions to complete your installation.

Prerequisites
=============

Python version must be equal to *2.7* to run CEFCIG.

Numpy
Scipy
Pandas
rpy2
matplotlib
sklearn
seaborn

Install from source
===================

CEFCIG uses Python's distutils tools for source installations. To
install a source distribution of CEFCIG, unpack the distribution tarball
and open up a command terminal. Go to the directory where you unpacked
CEFCIG, and simply run the install script::

 $ python setup.py install

By default, the script will install python library and executable
codes globally, which means you need to be root or administrator of
the machine so as to complete the installation. Please contact the
administrator of that machine if you want their help. If you need to
provide a nonstandard install prefix, or any other nonstandard
options, you can provide many command line options to the install
script. Use the –help option to see a brief list of available options::

 $ python setup.py --help

PATH
~~~~

Add CEFCIG_PATH to your PATH environment variable.

 $ export PATH=/CEFCIG_PATH/src:$PATH

--
Bo Xia <bxia@houstonmethodist.org>
Kaifu Chen <kchen2@houstonmethodist.org>

