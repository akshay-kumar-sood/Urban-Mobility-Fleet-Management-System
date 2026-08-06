class Fleet:

    def __init__(self):
        self.hubs=[]

    def add_hub(self,hub):
        for existing_hub in self.hubs:

            if existing_hub.hub_name == hub.hub_name:
                raise ValueError(f"Hub named {hub.hub_name} already exists.")

        self.hubs.append(hub)


    def get_hub(self,hub_name):
        for hub in self.hubs:
            if hub.hub_name == hub_name:
                return hub

        raise ValueError(f"Hub '{hub_name}' does not exist. Please add it first.")   