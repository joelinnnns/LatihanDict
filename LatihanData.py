import os
import random
import string

data = dict()
while True:
    os.system("cls") # WIN
    # os.system("clear") # mac/linux
    print(f" {'DATA MEREK PRODUK':❤^45}")
    keyFinal = "".join(random.choice(string.ascii_uppercase) for i in range(3))
    pantene = input("Enter nama sampo\t\t:")
    wardah = input("Enter nama skincare\t\t:")
    lifeboy = input("Enter nama sabun\t:") 

    data[ keyFinal ] = { 'pantenekey' : pantene, 'wardahkey' : wardah,'lifeboykey' : lifeboy } 
     
    opsi = input("input data LAGI (y/t) :").lower()
    if opsi == 't':
        break

print("-"*40)
print(f"Key\t sampo\t skincare\t sabun")
print("-"*40)
for key, value in data.items():
    print(f"{key}.\t {value['pantenekey']}\t {value['wardahkey']}\t \t{value['lifeboykey']}")