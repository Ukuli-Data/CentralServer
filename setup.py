#!/usr/bin/env python 
# -*- coding: UTF-8 -*- 
import os 
from setuptools import setup 
 
setup( 
    name = 'my_app', 
    version='1.0', 
    license='GNU General Public License v3', 
    author='Tomi Toivio', 
    author_email='tomi.toivio@ukuli.fi', 
    description='Survival tool for data ocean', 
    packages=['my_app'], 
    platforms='any', 
    install_requires=[ 
        'flask', 
    ], 
    classifiers=[ 
        'Development Status :: 4 - Beta', 
        'Environment :: Web Environment', 
        'Intended Audience :: Developers', 
        'License :: OSI Approved :: GNU General Public License v3', 
        'Operating System :: OS Independent', 
        'Programming Language :: Python', 
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content', 
        'Topic :: Software Development :: Libraries :: Python Modules' 
    ], 
) 