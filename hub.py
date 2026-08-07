from dataclasses import dataclass,field
from Vehicle import Vehicle
from collections import defaultdict

@dataclass
class Hub:

    hub_name: str
    vehicles: list[Vehicle] = field(default_factory=list)

    def add_vehicle(self,vehicle: Vehicle) -> None:

        existing_vehicles=[v for v in self.vehicles if vehicle==v]

        if existing_vehicles:
            raise ValueError(f"Vehicle ID {vehicle.vehicle_id} already exists in {self.hub_name}")

        self.vehicles.append(vehicle)

    def display_vehicle(self) -> None:

        if not self.vehicles:
            raise ValueError(f"No vehicle Found in {self.hub_name} hub.")

        else:
            print()
            print(f"=" * 60)
            print(f"Vehicles Available in Hub : {self.hub_name}")
            print(f"=" * 60)
            print()
            print("-" * 60)

            for v in self.vehicles:
                print(f"Vehicle Type         : {type(v).__name__}")
                print(f"Vehicle id           : {v.vehicle_id}")
                print(f"Vehicle model        : {v.model}")
                print(f"Battery percentage   : {v.battery_percentage}")
                print("-"*60)

    def percentage_gt_80(self):
        if not self.vehicles:
            raise ValueError(f"No vehicle Found in {self.hub_name} hub.")

        vehicles_list=list(filter(lambda vehicle:vehicle.battery_percentage>80,self.vehicles))

        if not vehicles_list:
            raise ValueError(f"No vehicle have battery percentage greater than 80 in Hub : {self.hub_name}")

        for v in vehicles_list:
            print(f"Vehicle Type         : {type(v).__name__}")
            print(f"Vehicle id           : {v.vehicle_id}")
            print(f"Vehicle model        : {v.model}")
            print(f"Battery percentage   : {v.battery_percentage}")
            print("-"*60)


    def categorized_view(self) -> None:

        if not self.vehicles:
            raise ValueError(f"No vehicle found in {self.hub_name} hub.")

        vehicle_map=defaultdict(list)

        for vehicle in self.vehicles:
            vehicle_type=type(vehicle).__name__
            vehicle_map[vehicle_type].append(vehicle)

        print()
        print("=" * 60)
        print(f"Categorized Vehicle in Hub : {self.hub_name}")
        print("=" * 60)

        for vehicle_type,vehicle_list in vehicle_map.items():

            print()
            print("=" * 12)
            print(f"{vehicle_type}")
            print("=" * 12)

            for vehicle in vehicle_list:

                print("-"*60)
                print(f"Vehicle Id          :  {vehicle.vehicle_id}")
                print(f"Model               :  {vehicle.model}")
                print(f"Battery Percentage  :  {vehicle.battery_percentage}%")

                if vehicle_type == "ElectricCar":
                    print(f"Seating Capacity    :  {vehicle.seating_capacity}")

                elif vehicle_type == "ElectricScooter":
                    print(f"Max Speed Limit :{vehicle.max_speed_limit} %")

                print("-"*60)


   