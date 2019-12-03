def fuel_from_mass(mass):
    fuel = int(mass/3) - 2
    return fuel

def fuel_from_fuelmass(mass):
    fuel = fuel_from_mass(mass)
    if fuel < 0:
        return 0
    else:
        fuelmass = fuel_from_mass(mass)
        return fuel + fuel_from_fuelmass(fuelmass)

# Part 1
inputs = [int(input.rstrip('\n')) for input in open('input.txt')]
fuel = []

for i in inputs:
    fuel.append(fuel_from_mass(i))

print(f"Part 1 Sum: {sum(fuel)}")

# Part 2 
fuel = []

for i in inputs:
    fuel.append(fuel_from_fuelmass(i))

print(f"Part 2 Sum: {sum(fuel)}")