import contextlib
import re

import autopep8

from pyecore.resources import ResourceSet
import pyecore.ecore as ecore

import pyecoregen
import pyecoregen.adapter
import pyecoregen.ecore


def to_snake_case(name):
    s1 = re.sub(r"(.)([A-Z][a-z]+)", r"\1_\2", name)
    return re.sub("([a-z0-9])([A-Z])", r"\1_\2", s1).lower()


@contextlib.contextmanager
def snake_pythonic_names():
    """ Monkey patch pythonic_names to get snake name for each EOperation. """
    original_get_attribute = ecore.ENamedElement.__getattribute__

    def get_attribute(self, name):
        value = original_get_attribute(self, name)

        if name == "name":
            value = pyecoregen.adapter.fix_name_clash(value)
            if isinstance(self, ecore.EOperation):
                value = to_snake_case(value)

        return value

    ecore.ENamedElement.__getattribute__ = get_attribute
    yield
    ecore.ENamedElement.__getattribute__ = original_get_attribute


pyecoregen.adapter.pythonic_names = snake_pythonic_names


def setup_resourceset():
    import pyuml2.types as types
    import pyuml2.uml as uml

    ecore_uri = "platform:/plugin/org.eclipse.emf.ecore/model/Ecore.ecore"
    types_uri = "platform:/plugin/org.eclipse.uml2.types/model/Types.ecore"
    uml_uri = "platform:/plugin/org.eclipse.uml2.uml/model/UML.ecore"
    uml_profile_uri = "platform:/plugin/org.eclipse.uml2.uml.profile.standard" \
                      "/model/Standard.ecore"

    rset = ResourceSet()
    rset.metamodel_registry[ecore_uri] = ecore
    rset.metamodel_registry[types_uri] = types
    rset.metamodel_registry[uml_uri] = uml
    # TODO: add uml_standard_profile (necessary for Refine and Trace)
    return rset


def generate_code():
    def format_autopep8(raw: str) -> str:
        return autopep8.fix_code(raw, options={"experimental": True})

    rset = setup_resourceset()
    sysml_ecore = rset.get_resource("model/sysml.ecore").contents[0]
    generator = pyecoregen.ecore.EcoreGenerator(
        user_module="pysysml.sysml_mixins",
    )
    for task in generator.tasks:
        task.formatter = format_autopep8
    generator.generate(sysml_ecore, "pysysml")


if __name__ == "__main__":
    generate_code()
