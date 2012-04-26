#!/usr/bin/env python
# -*- coding: utf-8 -*-

from distutils.core import setup

VERSION = '0.3'
LONG_DESCRIPTION = open('README.rst').read()
INSTALL_REQUIRES = [
    'beautifulsoup4',
    ]

setup(
    name='rivercrab',
    version=VERSION,
    description='River Crab',
    long_description=LONG_DESCRIPTION,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Site Management',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
        ],
    author='Philip Xu',
    author_email='pyx@xrefactor.com',
    url='https://bitbucket.org/pyx/rivercrab',
    download_url='https://bitbucket.org/pyx/rivercrab/get/tip.tar.bz2',
    scripts=['rivercrab'],
    license='BSD-New',
    install_requires=INSTALL_REQUIRES,
    )
