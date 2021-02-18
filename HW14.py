
import pickle
import dill

class Employee:
    def __init__(self, name, lastname, position, phone):
        self.name = name
        self.lastname = lastname
        self.positon = position
        self.phone = phone

    def say_name(self):
        print(f"My name is {self.name}.")

    def say_phone(self):
        print(f"My phone {self.phone}.")


Mary = Employee("Mary", "Popins", "Director", "+9657907365")

with open('/home/vitaliy/HomeWork/d.pkl') as dump_out:  # Сохраняем Mary
    pickle.dump(Mary, dump_out)


