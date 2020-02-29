# Write a program that prints out 10 random integers, each in the range 1 through 6.
from random import randrange

for i in range(1, 11, 1):
    rand = randrange(1, 11)
    print(rand)

'''
/Users/a6003261/Documents/class/pythonProjects/venv/bin/python /Users/a6003261/Documents/class/pythonProjects/H3/rand10.py
5
8
9
4
9
7
10
8
2
5

Process finished with exit code 0
'''