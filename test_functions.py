from resources import resources
from functions import check_resources, report

test_drink = {
    "water": 300,
    "milk": 300,
    "coffee": 100
}


def test_resources():
    assert check_resources(test_drink) == True


def test_no_resources():
    resources = {
        "water": 0,
        "milk": 0,
        "coffee": 0
    }
    assert check_resources(test_drink) == False

def test_report():
    assert report() == True
