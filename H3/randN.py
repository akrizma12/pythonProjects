from random import randrange

numRolls = input('Enter num rolls')
num = int(numRolls)
sumOfRolls = 0

for n in range(1, num, 1):
    rand = randrange(1, 7)
    print('number')
    sumOfRolls = rand + sumOfRolls

print(sumOfRolls / num)

'''
/Users/a6003261/Documents/class/pythonProjects/venv/bin/python /Users/a6003261/Documents/class/pythonProjects/H3/randN.py
Enter num rolls3
2.3333333333333335

Process finished with exit code 0
'''
