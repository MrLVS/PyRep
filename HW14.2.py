
import pickle
from HW14 import Employee

with open('C:/Users/mrlvs/OneDrive/Рабочий стол/DV/Marydump', 'rb') as file:
    Mary = pickle.load(file)

print(type(Mary))
print(Mary.name)
print(Mary.phone)
Mary.say_name()


