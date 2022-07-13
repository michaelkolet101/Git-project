lst_1 = [11, 7, 5, 8, 53, 37, 114, 54]
lst_2 = [22, 8, 10, 1, 11]
lst_3 = [71, 3, 22, 8, 2, 14, 1]

list_of_lists = [lst_1, lst_2, lst_3]

# delet from list of lists the list with dup val
for l in list_of_lists:
    if len(l) != len(set(l)):
        print(f"in this list ther is duplicated values {l}")
        list_of_lists.remove(l)

if len(list_of_lists) == 1:
    print(f"the anser is: {list_of_lists}")
elif len(list_of_lists) == 0 :
    print("it is ampty list !!!")
elif len(list_of_lists) > 1:
    while len(list_of_lists) > 1:
        intersct = set(list_of_lists[0]).intersection(set(list_of_lists[1]))
        list_of_lists.remove(list_of_lists[0])

print (f"the intersction of the other lists is: {intersct}")

