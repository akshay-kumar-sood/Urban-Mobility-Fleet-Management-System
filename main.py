from ElectricCar import ElectricCar
from ElectricScooter import ElectricScooter
from hub import Hub
from Fleet import Fleet

tesla=ElectricCar(1051,"T202",86,8)
ola=ElectricScooter(1235,"S306",20,120)

print(f"Tesla Battery Percentage : {tesla.battery_percentage}")
print(f"Ola Battery Percentage   : {ola.battery_percentage}")

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

    print("\n====== ECO RIDE ======")
    print("1.  Add Hub ")
    print("2.  Add Vehicle ")
    print("3.  Display HUb Vehicles ")
    print("4.  Categorized View")
    print("5.  Vehicle status Count ")
    print("6.  Sort Vehicles ")
    print("7.  Save Fleet to CSV")
    print("8.  Load Fleet from CSV")
    print("9.  Save Fleet to JSON")
    print("10. Load Fleet from JSON")
    print("11. Exit ")
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


        status_map ={
            1: "Available",
            2: "On Trip",
            3: "Under Maintenance"
        }

        car_status =int(input("Maintenance Status (1-Available, 2 -On Trip, 3- Under Maintenance) : "))

        if car_status not in status_map:
            raise ValueError("Incorrect Maintenance Status")
        
        
        if vehicle_choice == 1:

            seating = int(input("Seating Capacity : "))
            
            vehicle = ElectricCar(
                vehicle_id,
                model,
                battery,
                seating
            )

            distance = float(input("Enter Trip Distance (KM): "))
            vehicle.rental_price = vehicle.calculate_trip_cost(distance)
            vehicle.maintenance_status = status_map[car_status]

        elif vehicle_choice == 2:

            speed = int(input("Max Speed Limit : "))

            vehicle = ElectricScooter(
                vehicle_id,
                model,
                battery,
                speed
            )

            minutes = float(input("Enter Trip Duration (Minutes): "))
            vehicle.rental_price = vehicle.calculate_trip_cost(minutes)
            vehicle.maintenance_status = status_map[car_status]

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
        fleet.sorting()

    elif choice == 7:
        fleet.save_csv()
        print("Data Saved Successfully", flush=True)

    elif choice == 8:
        fleet.load_csv()
        print("Fleet data loaded from CSV successfully.")

        for hub in fleet.hubs:
            print(f"\nHub : {hub.hub_name}")

            for vehicle in hub.vehicles:
                print(vehicle)

    elif choice == 9:
        fleet.save_json()
        print("Fleet data loaded from JSON successfully.")


    elif choice == 10:
        fleet.load_json()
        print("Fleet data loaded from JSON successfully.")

        for hub in fleet.hubs:
            print(f"\nHub : {hub.hub_name}")

        for vehicle in hub.vehicles:
            print(vehicle)

    elif choice == 11:
        print("Signing Off - AKSHAY KUMAR SOOD")
        break

    else:
        print("Invalid Choice")


print("-"*60)







        
