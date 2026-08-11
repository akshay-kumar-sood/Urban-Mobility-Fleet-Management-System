from ElectricCar import ElectricCar
from ElectricScooter import ElectricScooter
from hub import Hub
from Fleet import Fleet

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


print("-" *60)
print("Testing UC6 Hub and Fleet Class")
print("-" *60)

fleet=Fleet()

while True:

    print(f"\n====== ECO RIDE ======")
    print(f"1. Add Hub ")
    print(f"2. Add Vehicle ")
    print(f"3. Display HUb Vehicles ")
    print("4. Exit ")

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
            continue

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
                print(f"Battery    : {vehicle.get_battery_percentage()}%")

    elif choice == 4:

        print("Signing Off - AKSHAY KUMAR SOOD")
        break

    else:

        print("Invalid Choice")

print("-"*60)





        

