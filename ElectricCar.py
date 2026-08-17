from dataclasses import dataclass
from Vehicle import Vehicle

@dataclass
class ElectricCar(Vehicle):

    seating_capacity: int

    def calculate_trip_cost(self, distance):
        return 5 + (distance * 0.50)

