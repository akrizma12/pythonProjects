import pytest


def speeding_fine(speed, limit):
    fine = 0
    if speed > limit:
        fine = 100
        additionalSpeed = (speed - limit)  # MPH over the limit
        if additionalSpeed:
            fine = fine + 10 * additionalSpeed

            if (90 < speed < 100):
                fine = fine + 100

        elif speed >= 100:
            fine = 500

        print('Speed was illegal')
        print('Amount of fine is: ', fine, '\n')
    else:
        print('Speed was legal \n')
    return fine


def test_speeding_fine():
    print('speed was 80, limit was 60')
    fine = speeding_fine(80, 60)
    assert fine == 300

    print('speed was 50, limit was 60')
    fine = speeding_fine(50, 60)
    assert fine == 0

    print('speed was 95, limit was 60')
    fine = speeding_fine(95, 60)
    assert fine == 550

    print('speed was 100, limit was 60')
    fine = speeding_fine(100, 60)
    assert fine == 500


def main():
    test_speeding_fine()


if __name__ == '__main__':
    main()

'''
/Users/a6003261/Documents/class/pythonProjects/venv/bin/python /Users/a6003261/Documents/class/pythonProjects/L5/bool_if_TDD.py
speed was 80, limit was 60
Speed was illegal
Amount of fine is:  300 

speed was 50, limit was 60
Speed was legal 

speed was 95, limit was 60
Speed was illegal
Amount of fine is:  550 

speed was 100, limit was 60
Speed was illegal
Amount of fine is:  500 


Process finished with exit code 0

'''
