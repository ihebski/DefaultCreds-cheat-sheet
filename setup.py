import os
from setuptools import setup

with open('requirements.txt') as f:
        required = f.read().splitlines()

setup(name='default-creds',
    version='0.4',
    description='One place for all the default credentials to assist pentesters during an engagement, this document has several products default login/password gathered from multiple sources.',
    url='https://github.com/ihebski/DefaultCreds-cheat-sheet.git',
    install_requires=required,
    scripts=['creds']
)
