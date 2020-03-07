import unittest


def km_to_miles(km):
    return km*0.621371

def miles_to_km(miles):
    return miles*1.60934

class km_to_miles(unittest.TestCase):
    mileValue = km_to_miles(1)
    assert mileValue == 0.621371

    mileValue = round(km_to_miles(2), 2)
    assert mileValue == 1.24

    mileValue =round(km_to_miles(3), 2)
    assert mileValue == 1.86

    mileValue = round(km_to_miles(4), 2)
    assert mileValue == 2.49

    mileValue = round(km_to_miles(5), 2)
    assert mileValue == 3.11

class miles_to_km(unittest.TestCase):
    kmValue = miles_to_km(1)
    assert kmValue == 1.60934

    kmValue = round(miles_to_km(2), 2)
    assert kmValue == 3.22

    kmValue =round(miles_to_km(3), 2)
    assert kmValue == 4.83

    kmValue = round(miles_to_km(4), 2)
    assert kmValue == 6.44

    kmValue = round(miles_to_km(5), 2)
    assert kmValue == 8.05