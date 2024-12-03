# Part 1: Design my Class
class Smartphone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def make_call(self, number):
        return f"Calling {number} using {self.model}."

    def browse_web(self, website):
        return f"Browsing {website} on {self.model}."

# Example usage of Smartphone class
my_phone = Smartphone("Apple", "iPhone 14", 999)
print(my_phone.make_call("123-456-7890"))
print(my_phone.browse_web("www.google.com"))

# Adding inheritance
class GamingSmartphone(Smartphone):
    def __init__(self, brand, model, price, gpu):
        super().__init__(brand, model, price)
        self.gpu = gpu

    def play_game(self, game_name):
        return f"Playing {game_name} with {self.gpu} GPU on {self.model}."

# Example usage of GamingSmartphone class
my_gaming_phone = GamingSmartphone("Asus", "ROG Phone 6", 1200, "Adreno 730")
print(my_gaming_phone.play_game("Call of Duty Mobile"))

# Part 2: Polymorphism Challenge
class Vehicle:
    def move(self):
        pass

class Car(Vehicle):
    def move(self):
        return "Driving 🚗"

class Plane(Vehicle):
    def move(self):
        return "Flying ✈️"

class Boat(Vehicle):
    def move(self):
        return "Sailing 🚤"

# Example usage of polymorphism
vehicles = [Car(), Plane(), Boat()]
for vehicle in vehicles:
    print(vehicle.move())
