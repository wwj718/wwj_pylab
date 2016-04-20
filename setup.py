#!/usr/bin/env python
# -*- coding: utf-8 -*-


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    "requests==2.9.1",
    "click==6.3",
    ""
    # TODO: put package requirements here
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='wwj_pylab',
    version='0.1.0',
    description="my python laboratory",
    long_description=readme + '\n\n' + history,
    author="wenjie wu",
    author_email='wuwenjie718@gmail.com',
    url='https://github.com/wwj718/wwj_pylab',
    packages=[
        'wwj_pylab',
    ],
    package_dir={'wwj_pylab':
                 'wwj_pylab'},
    include_package_data=True,
    install_requires=requirements,
    license="ISCL",
    zip_safe=False,
    keywords='wwj_pylab',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: ISC License (ISCL)',
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
    tests_require=test_requirements,
    entry_points={
         'console_scripts': [
                         'wwj_pylab = wwj_pylab.wwj_pylab:main'
            ]
        }
)
