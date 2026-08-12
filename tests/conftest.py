import pytest
from ElectricCar import ElectricCar
from ElectricScooter import ElectricScooter
from hub import Hub
from Fleet import Fleet


@pytest.fixture 
def vehicle():
    return ElectricCar(101,"T1",80,8)

@pytest.fixture
def scooter():
    return ElectricScooter(102,"T2",90,9)

@pytest.fixture
def hub():
    return Hub("Airport",[])


@pytest.fixture 
def vehicle1():
    return ElectricCar(109,"T4",89,8)


@pytest.fixture 
def vehicle2():
    return ElectricCar(105,"T8",70,8)


@pytest.fixture 
def vehicle3():
    return ElectricCar(106,"T9",91,10)


@pytest.fixture 
def vehicle4():
    return ElectricCar(107,"T10",78,6)


@pytest.fixture
def hub1():
    return hub("Airport",[vehicle1,vehicle2])


@pytest.fixture
def hub2():
    return hub("BusStand",[vehicle3,vehicle4])


@pytest.fixture
def fleet1():
    return Fleet([])


@pytest.fixture
def fleet2():
    return Fleet([hub1])

