#!/usr/bin/python3
import marshal
import types

#Open the hidden_4.pyc file
with open('hidden_4.pyc', 'rb') as f:
    #Read the content of the file as bytes
    pyc_file = f.read()

#Get the code object from the file
code = marshal.loads(pyc_file[8:])

#Get the list of all the names used in the code
names = list(code.co_names)

#Sort the list in alphabetical order
names.sort()

#Print the names that do not start with __
for name in names:
    if not name.startswith('__'):
        print(name)
