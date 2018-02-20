Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> print('hello')
hello
>>> print('hello')

hello
>>> test.py
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    test.py
NameError: name 'test' is not defined
>>> C:\Users\asatharla.EVOKE\AppData\Local\Programs\Python\Python36\test.py
SyntaxError: unexpected character after line continuation character
>>> execfile('C:\Users\asatharla.EVOKE\AppData\Local\Programs\Python\Python36\test.py')
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape
>>> execfile('C:\Users\asatharla.EVOKE\AppData\Local\Programs\Python\Python36\test.py')
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape
>>> exec(open(test.py).read())
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    exec(open(test.py).read())
NameError: name 'test' is not defined
>>> exec(open('test.py').read())
Hello World!
H
llo
llo World!
Hello World!Hello World!
Hello World!TEST
hello
>>> import subprocess as sp
sp.call('cls',shell=True)
SyntaxError: multiple statements found while compiling a single statement
>>> import py_compile
>>> py_compile.compile('test.py')
SyntaxError: multiple statements found while compiling a single statement
>>> import py_compile
py_compile.compile('test.py')
SyntaxError: multiple statements found while compiling a single statement
>>> import os
os.system("clear")
SyntaxError: multiple statements found while compiling a single statement
>>> import os
>>> os.system("clear")
1
>>> import py_compile
>>> py_compile.compile('test.py')
'__pycache__\\test.cpython-36.pyc'
>>> py_compile.compile('C:\Users\asatharla.EVOKE\AppData\Local\Programs\Python\Python36\test.py')
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape
>>> import subprocess as sp
>>> sp.call('cls',shell=True)
0
>>> sp.call('cls')
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    sp.call('cls')
  File "C:\Users\asatharla.EVOKE\AppData\Local\Programs\Python\Python36\lib\subprocess.py", line 267, in call
    with Popen(*popenargs, **kwargs) as p:
  File "C:\Users\asatharla.EVOKE\AppData\Local\Programs\Python\Python36\lib\subprocess.py", line 707, in __init__
    restore_signals, start_new_session)
  File "C:\Users\asatharla.EVOKE\AppData\Local\Programs\Python\Python36\lib\subprocess.py", line 992, in _execute_child
    startupinfo)
FileNotFoundError: [WinError 2] The system cannot find the file specified
>>> 
