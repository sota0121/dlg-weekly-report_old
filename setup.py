#!/usr/bin/env python

from setuptools import setup

import drep

setup(
    name='drep',
    version=drep.__version__,
    description='A supporter for reporting slack community.',
    author='Sota Masuda',
    packages=['drep', 'drep.dreplib'],
    install_requires=["slackclient"],
    entry_points={
        'console_scripts': ['drep = drep:run_main'],
    }
)


