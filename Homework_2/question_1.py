# ******************************** q 1 a ************************************
string = input("ENTER A STRING: ")
char_keys = {}

for ch in string:
    if ch not in char_keys:
        char_keys[ch] = 1
    else:
        char_keys[ch] += 1

lst = sorted(char_keys)

for item in lst:
    print(f"{item} - {char_keys[item]}")

# ******************************** q 1 b ************************************

# revers dict
dict2 = {"a": 1, "b": 2, "c": 3, "d": 4}
print(f"befor the revers the dict is: {dict2}")

dict2 = {v : k for k , v in dict2.items()}
print(f"after the revers the dict is: {dict2}")

