from ElectricCar import ElectricCar
from ElectricScooter import ElectricScooter
from hub import Hub
from Fleet import Fleet

tesla=ElectricCar(1051,"T202",86,8)
ola=ElectricScooter(1235,"S306",20,120)

print(f"Tesla Battery Percentage : {tesla.battery_percentage}")
print(f"Ola Battery Percentage : {ola.battery_percentage}")

vehicle_list=[tesla,ola]

for ele in vehicle_list:
    if isinstance(ele,ElectricCar):
        print(f"Model is : {ele.model} and Fare is : {ele.calculate_trip_cost(20)}")

    else:
        print(f"Model is : {ele.model} and Fare is : {ele.calculate_trip_cost(60)}")


print("-" *60)
print("Testing UC6 Hub and Fleet Class")
print("-" *60)

fleet=Fleet()

while True:

    print(f"\n====== ECO RIDE ======")
    print(f"1. Add Hub ")
    print(f"2. Add Vehicle ")
    print(f"3. Display HUb Vehicles ")
    print(f"4. Categorized View")
    print(f"5. Exit ")
    print()
    choice = int(input("Enter Choice : "))

    if choice == 1:

        hub_name = input("Enter Hub Name : ")

        fleet.add_hub(Hub(hub_name))

        print("Hub Added Successfully.")

    elif choice == 2:

        hub_name = input("Enter Hub Name : ")

        hub = fleet.get_hub(hub_name)

        print("\n1. Electric Car")
        print("2. Electric Scooter")

        vehicle_choice = int(input("Enter Vehicle Type : "))

        vehicle_id = int(input("Vehicle ID : "))
        model = input("Model : ")
        battery = float(input("Battery Percentage : "))

        
        if vehicle_choice == 1:

            seating = int(input("Seating Capacity : "))
            
            vehicle = ElectricCar(
                vehicle_id,
                model,
                battery,
                seating
            )


        elif vehicle_choice == 2:

            speed = int(input("Max Speed Limit : "))

            vehicle = ElectricScooter(
                vehicle_id,
                model,
                battery,
                speed
            )


        else:
            raise ValueError("Invalid Vehicle Type")
            


        hub.add_vehicle(vehicle)

        print("Vehicle Added Successfully.")

    elif choice == 3:

        hub_name = input("Enter Hub Name : ")

        hub = fleet.get_hub(hub_name)

        print(f"\nHub : {hub.hub_name}")

        if not hub.vehicles:
            print("No Vehicles Found.")
        else:

            for vehicle in hub.vehicles:

                print("----------------------------")
                print(f"Vehicle ID : {vehicle.vehicle_id}")
                print(f"Model      : {vehicle.model}")
                print(f"Battery    : {vehicle.battery_percentage}%")

    elif choice == 4:

        fleet.categorized_search()

    elif choice == 5:
        fleet.vehicle_status_cnt()

    elif choice == 6:

        print("Signing Off - AKSHAY KUMAR SOOD")
        break



    else:

        print("Invalid Choice")


print("-"*60)



print("="*60)
print("Testing UC7 - Validation on same vehicle id")
print("="*60)

old_tesla=ElectricCar(1098,"A2026",90,5)
new_tesla=ElectricCar(1097,"A2027",80,8)

airport=Hub("airport")
airport.add_vehicle(old_tesla)
airport.add_vehicle(new_tesla)



fleet3=Fleet()
hub3=Hub("Airport")
omni=ElectricCar(1051,"A102",83,8)
jeep=ElectricScooter(1045,"A345",89,120)
hub3.add_vehicle(omni)
hub3.add_vehicle(jeep)

fleet3.add_hub(hub3)
print("="*60)
print("Testing UC8 - Search Functionality - Display Vehicles in a Hub")
print("="*60)
fleet3.search_hub()

print("="*60)
print("Testing UC8 - Search Functionality - Filter on basic of battery percentage>80")
print("="*60)
fleet3.percentage_search()


        
