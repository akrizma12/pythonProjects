N = int(input('Enter the value of n'))

print('*'*N)
print("\r")

for i in range(0, N):
    for j in range(0, N):
        print("*", end="")
    print("\r")

'''
/Users/a6003261/Documents/class/pythonProjects/venv/bin/python /Users/a6003261/Documents/class/pythonProjects/L6/patterns.py
Enter the value of n4
****

****
****
****
****

Process finished with exit code 0
'''