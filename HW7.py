
from collections import Counter

with open("/etc/passwd") as passwdfile:
        info_list = [(x.strip().split(":"))[-1] for x in passwdfile]
        shells_dict = Counter(info_list)


with open("/etc/group") as groupfile:


