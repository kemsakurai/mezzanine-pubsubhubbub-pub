# -*- coding: utf-8 -*-
"""
   Copyright 2016 Kem

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""

from __future__ import unicode_literals

import os
import sys

from setuptools import setup, find_packages

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

import mezzanine_pubsubhubbub_pub

setup(
    name='mezzanine-pubsubhubbub-pub',
    version=mezzanine_pubsubhubbub_pub.VERSION,
    url=mezzanine_pubsubhubbub_pub.SITE,
    author=mezzanine_pubsubhubbub_pub.AUTHOR,
    author_email=mezzanine_pubsubhubbub_pub.EMAIL,
    license=mezzanine_pubsubhubbub_pub.LICENSE,
    description='publisher of pubsubhubbub (PuSH) in Mezzanine.',
    long_description=open('README.md').read(),
    keywords='django, mezzanine, pubsubhubbub',
    packages=find_packages(),
    setup_requires=('setuptools'),
    install_requires=('setuptools',
                      'Mezzanine>=4.2.0',
                      'requests>=2.1.0',),
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        'Environment :: Web Environment',
        'Framework :: Django :: 1.10',
        'Intended Audience :: Developers',
        "License :: OSI Approved :: Apache Software License",
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: '
        'Application Frameworks',
        'Topic :: Software Development :: Libraries :: Python Modules', ],
    zip_safe=False,
    include_package_data=True,
)
