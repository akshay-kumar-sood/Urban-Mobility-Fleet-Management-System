from dataclasses import dataclass,field
from hub import Hub

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

    def sort_vehicle(self) -> None:
        hub_name = input("Enter Hub Name : ")
        hub = self.get_hub(hub_name)
        hub.sort_vehicle_model()

    
