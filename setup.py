#!/usr/bin/env python
# -* encoding: utf-8 *-
import os
from setuptools import setup

HERE = os.path.dirname(__file__)

try:
    long_description = open(os.path.join(HERE, 'README.rst')).read()
except IOError:
    long_description = None


setup(
    name="django-postgresql-setrole",
    version="1.0.0",
    packages=["postgresql_setrole"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "Programming Language :: Python :: 2.7.*",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX",
    ],
    url="https://github.com/arm-g/django-postgresql-setrole",
    author="Armen Ghahramanyan (@teamable)",
    author_email="armen@teamable.com",
    description="Execute `SET ROLE` statement on every PostgreSQL connection",
    long_description=long_description,
)
