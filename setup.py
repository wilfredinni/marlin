# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import os

marlin = os.path.join('marlin', 'scripts', 'marlin.bat')

with open('README.md') as f:
    readme = f.read()


setup(
    name='marlin-bookmark',
    version='0.1.0',
    description='Swim between bookmarks in the terminal',
    long_description=readme,
    author='Carlos Montecinos Geisse',
    author_email='carlos.w.montecinos@gmail.com',
    url='https://github.com/wilfredinni/marlin',
    license='MIT License',
    packages=find_packages(exclude=('tests', 'docs')),
    include_package_data=True,
    install_requires=['click', 'colorama'],
    python_requires='>=3',
    scripts=[marlin],
    entry_points={
        'console_scripts': [
            'bookmark = marlin.bookmark:main',
            'rmark = marlin.rmark:main',
            'marlin_help = marlin.marlin_help:main',
        ]
    },
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ]
)
