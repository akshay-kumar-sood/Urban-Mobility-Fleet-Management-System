from dataclasses import dataclass
from Vehicle import Vehicle

@dataclass
class ElectricScooter(Vehicle):

    max_speed_limit: int

    def calculate_trip_cost(self, minutes):
        return 1 + (0.15 * minutes)

