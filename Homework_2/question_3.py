
list_of_nums = [31, 99, 3, 1943]

# it can be changed to "asc" or "desc", try it
sort_order = "desc"

list_of_nums = [str(n) for n in list_of_nums]
nums = []

for num in list_of_nums:
    for digit in num:
        nums.append(digit)

if sort_order == "asc":
    print(sorted(set(nums)))
elif sort_order == "desc":
    print(sorted(set(nums), reverse=True))

