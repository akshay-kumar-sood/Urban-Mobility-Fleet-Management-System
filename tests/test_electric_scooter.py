import pytest
from ElectricScooter import ElectricScooter

@pytest.mark.parametrize('actual,excepted',([
    (60,10),
    (90,14.5),
    (600,91)
]))

def test_calculate_trip_cost(scooter,actual,excepted):
    assert scooter.calculate_trip_cost(actual)==excepted
