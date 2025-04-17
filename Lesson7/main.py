import Car
import ElectricCar



def main():
    my_leaf = ElectricCar("Nissan","Leaf",2024,60)
    print(my_leaf.battery_capacity)
    print(my_leaf.make)
    print(my_leaf.battery_charge)
    my_leaf.fill_gas_tank(0.6)
    print(my_leaf.battery_charge)
    my_leaf.charge_car(0.3)
    print(my_leaf.battery_charge)
    print(my_leaf.year)
    my_leaf.battery_charge = 0.2
    
if __name__ == '__main__':
    main()