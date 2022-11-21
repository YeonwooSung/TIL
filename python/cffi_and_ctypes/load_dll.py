import platform
import ctypes


def load_dll(name):
    if platform.system() == 'Windows':
        return ctypes.WinDLL(name)
    else:
        return ctypes.cdll.LoadLibrary(ctypes.util.find_library(name))
