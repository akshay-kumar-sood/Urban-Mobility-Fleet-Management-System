import pytest
from ElectricCar import ElectricCar

@pytest.mark.parametrize('value,expected',([
    (5,7.5),
    (10,10),
    (100,55)
]))

def test_calculate_trip_cost(vehicle,value,expected):
    assert vehicle.calculate_trip_cost(value) == expected
