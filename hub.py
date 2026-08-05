class FleetHub:
    def __init__(self):
        self.hubs={}

    def new_hub(self,hub):
        if hub not in self.hubs:
            self.hubs[hub]=[] 
        else:
            raise Exception("Hub Already Exists. ")

    def add_vehicle(self,hub,vehicle):
        if hub in self.hubs:
            self.hubs[hub].append(vehicle)
        else:
            raise Exception("Hub not exists")

    