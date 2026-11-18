# SteaMidra - Steam game setup and manifest tool (SFF)
# Copyright (c) 2025-2026 Midrag (https://github.com/Midrags)
#
# This file is part of SteaMidra.
#
# SteaMidra is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# SteaMidra is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with SteaMidra.  If not, see <https://www.gnu.org/licenses/>.

"""
Shim to provide pyyaml-compatible API using ruamel.yaml.
This is a fallback for Python versions where pyyaml wheels are not available.
"""

import ruamel.yaml

# Create a YAML instance that behaves like pyyaml's safe_load/safe_dump
_yaml = ruamel.yaml.YAML(typ='safe')
_yaml.default_flow_style = False
_yaml.allow_duplicate_keys = True


def safe_load(stream):
    """Parse a YAML stream (string or file-like object) and return a Python object."""
    if hasattr(stream, 'read'):
        return _yaml.load(stream)
    return _yaml.load(stream)


def safe_dump(data, stream=None, **kwargs):
    """Serialize a Python object into a YAML stream."""
    if stream is None:
        import io
        stream = io.StringIO()
        _yaml.dump(data, stream)
        return stream.getvalue()
    _yaml.dump(data, stream)


def load(stream, Loader=None):
    """Load YAML from a stream. Loader is ignored (always safe)."""
    return safe_load(stream)


def dump(data, stream=None, Dumper=None, **kwargs):
    """Dump YAML to a stream. Dumper is ignored."""
    return safe_dump(data, stream, **kwargs)


# Compatibility aliases
class YAMLError(Exception):
    pass


class Mark:
    pass


class MarkedYAMLError(YAMLError):
    pass


# For compatibility with code that does `from yaml import CLoader, CDumper`
try:
    from ruamel.yaml import CLoader, CDumper
except ImportError:
    CLoader = None
    CDumper = None

# For code that does `yaml.SafeLoader`
SafeLoader = None
SafeDumper = None

# Make this module look like the yaml module
__version__ = ruamel.yaml.__version__
__all__ = ['safe_load', 'safe_dump', 'load', 'dump', 'YAMLError', 'Mark', 'MarkedYAMLError', 
           'CLoader', 'CDumper', 'SafeLoader', 'SafeDumper']