def calculate_heat_load(area, insulation_factor, occupancy, equipment, temperature_difference):
    heat_loss = area * insulation_factor * temperature_difference
    total_heat_load = heat_loss + occupancy + equipment
    return total_heat_load

def main():
    building_area = float(input("Enter the building area (in square meters): "))
    insulation_factor = float(input("Enter the insulation factor: "))
    occupancy_load = float(input("Enter the occupancy load (in Watts): "))
    equipment_load = float(input("Enter the equipment load (in Watts): "))
    temperature_difference = float(input("Enter the temperature difference (in Celsius): "))
    
    heat_load = calculate_heat_load(building_area, insulation_factor, occupancy_load, equipment_load, temperature_difference)
    
    print(f"The total heat load of the building is {heat_load} Watts.")

if _name_ == "_main_":
    main()
