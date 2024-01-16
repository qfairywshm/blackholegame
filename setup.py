import PyInstaller.__main__
import os

PyInstaller.__main__.run([
    'name-' % 'setup.exe',
    '--onefile',
    '--windowed',
    os.path.join('C:\Users\Анна\PycharmProjects\blackholegame\main.py', 'main.py'), """your script and path to the script"""
])