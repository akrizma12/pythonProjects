import pytest

def f2c(fahr):
    celc = (fahr - 32) * (5 / 9)
    return round(celc, 2)


def test_f2c(fahr, celc):
    assert celc == f2c(fahr)
    print(fahr, ' degree fahrenheit to ', celc, ' degree celcius is ', celc == f2c(fahr))


def main():
    test_f2c(32.0, 0.0)
    test_f2c(10.0, -12.22)
    test_f2c(40.0, 4.44)
    test_f2c(78.0, 25.56)
    test_f2c(0.0, -17.78)
    test_f2c(100.0, 37.78)
    test_f2c(-50.0, -45.56)
    test_f2c(-0.0, -17.78)
    test_f2c(-80.0, -62.22)
    test_f2c(-100.0, -73.33)


if __name__ == '__main__':
    main()

'''
/Users/a6003261/Documents/class/pythonProjects/venv/bin/python /Users/a6003261/Documents/class/pythonProjects/H4/test_f2c.py
32.0  degree fahrenheit to  0.0  degree celcius is  True
10.0  degree fahrenheit to  -12.22  degree celcius is  True
40.0  degree fahrenheit to  4.44  degree celcius is  True
78.0  degree fahrenheit to  25.56  degree celcius is  True
0.0  degree fahrenheit to  -17.78  degree celcius is  True
100.0  degree fahrenheit to  37.78  degree celcius is  True
-50.0  degree fahrenheit to  -45.56  degree celcius is  True
-0.0  degree fahrenheit to  -17.78  degree celcius is  True
-80.0  degree fahrenheit to  -62.22  degree celcius is  True
-100.0  degree fahrenheit to  -73.33  degree celcius is  True

Process finished with exit code 0
'''