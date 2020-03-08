from H4 import revstr


def test_revstr(original, reversed):
    assert reversed == revstr.reverse(original)
    print('reversed == revstr.reverse(original), ', reversed == revstr.reverse(original))


if __name__ == '__main__':
    test_revstr('python', 'nohtyp')
    test_revstr('hello! summer', 'remmus !olleh')
    test_revstr('graduation', 'noitaudarg')
    test_revstr('1234rev4321', '1234ver4321')
    test_revstr('semester!!!', '!!!retsemes')
    test_revstr('23456789!@#$%', '%$#@!98765432')
    test_revstr('98418235762346523', '32564326753281489')
    test_revstr('very very looong string', 'gnirts gnoool yrev yrev')
    test_revstr('String with        spaces......', '......secaps        htiw gnirtS')
    test_revstr('CAPITALLETTER', 'RETTELLATIPAC')

'''
/Users/a6003261/Documents/class/pythonProjects/venv/bin/python /Users/a6003261/Documents/class/pythonProjects/H4/test_revstr.py
reversed == revstr.reverse(original),  True
reversed == revstr.reverse(original),  True
reversed == revstr.reverse(original),  True
reversed == revstr.reverse(original),  True
reversed == revstr.reverse(original),  True
reversed == revstr.reverse(original),  True
reversed == revstr.reverse(original),  True
reversed == revstr.reverse(original),  True
reversed == revstr.reverse(original),  True
reversed == revstr.reverse(original),  True
'''
