#PROGRAM 16
with open(input("enter file to copy from: "), "r") as f1:
    with open(input("enter file to copy to: "), "w") as f2:
        for i in f1:
            f2.write(i)
