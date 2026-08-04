from Vehicle import Vehicle

v1 = Vehicle(
    1051,
    "Tesla Model 3",
    90,
    "Available",
    250000
)

print(f"Vehicle ID               : {v1.vehicle_id}")
print(f"Vehicle Model            : {v1.model}")
print(f"Battery Percentage       : {v1.get_battery_percentage()} %")
print(f"Maintenance Status       : {v1.get_maintenance_status()}")
print(f"Rental Price             : ₹{v1.get_rental_price()}")

print("\nAfter Updating Data\n")

v1.set_battery_percentage(80)
v1.set_maintenance_status("Under Maintenance")
v1.set_rental_price(350000)

print(f"Vehicle ID               : {v1.vehicle_id}")
print(f"Vehicle Model            : {v1.model}")
print(f"Battery Percentage       : {v1.get_battery_percentage()} %")
print(f"Maintenance Status       : {v1.get_maintenance_status()}")
print(f"Rental Price             : ₹{v1.get_rental_price()}")