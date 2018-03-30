"""
Python bindings for GLFW.
"""

__author__ = 'Florian Rhiem (florian.rhiem@gmail.com)'
__copyright__ = 'Copyright (c) 2013-2018 Florian Rhiem'
__license__ = 'MIT'
__version__ = '1.6'

# By default (ERROR_REPORTING = True), GLFW errors will be reported as Python
# exceptions. Set ERROR_REPORTING to False or set a curstom error callback to
# disable this behavior.
ERROR_REPORTING = True

# By default (NORMALIZE_GAMMA_RAMPS = True), gamma ramps are expected to
# contain values between 0 and 1, and the conversion to unsigned shorts will
# be performed internally. Set NORMALIZE_GAMMA_RAMPS to False if you want
# to disable this behavior and use integral values between 0 and 65535.
NORMALIZE_GAMMA_RAMPS = True


def _pythonize_names():
    """
    This function will convert the prefixed, glfwCamelCase function names of
    the C-style GLFW module to the pythonic snake_case and remove the GLFW_
    prefix from its constants.

    The code for this is only called once, but wrapped in a function
    to prevent cluttering the module namespace.
    """
    import re
    from . import GLFW

    _globals = globals()

    for name in dir(GLFW):
        if name.startswith("GLFW_"):
            # remove GLFW_ prefix
            constant_name = name[5:]
            _globals[constant_name] = getattr(GLFW, name)
        elif name.startswith("glfw"):
            # convert function names to snake_case
            function_name = re.sub('(?!^)([A-Z]+)', r'_\1', name[4:]).lower()
            _globals[function_name] = getattr(GLFW, name)

_pythonize_names()
