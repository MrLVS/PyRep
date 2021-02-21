
import dill


class Employee:
    def __init__(self, name, lastname, position, phone):
        self.name = name
        self.lastname = lastname
        self.position = position
        self.phone = phone

    def say_name(self):
        print(f"My name is {self.name}.")

    def say_phone(self):
        print(f"My phone {self.phone}.")

with open('C:/Users/mrlvs/OneDrive/Рабочий стол/DV/Marydump', 'rb') as file:
    Mary = dill.load(file)

print(type(Mary))
print(Mary.name)
print(Mary.phone)

