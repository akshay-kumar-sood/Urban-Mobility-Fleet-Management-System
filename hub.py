class FleetHub:
    def __init__(self):
        self.hubs={}

    def new_hub(self,hub):
        if hub not in self.hubs:
            self.hubs[hub]=[] 
        else:
            raise Exception("Hub Already Exists")
            # print("Hub Already Exists. ")

    def add_vehicle(self,hub,vehicle):
        if hub in self.hubs:
            existed_list=[x for x in self.hubs[hub] if x==vehicle]

            if existed_list:
                raise Exception("Vehicle with same vehicle id already exists.")
                #print("Vehicle with same vehicle id already exists.")
            else:
                self.hubs[hub].append(vehicle)
        else:
            raise Exception("Hub not exists")
            #print("Hub not exists")
            

    