# setup.py
from setuptools import setup, find_packages

setup(
    name="myproject",
    version="0.1",
    packages=find_packages(),
    entry_points={"console_scripts": ["myproject=main:main"]},
)
