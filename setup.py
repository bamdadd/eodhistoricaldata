# -*- coding: utf-8 -*-
import os

from setuptools import setup, find_packages
from datetime import datetime

if os.path.exists('../version/version'):
    with open('../version/version') as f:
        version = f.read()
else:
    version = '0.1.0dev'


with open('README.md') as f:
    README = f.read()

with open('requirements.txt') as f:
    requirements = f.readlines()

setup(
    name='eodhistoricaldata',
    version=version,
    description='eodhistoricaldata unofficial python library',
    long_description=README,
    long_description_content_type="text/markdown",
    author='Satis engineering',
    author_email='engineering@satis.ai',
    url='https://github.com/bamdadd/eodhistoricaldata',
    license='MIT',
    install_requires=requirements,
    setup_requires=requirements+"pytest",
    pbr=True,
    package_dir={"": "src"},
    packages=find_packages(where="src"),
)

