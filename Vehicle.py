from abc import ABC,abstractmethod
from dataclasses import dataclass,field

@dataclass
class Vehicle(ABC):

    vehicle_id:int
    model:str
    _battery_percentage:float
    __maintenance_status:str = field(default="Available",init=False, repr=False)
    __rental_price: float = field(default=0,init=False,repr=False)

    def __post_init__(self) -> None:
        self.battery_percentage=self._battery_percentage

    @property
    def battery_percentage(self) -> float:
        return self._battery_percentage

    @battery_percentage.setter
    def battery_percentage(self,value:float) -> None:

        if not 0 <= value <=100:
            raise ValueError("Battery Percentage must be between 0 and 100 ")

        self._battery_percentage=value

    @property
    def maintenance_status(self) -> str:
        return self.__maintenance_status
    

    @maintenance_status.setter
    def maintenance_status(self,value:str) -> None:

        trusted_status=[
            "Available",
            "On Trip",
            "Under Maintenance"
        ]

        if value not in trusted_status:
            raise ValueError(f"Incorrect status. choose (Available / ON Trip / Under Maintenance) ")
        
        self.__maintenance_status=value


    @property
    def rental_price(self) -> float:
        return self.__rental_price
    

    @rental_price.setter
    def rental_price(self,value:float) -> None:
        self.__rental_price = value


    @abstractmethod
    def calculate_trip_cost(self,distance:float) -> float:
        pass


    def __eq__(self,other:object) -> bool:

        if isinstance(other,Vehicle):
            return self.vehicle_id == other.vehicle_id

        return False

    def __str__(self) -> str:

        return (    
        f"-------------------------------------------------"
        f"\n"
        f"Vehicle Type       : {type(self).__name__}\n"
        f"Vehicle ID         : {self.vehicle_id}\n"
        f"Vehicle Model      : {self.model}\n"
        f"Battery Percentage : {self.battery_percentage}%\n"
        f"Maintenance Status : {self.maintenance_status}"
        f"\n"
        f"-------------------------------------------------"
        )