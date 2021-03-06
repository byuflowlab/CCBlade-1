#!/usr/bin/env python
# encoding: utf-8

from setuptools import setup
from numpy.distutils.core import setup, Extension



setup(
    name='CCBlade',
    version='1.2.1',
    description='Blade element momentum aerodynamics for wind turbines',
    author='S. Andrew Ning',
    author_email='andrew.ning@nrel.gov',
    package_dir={'': 'src'},
    py_modules=['ccblade'],
    install_requires=['airfoilprep.py>=0.2'],  # , 'zope.interface'],
    # test_suite='test.test_ccblade.py',
    license='Apache License, Version 2.0',
    ext_modules=[Extension('_bem', ['src/bem.f90'], extra_compile_args=['-O2'])],
    dependency_links=['https://github.com/BYUFLOWLab/AirfoilPreppy/tarball/master#egg=airfoilprep.py-0.2'],
    zip_safe=False
)
