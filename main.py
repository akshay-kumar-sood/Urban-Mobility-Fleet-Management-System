from ElectricCar import ElectricCar
from ElectricScooter import ElectricScooter
from hub import FleetHub

tesla=ElectricCar(1051,"T202",86,8)
ola=ElectricScooter(1235,"S306",20,120)

print(f"Tesla Battery Percentage : {tesla.get_battery_percentage()}")
print(f"Ola Battery Percentage : {ola.get_battery_percentage()}")

vehicle_list=[tesla,ola]

for ele in vehicle_list:
    if isinstance(ele,ElectricCar):
        print(f"Model is : {ele.model} and Fare is : {ele.calculate_trip_cost(20)}")

    else:
        print(f"Model is : {ele.model} and Fare is : {ele.calculate_trip_cost(60)}")


Fleet1=FleetHub()
Fleet1.new_hub("Airport")
Fleet1.new_hub("Bus-Stand")

print(Fleet1.hubs)

Fleet1.add_vehicle("Airport",tesla)
Fleet1.add_vehicle("Bus-Stand",ola)

print(Fleet1.hubs)

print("----testing uc7------")

tesla1=ElectricCar(1054,"T202",86,8)
tesla2=ElectricCar(1054,"T209",40,8)

Fleet1.add_vehicle("Airport",tesla1)
Fleet1.add_vehicle("Airport",tesla2)

print(Fleet1.hubs)

