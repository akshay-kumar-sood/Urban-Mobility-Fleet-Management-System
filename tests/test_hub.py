import pytest
from hub import Hub


def test_add_vehicle(hub, vehicle):
    hub.add_vehicle(vehicle)

    assert len(hub.vehicles) == 1
    assert hub.vehicles[0] == vehicle


def test_duplicate_vehicle(hub, vehicle):
    hub.add_vehicle(vehicle)

    with pytest.raises(ValueError):
        hub.add_vehicle(vehicle)


def test_percentage_gt_80(hub,vehicle,capsys):
    vehicle.battery_percentage=90
    hub.add_vehicle(vehicle)

    hub.percentage_gt_80()
    captured=capsys.readouterr()

    assert "101" in captured.out


def test_sorting_battery(hub, vehicle1, vehicle2, capsys, monkeypatch):
    hub.add_vehicle(vehicle1)
    hub.add_vehicle(vehicle2)

    monkeypatch.setattr("builtins.input", lambda x: "1")

    hub.sorting()

    captured = capsys.readouterr()

    assert captured.out.index(str(vehicle1)) < captured.out.index(str(vehicle2))


def test_sorting_rental_price(hub,vehicle1,vehicle2,capsys,monkeypatch):
    vehicle1.rental_price=50000
    vehicle2.rental_price=60000

    hub.add_vehicle(vehicle1)
    hub.add_vehicle(vehicle2)

    monkeypatch.setattr("builtins.input",lambda x:"2")

    hub.sorting()
    captured=capsys.readouterr()

    assert captured.out.index(str(vehicle1)) > captured.out.index(str(vehicle2))


def test_sorting_vehicle_model(hub,vehicle1,vehicle2,capsys,monkeypatch):
    hub.add_vehicle(vehicle1)
    hub.add_vehicle(vehicle2)

    monkeypatch.setattr('builtins.input',lambda x:'3')
    hub.sorting()

    captured=capsys.readouterr()

    assert "T4" in captured.out
    assert "T8" in captured.out
    assert captured.out.index("T4") < captured.out.index("T8")


def test_status_count(hub,vehicle1,vehicle2,vehicle3,vehicle4,capsys):

    vehicle1.maintenance_status="Available"
    vehicle2.maintenance_status="On Trip"
    vehicle3.maintenance_status="Available"
    vehicle4.maintenance_status="Under Maintenance"

    hub.add_vehicle(vehicle1)
    hub.add_vehicle(vehicle2)
    hub.add_vehicle(vehicle3)
    hub.add_vehicle(vehicle4)

    hub.status_count()

    captured=capsys.readouterr()

    assert "Available status : 2" in captured.out
    assert "On Trip :1" in captured.out
    assert "under Miantennance are : 1" in captured.out


    




