num = int(input("Enter number"))
one = int(input("Enter number one"))
two = int(input("Enter number two"))

if one > num > two:
    print(num, " is between " ,one, " and ", two)
elif two > num > one:
    print(num, " is between " ,one, " and ", two)
else:
    print(num, " is outside range")

# this is easier to understand
if (one > num > two) or (two > num > one):
    print(num, " is between " ,one, " and ", two)
else:
    print(num, " is outside range")


def range_check(num, one, two):
    if (one > num > two) or (two > num > one):
        print(num, " is between " ,one, " and ", two)
    else:
        print(num, " is outside range")


def main():
    range_check(num, one, two)


if __name__ == '__main__':
    main()

'''
/Users/a6003261/Documents/class/pythonProjects/venv/bin/python /Users/a6003261/Documents/class/pythonProjects/L5/int_check.py
Enter number1
Enter number one5
Enter number two9
1  is outside range
1  is outside range
1  is outside range

Process finished with exit code 0'''

'''
/Users/a6003261/Documents/class/pythonProjects/venv/bin/python /Users/a6003261/Documents/class/pythonProjects/L5/int_check.py
Enter number6
Enter number one1
Enter number two20
6  is between  1  and  20
6  is between  1  and  20
6  is between  1  and  20

Process finished with exit code 0
'''