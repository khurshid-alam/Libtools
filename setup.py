import os
import sys
import setuptools
from distutils.core import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='libtools',
    version="1.25.0",
    author='Khurshid Alam',
    author_email='khurshid.alam@linuxmail.org',
    url='http://dev.libtools.com',
    description='More shopisticated wrapper around standard library',
    long_description=read('readme.md'),
    packages=['libtools'],
    classifiers=[
        'Development Status :: 4 - Production/Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Topic :: Software Development :: Libraries',
        'Programming Language :: Python :: 3'
    ],
    license='BSD',
    install_requires=[
        'gi',
        'gobject',
    ],
)
