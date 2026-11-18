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
Runtime hook to ensure OpenSSL DLLs are found.
This adds the _internal directory to the DLL search path so that
libcrypto-3.dll and libssl-3.dll can be loaded.
"""

import os
import sys

# Get the directory where the executable is running from
if getattr(sys, 'frozen', False):
    # Running as PyInstaller bundle
    base_dir = os.path.dirname(sys.executable)
    internal_dir = os.path.join(base_dir, '_internal')
    
    # Add _internal to PATH so OpenSSL DLLs can be found
    if os.path.isdir(internal_dir):
        os.environ['PATH'] = internal_dir + os.pathsep + os.environ.get('PATH', '')
        
        # Also add to DLL search path on Windows 10+
        if hasattr(os, 'add_dll_directory'):
            try:
                os.add_dll_directory(internal_dir)
            except Exception:
                pass