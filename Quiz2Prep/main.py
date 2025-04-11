class Cellphone:
    num_made = 0
    def __init__(self, color="white", model="iPhone 16", weight=250):
        self.color = color
        self.model = model
        self.weight = weight
    def __repr__(self)->str:
        return f"This is a {self.color} {self.model} phone that weighs {self.weight} grams"
    def __eq__(self,other_phone)->bool:
        return self.color == other_phone.color and \
            self.model == other_phone.model and \
                self.weight == other_phone.weight
    def send_text(self,number,message)->None:
        print(f"Sending {message} to {number}")
        

phone1 = Cellphone("blue","iPhone 12",164)
phone2 = Cellphone()
phone3 = Cellphone("blue","iPhone 12",164)
print(phone1 == phone2)
print(phone1 == phone3)
print(phone1.send_text(5551234567,"Hello!"))


