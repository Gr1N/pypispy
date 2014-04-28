# -*- coding: utf-8 -*-

import os

from setuptools import setup
from setuptools import find_packages


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()


long_description = """{0}

{1}
""".format(read('README.rst'), read('HISTORY.rst'))


setup(
    name='pypispy',
    version='0.1.3',
    description='"Big Brother" is watching your packages!',
    long_description=long_description,
    classifiers=(
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
    ),
    author='Nikita Grishko',
    author_email='grin.minsk@gmail.com',
    url='http://gr1n.github.io/pypispy/',
    license='MIT',
    packages=find_packages(),
    install_requires=[
        'setuptools',
        'requests>=2.2.1',
    ],
    extras_require={
        'development': (
            'flake8',
            'zest.releaser',
            'check-manifest',
        ),
    },
    include_package_data=True,
    zip_safe=False,
    scripts=(
        'pypispy',
    ),
)
