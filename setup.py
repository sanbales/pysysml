#!/usr/bin/env python
import re
from setuptools import setup, find_namespace_packages


try:
    __version__ = re.findall(
        r"""__version__ = ["']+([0-9\.]*)["']+""",
        open('pysysml/__init__.py').read(),
    )[0]
except IndexError:
    raise RuntimeError("Could not find __version__ in 'cortex/__init__.py'!")

setup(
    name='pysysml',
    version=__version__,
    description="A Python(ic) implementation of the SysML 1.4 metamodel",
    long_description=open("README.rst").read(),
    keywords="model metamodel MDE UML SysML",
    url='https://github.com/sanbales/pysysml',
    author='Santiago Balestrini-Robinson',
    author_email='sanbales@gmail.com',
    packages=find_namespace_packages(include="pysysml.*"),
    package_data={'': ["README.rst", "LICENSE", "CHANGELOG.rst"]},
    include_package_data=True,
    install_requires=["pyecore"],
    tests_require=["pytest"],
    license="BSD 3-Clause",
    classifiers=[
        "Development Status :: 4 - Beta",
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries',
        'License :: OSI Approved :: BSD License',
    ]
)
