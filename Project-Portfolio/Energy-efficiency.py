def calculate_energy_efficiency(energy_consumption, building_area):
    energy_efficiency = energy_consumption / building_area
    return energy_efficiency
    """ Given parameters available are only energy consumption and building area """

def main():
    energy_consumption = float(input("Enter the total energy consumption (in kWh): "))
    building_area = float(input("Enter the building area (in square meters): "))
    """ Building area parameter is to be calculated in meter squared """
    
    energy_efficiency = calculate_energy_efficiency(energy_consumption, building_area)
    
    print(f"The energy efficiency of the building is {energy_efficiency:.2f} kWh/sq.m.")

if _name_ == "_main_":
    main()
