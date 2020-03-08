def f2c(fahr):
    celc = (fahr - 32) * (5 / 9)
    return round(celc, 2)


def main():
    fahr = float(input('Enter temperature in degrees Fahrenheit'))
    celc = f2c(fahr)
    print(fahr ,'degrees F is to ', celc, 'degrees C')


if __name__ == "__main__":
    main()

'''
/Users/a6003261/Documents/class/pythonProjects/venv/bin/python /Users/a6003261/Documents/class/pythonProjects/H4/ftoc.py
Enter temperature in degrees Fahrenheit32
32.0 degrees F is to  0.0 degrees C

Process finished with exit code 0'''

