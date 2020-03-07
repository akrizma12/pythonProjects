import math

number = int(input("Enter number of ints to process: "))

min_so_far = -1
list = []
for count in range(number):
    next_int = int(input("Enter next integer: "))
    # bug was- the existing code was not checking against the entered values
    # added the list that takes all the user entered value and minds min amongst them
    list.append(next_int)
    min_so_far = min(list)  # note the built-in function min()

print("Smallest entered is:", min_so_far)

'''
/Users/a6003261/Documents/class/pythonProjects/venv/bin/python /Users/a6003261/Documents/class/pythonProjects/L3/find_min.py
Enter number of ints to process: 3
Enter next integer: 4
Enter next integer: 3
Enter next integer: 2
Smallest entered is: 2

Process finished with exit code 0
'''


