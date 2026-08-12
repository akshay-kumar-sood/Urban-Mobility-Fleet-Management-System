import pytest
from ElectricCar import ElectricCar


@pytest.mark.parametrize('value,expected',[
    (100,100),(0,0),(90,90)])


# valid testcases - percentage
def test_percentage_valid_cases(vehicle,value,expected):
    vehicle.battery_percentage=value
    assert vehicle.battery_percentage==expected


# boundary test cases - percentage
@pytest.mark.parametrize('battery',[
    -1,101
])

def test_percentage_invalid_cases(battery):
    with pytest.raises(ValueError):
        ElectricCar(101,"T66",battery,9)

# test casing for maintenance status method

@pytest.mark.parametrize('value,expected',[
    ("Available","Available"),
    ("On Trip","On Trip"),
    ("Under Maintenance","Under Maintenance")
])

def test_maintenance_status(vehicle,value,expected):
    vehicle.maintenance_status=value
    assert vehicle.maintenance_status==expected







