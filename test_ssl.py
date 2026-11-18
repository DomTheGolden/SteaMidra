import ctypes
import os
full_path = r'C:\Users\domho\Downloads\ABDM\Compressed\SFF-6.10.1\dist\SteaMidra_GUI\_internal'
print('Full path:', full_path)
print('Exists:', os.path.isdir(full_path))
print('Files:', os.listdir(full_path)[:5])
try:
    libcrypto = ctypes.CDLL(os.path.join(full_path, 'libcrypto-3.dll'))
    print('libcrypto-3.dll loaded OK from _internal')
except Exception as e:
    print('libcrypto-3.dll failed:', e)

try:
    libssl = ctypes.CDLL(os.path.join(full_path, 'libssl-3.dll'))
    print('libssl-3.dll loaded OK from _internal')
except Exception as e:
    print('libssl-3.dll failed:', e)