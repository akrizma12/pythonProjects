import math

angle = float(input("Enter an angle in degrees: "))
print('angle ', angle)

radian = math.radians(angle)
print('radian ', radian)

sinSquare = math.sin(radian)**2
cosSquare = math.cos(radian)**2
print('Sin square plus Cos square ', sinSquare + cosSquare)

'''/Users/a6003261/Documents/class/pythonProjects/venv/bin/python /Users/a6003261/Documents/class/pythonProjects/L3/modules_1.py
Enter an angle in degrees: 180
angle  180.0
radian  3.141592653589793
Sin square plus Cos square  1.0

Process finished with exit code 0
'''

