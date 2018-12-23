===========================================================
PySysML: A Pythonic Implementation of the SysML UML Profile
===========================================================

PySysML is the implementation of the SysML 1.4 UML profile for Python >=3.4,
relying on PyEcore. The goal of this project is to provide an almost-full
implementation of the SysML 1.4 profile in Python with Profile supports and
compatibility with the Eclipse UML2 project.


Installation
============

There is not yet a pypi package for pysysml nor pyuml, you can manually install
both projects using:

.. code-block:: shell

    $ pip install git+https://github.com/pyecore/pyuml2
    $ pip install -e .

Documentation
=============

This is not currently working as there is an issue with the parsing of the
SysML ecore model due to unlimited literal being less than zero.

You can try to build the SysML model by running:

.. code-block:: shell
    $ python generator/sysml_generator.py
