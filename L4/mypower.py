n = int(input('Enter value of n'))
r = int(input('Enter value of r'))

def power(n, r):
    result = 1
    for counter in range(r):
        result = result * n
    return result

result = power(n, r)
print(n, '**', r, '=', result, sep='')

'''
/Users/a6003261/Documents/class/pythonProjects/venv/bin/python /Users/a6003261/Documents/class/pythonProjects/L4/mypower.py
Enter value of n2
Enter value of r3
n**r is  8
computed result of function  8
2**3=8

Process finished with exit code 0
'''

