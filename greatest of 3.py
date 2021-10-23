str = input("enter 3 numbers")
z = str.split(" ")
print(type(z))
if z[0] <= z[2] and z[1] <= z[2]:
    print(z[2], "is the greatest")
elif z[0] >= z[1]:
    print(z[0], "is the greatest")
elif z[1] >= z[2]:
    print(z[1], "is the greatest")
