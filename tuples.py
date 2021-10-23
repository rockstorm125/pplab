list_1 = tuple(int(x) for x in input("enter the elements in tuple 1: ").split())

list_2 = tuple(int(x) for x in input("enter the elements in tuple 2: ").split())
print("first tuple is: ",list_1)
print("second tuple is: ",list_2)
merge_list = list_1 + list_2
print("merged tuple is: ",merge_list)
print(type(merge_list))
print("length of merged list is: ", len(merge_list))
