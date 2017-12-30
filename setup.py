# coding=utf-8
from distutils.util import convert_path
from setuptools import setup, find_packages
from codecs import open
import os


def read(fname):
    path = os.path.join(os.path.dirname(__file__), fname)
    return open(path, encoding='utf-8').read()


exec(read('spddb/version.py'))


setup(
    name="spddb",
    version=__version__,
    packages=find_packages(),

    # development metadata
    zip_safe=True,

    # metadata for upload to PyPI
    author="CVSAE",
    author_email="cvsc@gmx.com",
    description="Simple python dictionary database",
    license="MIT",
    keywords="database nosql python dictionary",
    url="https://github.com/spddb/spddb",
    classifiers=[
        
    ],


    long_description=read('README.md'),
)