# Write a program which prints out as many different Python object types as you can, such as: print(type([47])).
# Note you'll need to do some research on types beyond those mentioned in HTT2.

print(type([47, 56]))
print(type(''))
print(type(1234))
print(type(1234.00))

comp = 4 + 2j
print(type(comp))

print(type({'place': 'usa', 'language': 'english'}))
print(type((1,'spam', 4, 'U')))

a = True
print(type(a))

'''
/Users/a6003261/Documents/class/python/Homework/venv/bin/python /Users/a6003261/Documents/class/python/Homework/pytypes.py
<type 'list'>
<type 'str'>
<type 'int'>
<type 'float'>
<type 'complex'>
<type 'dict'>
<type 'tuple'>
<type 'bool'>

Process finished with exit code 0
'''