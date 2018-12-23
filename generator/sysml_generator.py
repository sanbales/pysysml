import contextlib
import re

import autopep8

import pyecore.ecore
import pyecore.resources

import pyecoregen.adapter
import pyecoregen.ecore

import pyuml2.types
import pyuml2.uml


def to_snake_case(name):
    s1 = re.sub(r"(.)([A-Z][a-z]+)", r"\1_\2", name)
    return re.sub("([a-z0-9])([A-Z])", r"\1_\2", s1).lower()


@contextlib.contextmanager
def snake_pythonic_names():
    """ Monkey patch pythonic_names to get snake name for each EOperation. """
    original_get_attribute = pyecore.ecore.ENamedElement.__getattribute__

    def get_attribute(self, name):
        value = original_get_attribute(self, name)

        if name == "name":
            value = pyecoregen.adapter.fix_name_clash(value)
            if isinstance(self, pyecore.ecore.EOperation):
                value = to_snake_case(value)

        return value

    pyecore.ecore.ENamedElement.__getattribute__ = get_attribute
    yield
    pyecore.ecore.ENamedElement.__getattribute__ = original_get_attribute


pyecoregen.adapter.pythonic_names = snake_pythonic_names


def setup_resourceset():
    ecore_uri = "platform:/plugin/org.eclipse.emf.ecore/model/Ecore.ecore"
    types_uri = "platform:/plugin/org.eclipse.uml2.types/model/Types.ecore"
    uml_uri = "platform:/plugin/org.eclipse.uml2.uml/model/UML.ecore"
    uml_profile_uri = "platform:/plugin/org.eclipse.uml2.uml.profile.standard" \
                      "/model/Standard.ecore"

    rset = pyecore.resources.ResourceSet()
    rset.metamodel_registry[ecore_uri] = pyecore.ecore
    rset.metamodel_registry[types_uri] = pyuml2.types
    rset.metamodel_registry[uml_uri] = pyuml2.uml
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
