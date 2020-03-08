def reverse(st):
    reversed = ''
    for char in st:
        reversed = char + reversed
    return reversed


if __name__ == '__main__':
    s = input('Enter any string')
    reverseStr = reverse(s)
    print('Reversed string is ', reverseStr)

'''
/Users/a6003261/Documents/class/pythonProjects/venv/bin/python /Users/a6003261/Documents/class/pythonProjects/H4/revstr.py
Enter any stringoriginalString
Reversed string is  gnirtSlanigiro

Process finished with exit code 0
'''