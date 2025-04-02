import Car
import ElectricCar

def main():
    my_leaf = ElectricCar.ElectricCar("Nissan","Leaf",2024,60)
    print(my_leaf.battery_level)
    print(my_leaf.make)
    

if __name__ == '__main__':
    main()