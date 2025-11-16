# Day 2 - Numbers Tasks

print("\n=== Task 1: format(145, 'o') ===")

# Task 1: Use format() with 'o' (octal)
num = 145
formatted_val = format(num, 'o')   # 'o' = octal representation
print("145 in octal format =", formatted_val)
print("Data type:", type(formatted_val))

print("\n=== Task 2: Area of pond + water amount ===")

# Task 2: Circular pond calculations
radius = 84
pi = 3.14

pond_area = pi * (radius ** 2)
print("Area of the pond =", pond_area)

# Bonus: Water calculation (1.4 liters per square meter)
water_per_sq_meter = 1.4
total_water = pond_area * water_per_sq_meter

# Print without decimal point → use int()
print("Total water in liters (no decimal) =", int(total_water))

print("\n=== Task 3: Speed calculation ===")

# Task 3: Speed in m/s
distance = 490  # meters
time_minutes = 7
time_seconds = time_minutes * 60  # convert minutes → seconds

speed = distance / time_seconds
print("Speed in m/s (no decimal) =", int(speed))