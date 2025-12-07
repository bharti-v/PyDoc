# Transportation Mode Selection
# Problem: Choose a mode of transportation based on the distance (e.g., <3 km: Walk, 3-15 km: Bike, >15 km: Car).

distance = 16

if distance < 3:
    transport = "Walk"
if distance <= 15:
    transport = "Bike"
# if distance >15:
else:
    transport = "Car"

print(transport)