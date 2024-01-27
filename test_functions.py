from resources import resources

test_drink = {
    "water": 300,
    "milk": 300,
    "coffee": 100
}

def test_resources():
    for item in test_drink:
        assert resources[item] >= test_drink[item]
    
test_resources()
