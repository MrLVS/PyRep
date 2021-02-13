# Function to converting degrees to different unit(Celsius or Fahrenheit)
from textwrap import dedent

def degrees_convector():
    print(dedent("""
        Выберете вариант преобразования:
        1 - °F в °C 
        2 - °C в °F """))
    choice = input(">>> ")
    if choice == 1 or choice == "1":
        fahrenheit_to_celsius()
    elif choice == 2 or choice == "2":
        celsius_to_fahrenheit()
    else:
        print('Вы ввели неправильное значение. Выберете "1" или "2".')
        degrees_convector()

def fahrenheit_to_celsius():
    """ Function for converting Fahrenheit to Celsius"""
    f = int(input("Введите число --> "))
    c_degrees = 5.0 * (f - 32) / 9
    print(c_degrees)

def celsius_to_fahrenheit():
    """ Function for converting Celsius to Fahrenheit"""
    c = int(input("Введите число --> "))
    f_degrees = (9 / 5.0 * c) + 32
    print(f_degrees)


degrees_convector()