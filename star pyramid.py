n = int(input("enter number: "))
for i in range(1, n + 1):
    for j in range(1, 1 + i):
        print("*", end=" ")
    print("")

for i in range(1, n + 1):
    for j in range(1, n+1 - i):
        print("*", end=" ")
    print("")
