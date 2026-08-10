from dataclasses import dataclass,field
from hub import Hub
from ElectricCar import ElectricCar
from ElectricScooter import ElectricScooter
import csv
import json

@dataclass
class Fleet:

    hubs:list[Hub] = field(default_factory=list)

    def add_hub(self, hub:Hub) -> None:

        for existing_hub in self.hubs:

            if existing_hub.hub_name == hub.hub_name:
                raise ValueError(f"Hub named {hub.hub_name} already exists.")

        self.hubs.append(hub)


    def get_hub(self,hub_name:str) -> Hub:

        for hub in self.hubs:
            
            if hub.hub_name == hub_name:
                return hub

        raise ValueError(f"Hub '{hub_name}' does not exist. Please add it first.")   


    def search_hub(self) -> None:
        hub_name=input("Enter Hub name : ")
        hub=self.get_hub(hub_name)
        hub.display_vehicle()


    def percentage_search(self) -> None:
        hub_name=input("Enter Hub name : ")
        hub=self.get_hub(hub_name)
        hub.percentage_gt_80()


    def categorized_search(self) -> None:
        hub_name = input("Enter Hub Name : ")
        hub=self.get_hub(hub_name)
        hub.categorized_view()

    def vehicle_status_cnt(self) -> None:
        hub_name = input("Enter Hub Name : ")
        hub=self.get_hub(hub_name)
        hub.status_count()

    # def sort_vehicle(self) -> None:
    #     hub_name = input("Enter Hub Name : ")
    #     hub = self.get_hub(hub_name)
    #     hub.sort_vehicle_model()

    def sorting(self) -> None:
        hub_name = input("Enter Hub Name : ")
        hub = self.get_hub(hub_name)
        hub.sorting()



    def save_csv(self, filename="fleet.csv"):

        print("Saving fleet data...")

        with open(filename, "w", newline="") as file:

            writer = csv.writer(file)

            writer.writerow([
                "hub_name",
                "vehicle_type",
                "vehicle_id",
                "model",
                "battery_percentage",
                "maintenance_status",
                "rental_price",
                "extra"
            ])

            for hub in self.hubs:

                for vehicle in hub.vehicles:

                    if isinstance(vehicle, ElectricCar):
                        extra = vehicle.seating_capacity

                    elif isinstance(vehicle, ElectricScooter):
                        extra = vehicle.max_speed_limit

                    else:
                        raise ValueError("Unknown vehicle type")

                    writer.writerow([
                        hub.hub_name,
                        type(vehicle).__name__,
                        vehicle.vehicle_id,
                        vehicle.model,
                        vehicle.battery_percentage,
                        vehicle.maintenance_status,
                        vehicle.rental_price,
                        extra
                    ])

        print("CSV file written successfully.")



        
    def load_csv(self, filename="fleet.csv"):

        self.hubs.clear()

        with open(filename, "r", newline="") as file:

            reader = csv.DictReader(file)

            for row in reader:

                hub_name = row["hub_name"]

                try:
                    hub = self.get_hub(hub_name)

                except ValueError:
                    hub = Hub(hub_name)
                    self.add_hub(hub)

                if row["vehicle_type"] == "ElectricCar":

                    vehicle = ElectricCar(
                        int(row["vehicle_id"]),
                        row["model"],
                        float(row["battery_percentage"]),
                        int(row["extra"])
                    )

                elif row["vehicle_type"] == "ElectricScooter":

                    vehicle = ElectricScooter(
                        int(row["vehicle_id"]),
                        row["model"],
                        float(row["battery_percentage"]),
                        int(row["extra"])
                    )

                vehicle.maintenance_status = row["maintenance_status"]
                vehicle.rental_price = float(row["rental_price"])

                hub.add_vehicle(vehicle)


    def save_json(self, filename="fleet.json"):

        data = []

        for hub in self.hubs:

            hub_data = {
                "hub_name": hub.hub_name,
                "vehicles": []
            }

            for vehicle in hub.vehicles:

                vehicle_data = {
                    "vehicle_type": type(vehicle).__name__,
                    "vehicle_id": vehicle.vehicle_id,
                    "model": vehicle.model,
                    "battery_percentage": vehicle.battery_percentage,
                    "maintenance_status": vehicle.maintenance_status,
                    "rental_price": vehicle.rental_price
                }

                if isinstance(vehicle, ElectricCar):
                    vehicle_data["seating_capacity"] = vehicle.seating_capacity

                elif isinstance(vehicle, ElectricScooter):
                    vehicle_data["max_speed_limit"] = vehicle.max_speed_limit

                hub_data["vehicles"].append(vehicle_data)

            data.append(hub_data)

        with open(filename, "w") as file:
            json.dump(data, file, indent=4)


    def load_json(self, filename="fleet.json"):

        self.hubs.clear()

        with open(filename, "r") as file:
            data = json.load(file)

        for hub_data in data:

            hub = Hub(hub_data["hub_name"])

            for vehicle_data in hub_data["vehicles"]:

                if vehicle_data["vehicle_type"] == "ElectricCar":

                    vehicle = ElectricCar(
                        int(vehicle_data["vehicle_id"]),
                        vehicle_data["model"],
                        float(vehicle_data["battery_percentage"]),
                        int(vehicle_data["seating_capacity"])
                    )

                elif vehicle_data["vehicle_type"] == "ElectricScooter":

                    vehicle = ElectricScooter(
                        int(vehicle_data["vehicle_id"]),
                        vehicle_data["model"],
                        float(vehicle_data["battery_percentage"]),
                        int(vehicle_data["max_speed_limit"])
                    )

                else:
                    continue

                vehicle.maintenance_status = vehicle_data["maintenance_status"]
                vehicle.rental_price = float(vehicle_data["rental_price"])

                hub.add_vehicle(vehicle)

            self.add_hub(hub)


        

        
