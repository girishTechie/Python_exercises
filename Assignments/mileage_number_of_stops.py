total_distance = 560
tank_capacity = int(input("enter the total tank capacity? "))
utilized_fuel = int(input("enter the total utilized fuel? "))
milage = total_distance / utilized_fuel
one_time_fuel_mileage = tank_capacity * milage
number_of_stops = total_distance / one_time_fuel_mileage
print(number_of_stops)
