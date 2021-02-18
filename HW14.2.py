import pickle

with open('/home/vitaliy/HomeWork/dump.dat', 'r') as dump_in:
    Mary = pickle.load(dump_in)

print(Mary)
