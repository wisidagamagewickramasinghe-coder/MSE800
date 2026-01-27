data = []

for i in range(5):
    data.append(lambda a, i=i*2: i*a)


for f in data:
    print(f(10))

    
    