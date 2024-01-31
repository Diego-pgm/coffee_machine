from resources import resources
from functions import check_resources, report

test_drink = {
    "water": 300,
    "milk": 300,
    "coffee": 100
}

def test_noresources():
    global resources
    resources['water'] = 0
    resources['milk'] = 0
    resources['coffee'] = 0
    assert check_resources(test_drink) == False

def test_resources():
    assert check_resources(test_drink) == True


def test_report():
    assert report() == True


