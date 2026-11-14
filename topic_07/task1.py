class Perfume:
    def __init__(self, name, brand, price):
        self.name = name
        self.brand = brand
        self.price = price

    def __str__(self):
        return f"Парфуми: {self.name}, Бренд: {self.brand}, Ціна: {self.price} грн"


perfume1 = Perfume("Libre", "Yves Saint Laurent", 4500)
perfume2 = Perfume("Good Girl", "Carolina Herrera", 5200)
perfume3 = Perfume("J'adore", "Dior", 6100)

print(perfume1)
print(perfume2)
print(perfume3)
