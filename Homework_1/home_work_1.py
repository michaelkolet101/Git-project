lst = [4, 5, 7, 2]
histo = ['*' * item for item in lst]
print(f"EX 1 : {histo}")

lst1 = ['a', 'b', 'c']
lst2 = ['x', 'y', 'z']
lst_res = []

for idx in range(len (lst1)):
    lst_res.append(lst1[idx] + lst2[-1 -idx])

print(f"EX 2 - {lst_res}")