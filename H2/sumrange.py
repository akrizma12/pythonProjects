# Write a program that reads integers start and stop from the user,
# then calculates and prints the sum of the squares of each integer ranging from start to stop, inclusive.
# "Inclusive" means that both the values start and stop are included.

start = input("Enter start integer")
stop = input("Enter stop integer")

startInt = int(start)
stopInt = int(stop)
step = 1
stopInt += step
temp = 0
finalResult = 0

for num in range(startInt, stopInt, step):
    result = num*num
    finalResult = result+temp
    temp = finalResult
print(finalResult, end=' ')

'''
/Users/a6003261/Documents/class/pythonProjects/venv/bin/python /Users/a6003261/Documents/class/pythonProjects/H2/sumrange.py
Enter start integer2
Enter stop integer4
29 
Process finished with exit code 0
'''



