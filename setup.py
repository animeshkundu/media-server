#!/usr/bin/env python

try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

setup(
    name='videopy',
    version='0.0.1',
    author='Animesh Kundu',
    description='HTTP Media Server for VLC',
    author_email='anik.edu@gmail.com',
    scripts=[],
    url='https://github.com/animeshkundu/media-server',
    license='LICENSE.txt',
    long_description=open('README.md').read(),
    install_requires=['netifaces==0.10.5'],
    entry_points={
        'console_scripts': ['videopy = video:main']
    },
)
