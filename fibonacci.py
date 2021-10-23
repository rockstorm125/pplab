
count = int(input("enter the lenght of fibonacci: "))
out = [0, 1]
counter = 0
while counter != (count-2):
    x = out[-1] + out[-2]
    out.append(x)
    counter += 1

print(out)

