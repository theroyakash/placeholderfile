from setuptools import setup, find_packages
from os import path

__version__ = '1.2'

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='placeholderfile',
    version=__version__,
    description='Generates placeholderfile name',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/theroyakash/placeholderfile',
    download_url='https://github.com/theroyakash/placeholderfile/tarball/main',
    license='Apache License',
    packages=find_packages(),
    include_package_data=True,
    author='theroyakash',
    author_email='royakashappleid@icloud.com'
)