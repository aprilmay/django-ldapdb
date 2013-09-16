#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name = "django-ldapdb",
    version = "0.1.0",
    #license = ldapdb.__license__,
    url = "http://opensource.bolloretelecom.eu/projects/django-ldapdb/",
    author = "Jeremy Laine",
    author_email = "jeremy.laine@bolloretelecom.eu",
    #packages = ['ldapdb', 'ldapdb.backends', 'ldapdb.backends.ldap', 'ldapdb.models'],
    packages = find_packages(),
    zip_safe = False,
    install_requires = [
        'python-ldap',
    ]
)
