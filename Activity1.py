
keys = [1, 2, 3, 4, 5]
names = ["Alex", "Anne", "Andrew", "Adriel", "Hiruni"]
marks = ["60", "30", "95", "80", "40"]

name_dict = dict(zip(keys, names))
mark_dict = dict(zip(keys, marks))

 #Part2
result = {k: (name_dict[k], int(mark_dict[k]))for k in keys if int(mark_dict[k]) >= 50}

print(result)
