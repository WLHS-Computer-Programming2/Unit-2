import Car
class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self,make,model,year,battery_level):
        """Initialize attributes of the parent class."""
        super().__init__(make,model,year)
        self.battery_level = battery_level
    
    
