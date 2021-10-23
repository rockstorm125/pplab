list_1 = input("enter the elements of a list: ").split()
x = int(input("enter number to be appended: "))
y = int(input("enter number to be removed: "))

for i in range(len(list_1)):
    list_1[i] = int(list_1[i])
print("the created list is: ", list_1)
list_1.append(x)
print("the list after appending is:", list_1)
if y in list_1:

    list_1.remove(y)
    print("the list after removing element is: ", list_1)
else:
    print("enter a number present in the list to remove")
