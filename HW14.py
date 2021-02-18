
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

if __name__ == '__main__':
    Employee = Employee()


Mary = Employee("Mary", "Popins", "Director", "+9657907365")

# Сохраняем Mary
with open('C:/Users/mrlvs/OneDrive/Рабочий стол/DV/Marydump', 'wb') as file:
    dill.dump(Mary, file)
