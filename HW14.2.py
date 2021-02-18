
import dill


with open('C:/Users/mrlvs/OneDrive/Рабочий стол/DV/Marydump', 'rb') as file:
    Mary = dill.load(file)

print(type(Mary))
print(Mary.name)
print(Mary.phone)
print(Mary.say_name)

