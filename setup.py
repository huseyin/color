# -*- coding: utf-8 -*-

from setuptools import setup
import color

def readme():
    with open('README.md', 'r') as f:
        return f.read()
        
setup(
    name='color',
    version='0.1',
    description='python module of colorize string',
    long_description=readme(),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    keywords='colorize pycolorize color pycolor',
    url='http://github.com/htaslan/color',
    author='Hüseyin Tekinaslan',
    author_email='htaslan@bil.omu.edu.tr',
    license='MIT',
    packages=['color'],
    install_requires=[
        'enum34',
    ],
    include_package_data=True,
    zip_safe=False,
    entry_points={
        'console_scripts': [
            'pycolor = color.cli:main',
        ]
    },
)
