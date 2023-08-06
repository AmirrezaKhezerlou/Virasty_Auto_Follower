import sys
from cx_Freeze import setup, Executable

setup(
    name = "Virasti Auto Follow Bot",
    version = "1.0",
    description = "Virasty Follower",
    executables = [Executable("MainUi.py", base = "Win32GUI", icon="C:/Users/Lenovo/Downloads/Compressed/icons/windows_1.ico")])
