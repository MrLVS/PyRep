
import pwd

with open("/home/vitaliy/HomeWork/output.txt", 'w') as file:
    with open("/etc/passwd") as passwdfile:
        info_list = [(x.strip().split(":"))[-1] for x in passwdfile]
        shells_dict = {i: info_list.count(i) for i in info_list}
        shells_info = str(shells_dict)
        file.write(shells_info + "\n")


    with open("/etc/group") as groupfile:
        group = {}
        for line in groupfile:
            line = line.strip().split(":")

            if len(line[3]) > 1:
                users = line[3].split(",")
                user_list = ', '.join(map(str, [pwd.getpwnam(u).pw_uid for u in users]))
                group[line[0]] = user_list

    group_info = str(group)
    file.write(group_info)
