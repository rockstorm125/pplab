inp = input("enter numbers").split()
x = float(inp[0])
y = float(inp[1])
z = float(inp[2])
if (x**2 + y**2) == z**2 or (y**2 + z**2) == x**2 or (z**2 + x**2) == y**2:
    print("the given sides create a right angle triangle")
else:
    print("the given sides DO NOT create a right angle triangle")
