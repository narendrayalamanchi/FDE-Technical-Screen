def sort(width, height, length, mass):
    # Calculate volume
    volume = width*height*length
    # Determine if the package is bulky or heavy
    is_bulky = volume >= 1000000 or width >= 150 or  height >= 150 or  length >= 150
    is_heavy = mass >= 20
    # Determine the category based on bulkiness and heaviness
    if is_heavy and is_bulky:
        return "REJECTED"
    elif is_heavy or is_bulky:
        return "SPECIAL"
    else:
        return "STANDARD"

# One of the dimension is above 150cm and the mass is below 20. So, it should be Special 
print(sort(200, 50, 50, 10))
# The volume is 1000000 and the mass is above. If both are above it should be rejected.
print(sort(100, 100, 100, 25))
# The volume is below 1000000 and the mass is below 20. If both are below it should be Standard.
print(sort(30, 30, 30, 5))
