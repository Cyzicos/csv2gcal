#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'Click>=6.0',
    # TODO: put package requirements here
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='csv2gcal',
    version='0.1.0',
    description="csv2gcal creates google calender events out of a csv file.",
    long_description=readme + '\n\n' + history,
    author="Hannes Vietz",
    author_email='h.vietz@gmail.com',
    url='https://github.com/Cyzicos/csv2gcal',
    packages=[
        'csv2gcal',
    ],
    package_dir={'csv2gcal':
                 'csv2gcal'},
    entry_points={
        'console_scripts': [
            'csv2gcal=csv2gcal.cli:main'
        ]
    },
    include_package_data=True,
    install_requires=requirements,
    license="GNU General Public License v3",
    zip_safe=False,
    keywords='csv2gcal',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
