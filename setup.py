# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name="core2",
    version="0.1dev",
    description="IRC bot for final project for CIS 4932 (Special Topics in CS: Python)",
    author="Violet Jewel",
    url="https://github.com/VioletJewel/core2duo",
    license="GPLv3",
    include_package_data=True,
    packages=find_packages("src"),
    package_dir={"": "src"},
    entry_points={ "console_scripts": ["core2 = core2.bot:main"], },
    install_requires=[ ],
)
