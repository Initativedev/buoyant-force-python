import math

def calculate_buoyant_force(density_object, volume_object, density_fluid):
    return (density_fluid * volume_object * 9.8) - (density_object * volume_object * 9.8)

density_object = float(input("Enter the density of the object in kg/m^3: "))
volume_object = float(input("Enter the volume of the object in m^3: "))
density_fluid = float(input("Enter the density of the fluid in kg/m^3: "))

buoyant_force = calculate_buoyant_force(density_object, volume_object, density_fluid)
print("The buoyant force acting on the object is", buoyant_force, "N.")
