#PROGRAM 7
x = {}
while True:
    u, k = input("enter key and value of dictionary(type 0 0) to exit:").split()
    if u == "0" and k == "0":
        break
    x[u] = eval(k)
y = dict((("c", 3), ("d", 4)))
print(x)
print(y)
print("merging the 2 arrays:")
z = {}
for i, j in x.items():
    z[i] = j
for i, j in y.items():
    z[i] = z.get(i, 0) + j
print("after merging the two arrays:")
print(z)
print("popping an items from dictionary:")
z.pop("a")
print(z)
z.popitem()
print(z)
print("clearing a dictionary:")
z.clear()
print(z)
