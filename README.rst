===========================================================
PySysML: A Pythonic Implementation of the SysML UML Profile
===========================================================

|master-build| |coverage| |license|

.. |master-build| image:: https://travis-ci.org/pyecore/pyuml2.svg?branch=master
    :target: https://travis-ci.org/pyecore/pyuml2

.. |coverage| image:: https://coveralls.io/repos/github/pyecore/pyuml2/badge.svg?branch=master
    :target: https://coveralls.io/github/pyecore/pyuml2?branch=master

.. |license| image:: https://img.shields.io/badge/license-New%20BSD-blue.svg
    :target: https://raw.githubusercontent.com/pyecore/pyuml2/master/LICENSE

PySysML is the implementation of the SysML 1.4 UML profile for Python >=3.4,
relying on PyEcore. The goal of this project is to provide an almost-full
implementation of the SysML 1.4 profile in Python with Profile supports and
compatibility with the Eclipse UML2 project.


Installation
============

There is not yet a pypi package, you can manually install the project using:

.. code-block:: shell

    $ pip install -e .

Documentation
=============

Here is how to currently load a UML2 model using the implementation.

.. code-block:: python

    from pyecore.resources import ResourceSet
    import pysysml.sysml as sysml

    rset = ResourceSet()
    rset.metamodel_registry[sysml.nsURI] = sysml
    resource = rset.get_resource('path/to/my/model.sysml')
    model = resource.contents[0]

    print(model.name)
    print(model.packagedElement)
    print(model.nestedPackage)
