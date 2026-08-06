class Hub:

    def __init__(self,hub_name):
        self.hub_name=hub_name
        self.vehicles=[]

    def add_vehicle(self,vehicle):

        existing_vehicles=[v for v in self.vehicles if vehicle==v]

        if existing_vehicles:
            raise ValueError(f"Vehicle ID {vehicle.vehicle_id} already exists in {self.hub_name}")

        self.vehicles.append(vehicle)

    

