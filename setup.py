"""
Ce fichier de configuration est utilisé pour configurer la distribution
du package Python. Il contient des informations essentielles telles que le nom
du package, la version, les packages inclus et les dépendances requises.

Ce fichier utilise setuptools, une bibliothèque pour faciliter la création,
la distribution et l'installation de packages Python.

Pour plus d'informations sur l'utilisation de setuptools, consultez :
https://setuptools.pypa.io/en/latest/userguide/quickstart.html
"""

from setuptools import setup, find_packages

setup(
    name="dashboard",
    version="0.0.2",
    description="",
    url="https://github.com/thalleslimasys/mcc-dashboard",
    author="",
    author_email="",
    license="GNU AGPL3",
    packages=find_packages(),
    include_package_data=True,
    python_requires=">=3.8",
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Information Technology",
        "Topic :: Software Development :: Build Tools",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Framework :: Django :: 4.2",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
)
