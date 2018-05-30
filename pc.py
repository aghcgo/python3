from ctypes import cdll
import easygui as gui
libc = cdll.LoadLibrary('libc.so.6')  # Load standard C library on Linux
# libc = cdll.LoadLibrary('libc.dylib')  # Load standard C library on Mac
# libc = cdll.msvcrt  # Load standard C library on Windows
 
print (libc.time(None))

from ctypes import cdll
 
libc = cdll.LoadLibrary('libc.so.6')  # Load standard C library on Linux
# libc = cdll.LoadLibrary('libc.dylib')  # Load standard C library on Mac
# libc = cdll.msvcrt  # Load standard C library on Windows
 
print (libc.time(None))

gui.msgbox("郑怀国")

gui.passwordbox()
