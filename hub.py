class Hub:

    def __init__(self,hub_name):
        self.hub_name=hub_name
        self.vehicles=[]

    def add_vehicle(self,vehicle):

        existing_vehicles=[v for v in self.vehicles if vehicle==v]

        if existing_vehicles:
            raise ValueError(f"Vehicle ID {vehicle.vehicle_id} already exists in {self.hub_name}")

        self.vehicles.append(vehicle)

    def display_vehicle(self):

        if not self.vehicles:
            raise ValueError(f"No vehicle Found in {self.hub_name} hub.")

        else:
            print()
            print(f"="*60)
            print(f"Vehicles Available in Hub : {self.hub_name}")
            print(f"="*60)
            print()
            print("-"*60)

            for v in self.vehicles:
                print(f"Vehicle Type         : {type(v).__name__}")
                print(f"Vehicle id           : {v.vehicle_id}")
                print(f"Vehicle model        : {v.model}")
                print(f"Battery percentage   : {v.battery_percentage}")
                print("-"*60)

    def percentage_gt_80(self):
        if not self.vehicles:
            raise ValueError(f"No vehicle Found in {self.hub_name} hub.")

        vehicles_list=list(filter(lambda vehicle:vehicle.get_battery_percentage()>80,self.vehicles))

        if not vehicles_list:
            raise ValueError(f"No vehicle have battery percentage greater than 80 in Hub : {self.hub_name}")

        for v in vehicles_list:
            print(f"Vehicle Type         : {type(v).__name__}")
            print(f"Vehicle id           : {v.vehicle_id}")
            print(f"Vehicle model        : {v.model}")
            print(f"Battery percentage   : {v.battery_percentage}")
            print("-"*60)
        

        


    

