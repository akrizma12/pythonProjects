print("Trying to divide 5 by 2", 5 % 2)
print("Trying to divide 5 by 2", 9 % 5)
print("Trying to divide 5 by 2", 15 % 12)
print("Trying to divide 5 by 2", 12 % 15)
print("Trying to divide 5 by 2", 6 % 6)
print("Trying to divide 5 by 2", 0 % 7)

try:
    print("Trying to divide 5 by 2", 7 % 0)
except:
    print("Attempt to 0 any number gives ZeroDivisionError. Please try to put any other number other than 0")

'''
/usr/bin/python2.7 /Users/a6003261/Documents/class/pythonProjects/H1/htt2_6.py
('Trying to divide 5 by 2', 1)
('Trying to divide 5 by 2', 4)
('Trying to divide 5 by 2', 3)
('Trying to divide 5 by 2', 12)
('Trying to divide 5 by 2', 0)
('Trying to divide 5 by 2', 0)
Attempt to 0 any number gives ZeroDivisionError. Please try to put any other number other than 0

Process finished with exit code 0
'''