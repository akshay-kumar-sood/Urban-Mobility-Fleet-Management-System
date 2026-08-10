from dataclasses import dataclass,field
from hub import Hub
from ElectricCar import ElectricCar
from ElectricScooter import ElectricScooter
import csv

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



        

        
