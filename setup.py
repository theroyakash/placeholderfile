from setuptools import setup, find_packages
from os import path

__version__ = '1.0.1'

here = path.abspath(path.dirname(__file__))

setup(
    name='placeholderfile',
    version=__version__,
    description='Generates placeholderfile name',
    url='https://github.com/theroyakash/placeholderfile',
    download_url='https://github.com/theroyakash/placeholderfile/tarball/main',
    license='Apache License',
    packages=find_packages(),
    include_package_data=True,
    author='theroyakash',
    author_email='royakashappleid@icloud.com'
)