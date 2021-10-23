#PROGRAM 17
with open(input("enter the file to be opened: "),"r") as f:
    out = []
    print("before sorting and removing similar words:")
    for i in f:
        print(i)
        out += i.split()
    out = list(set(out))
    out.sort()
    print("after sorting and removing similar words:")
    for i in out:
        print(i,end=" ")