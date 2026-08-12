import pytest 
from Fleet import Fleet
from hub import Hub
import csv

def test_add_hub(fleet1,hub):
    fleet1.add_hub(hub)

    assert len(fleet1.hubs)==1

def test_duplicate_hub(fleet1,hub):
    fleet1.add_hub(hub)

    with pytest.raises(ValueError):
        fleet1.add_hub(hub)


def test_search_hub(fleet1,hub,vehicle1,capsys,monkeypatch):

    fleet1.add_hub(hub)
    hub.add_vehicle(vehicle1)
    monkeypatch.setattr("builtins.input",lambda _:"Airport")
    fleet1.search_hub()

    captured=capsys.readouterr()

    assert "Airport" in captured.out


def test_percentage_search(fleet1,hub,vehicle1,vehicle2,capsys,monkeypatch):

    fleet1.add_hub(hub)
    hub.add_vehicle(vehicle1)
    hub.add_vehicle(vehicle2)

    monkeypatch.setattr("builtins.input",lambda _:"Airport")
    fleet1.percentage_search()

    captured=capsys.readouterr()
    print(captured.out)

    assert "109" in captured.out
    assert "105" not in captured.out


def test_vehicle_status_cnt(hub,vehicle1,vehicle2,vehicle3,vehicle4,capsys):

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


def test_save_csv(fleet1, hub, vehicle1, vehicle2, tmp_path):
    fleet1.add_hub(hub)
    hub.add_vehicle(vehicle1)
    hub.add_vehicle(vehicle2)

    file = tmp_path / "test_fleet.csv"

    fleet1.save_csv(file)

    assert file.exists()

    with open(file) as f:
        content=f.read()

    assert "hub_name" in content
    assert "vehicle_id" in content
    assert str(vehicle1.vehicle_id) in content
    assert str(vehicle2.vehicle_id) in content


def test_load_csv(fleet1, hub, vehicle1, vehicle2, tmp_path):
    fleet1.add_hub(hub)
    hub.add_vehicle(vehicle1)
    hub.add_vehicle(vehicle2)

    file = tmp_path / "test_fleet.csv"

    fleet1.save_csv(file)

    new_fleet = Fleet([])
    new_fleet.load_csv(file)

    assert len(new_fleet.hubs) == 1
    assert len(new_fleet.hubs[0].vehicles) == 2
    assert new_fleet.hubs[0].vehicles[0].vehicle_id == vehicle1.vehicle_id
    assert new_fleet.hubs[0].vehicles[1].vehicle_id == vehicle2.vehicle_id


def test_save_json(fleet1, hub, vehicle1, vehicle2, tmp_path):
    fleet1.add_hub(hub)
    hub.add_vehicle(vehicle1)
    hub.add_vehicle(vehicle2)

    file = tmp_path / "test_fleet.json"

    fleet1.save_json(file)

    assert file.exists()

    
    with open(file) as f:
        content=f.read()

    assert "Airport" in content
    assert str(vehicle1.vehicle_id) in content
    assert str(vehicle2.vehicle_id) in content


def test_load_json(fleet1, hub, vehicle1, vehicle2, tmp_path):
    fleet1.add_hub(hub)
    hub.add_vehicle(vehicle1)
    hub.add_vehicle(vehicle2)

    file = tmp_path / "test_fleet.json"

    fleet1.save_json(file)

    new_fleet = Fleet([])
    new_fleet.load_json(file)

    assert len(new_fleet.hubs) == 1
    assert len(new_fleet.hubs[0].vehicles) == 2

    assert new_fleet.hubs[0].vehicles[0].vehicle_id == vehicle1.vehicle_id
    assert new_fleet.hubs[0].vehicles[1].vehicle_id == vehicle2.vehicle_id







