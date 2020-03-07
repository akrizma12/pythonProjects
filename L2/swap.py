# Write a program that prompts and reads two integers (int) from the user, assigning the first to variable one
# # and the second to variable two. Then write code which exchanges or swaps the values in one and two.


input1 = int(input("Enter first integer"))
input2 = int(input("Enter second integer"))

print ('Entered values (vars input1, input2)=', input1,input2)

temp = input1
input1 = input2

input2 = temp

print('After swap values are (vars input1, input2 after swap)', input1, input2)

'''
/Users/a6003261/Documents/class/pythonProjects/venv/bin/python /Users/a6003261/Documents/class/pythonProjects/L2/swap.py
Enter first integer1
Enter second integer2
Entered values (vars input1, input2)= 1 2
After swap values are (vars input1, input2 after swap) 2 1

Process finished with exit code 0
'''

