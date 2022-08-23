"""
This type stub file was generated by pyright.
"""

import re
import string
from typing import NamedTuple, Tuple, Union

"""
Utility functions for working with the color names and color value
formats defined by the HTML and CSS specifications for use in
documents on the Web.

See documentation (in docs/ directory of source distribution) for
details of the supported formats, conventions and conversions.

"""
__version__ = ...
HEX_COLOR_RE = ...
HTML4 = ...
CSS2 = ...
CSS21 = ...
CSS3 = ...
SUPPORTED_SPECIFICATIONS = ...
SPECIFICATION_ERROR_TEMPLATE = ...
IntegerRGB = ...
PercentRGB = ...
HTML5SimpleColor = ...
IntTuple = Union[IntegerRGB, HTML5SimpleColor, Tuple[int, int, int]]
PercentTuple = Union[PercentRGB, Tuple[str, str, str]]
HTML4_NAMES_TO_HEX: dict[str, str] = ...
CSS2_NAMES_TO_HEX: dict[str, str] = ...
CSS21_NAMES_TO_HEX: dict[str, str] = ...
CSS3_NAMES_TO_HEX: dict[str, str] = ...
HTML4_HEX_TO_NAMES: dict[str, str] = ...
CSS2_HEX_TO_NAMES: dict[str, str] = ...
CSS21_HEX_TO_NAMES: dict[str, str] = ...
CSS3_HEX_TO_NAMES: dict[str, str] = ...

def normalize_hex(hex_value: str) -> str:
    """
    Normalize a hexadecimal color value to 6 digits, lowercase.

    """
    ...

def normalize_integer_triplet(rgb_triplet: IntTuple) -> IntegerRGB:
    """
    Normalize an integer ``rgb()`` triplet so that all values are
    within the range 0-255 inclusive.

    """
    ...

def normalize_percent_triplet(rgb_triplet: PercentTuple) -> PercentRGB:
    """
    Normalize a percentage ``rgb()`` triplet so that all values are
    within the range 0%-100% inclusive.

    """
    ...

def name_to_hex(name: str, spec: str = ...) -> str:
    """
    Convert a color name to a normalized hexadecimal color value.

    The optional keyword argument ``spec`` determines which
    specification's list of color names will be used. The default is
    CSS3.

    When no color of that name exists in the given specification,
    ``ValueError`` is raised.

    """
    ...

def name_to_rgb(name: str, spec: str = ...) -> IntegerRGB:
    """
    Convert a color name to a 3-tuple of integers suitable for use in
    an ``rgb()`` triplet specifying that color.

    """
    ...

def name_to_rgb_percent(name: str, spec: str = ...) -> PercentRGB:
    """
    Convert a color name to a 3-tuple of percentages suitable for use
    in an ``rgb()`` triplet specifying that color.

    """
    ...

def hex_to_name(hex_value: str, spec: str = ...) -> str:
    """
    Convert a hexadecimal color value to its corresponding normalized
    color name, if any such name exists.

    The optional keyword argument ``spec`` determines which
    specification's list of color names will be used. The default is
    CSS3.

    When no color name for the value is found in the given
    specification, ``ValueError`` is raised.

    """
    ...

def hex_to_rgb(hex_value: str) -> IntegerRGB:
    """
    Convert a hexadecimal color value to a 3-tuple of integers
    suitable for use in an ``rgb()`` triplet specifying that color.

    """
    ...

def hex_to_rgb_percent(hex_value: str) -> PercentRGB:
    """
    Convert a hexadecimal color value to a 3-tuple of percentages
    suitable for use in an ``rgb()`` triplet representing that color.

    """
    ...

def rgb_to_name(rgb_triplet: IntTuple, spec: str = ...) -> str:
    """
    Convert a 3-tuple of integers, suitable for use in an ``rgb()``
    color triplet, to its corresponding normalized color name, if any
    such name exists.

    The optional keyword argument ``spec`` determines which
    specification's list of color names will be used. The default is
    CSS3.

    If there is no matching name, ``ValueError`` is raised.

    """
    ...

def rgb_to_hex(rgb_triplet: IntTuple) -> str:
    """
    Convert a 3-tuple of integers, suitable for use in an ``rgb()``
    color triplet, to a normalized hexadecimal value for that color.

    """
    ...

def rgb_to_rgb_percent(rgb_triplet: IntTuple) -> PercentRGB:
    """
    Convert a 3-tuple of integers, suitable for use in an ``rgb()``
    color triplet, to a 3-tuple of percentages suitable for use in
    representing that color.

    This function makes some trade-offs in terms of the accuracy of
    the final representation; for some common integer values,
    special-case logic is used to ensure a precise result (e.g.,
    integer 128 will always convert to '50%', integer 32 will always
    convert to '12.5%'), but for all other values a standard Python
    ``float`` is used and rounded to two decimal places, which may
    result in a loss of precision for some values.

    """
    ...

def rgb_percent_to_name(rgb_percent_triplet: PercentTuple, spec: str = ...) -> str:
    """
    Convert a 3-tuple of percentages, suitable for use in an ``rgb()``
    color triplet, to its corresponding normalized color name, if any
    such name exists.

    The optional keyword argument ``spec`` determines which
    specification's list of color names will be used. The default is
    CSS3.

    If there is no matching name, ``ValueError`` is raised.

    """
    ...

def rgb_percent_to_hex(rgb_percent_triplet: PercentTuple) -> str:
    """
    Convert a 3-tuple of percentages, suitable for use in an ``rgb()``
    color triplet, to a normalized hexadecimal color value for that
    color.

    """
    ...

def rgb_percent_to_rgb(rgb_percent_triplet: PercentTuple) -> IntegerRGB:
    """
    Convert a 3-tuple of percentages, suitable for use in an ``rgb()``
    color triplet, to a 3-tuple of integers suitable for use in
    representing that color.

    Some precision may be lost in this conversion. See the note
    regarding precision for ``rgb_to_rgb_percent()`` for details.

    """
    ...

def html5_parse_simple_color(input: str) -> HTML5SimpleColor:
    """
    Apply the simple color parsing algorithm from section 2.4.6 of
    HTML5.

    """
    ...

def html5_serialize_simple_color(simple_color: IntTuple) -> str:
    """
    Apply the serialization algorithm for a simple color from section
    2.4.6 of HTML5.

    """
    ...

def html5_parse_legacy_color(input: str) -> HTML5SimpleColor:
    """
    Apply the legacy color parsing algorithm from section 2.4.6 of
    HTML5.

    """
    ...