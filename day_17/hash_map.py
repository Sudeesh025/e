my_map={}
my_map["key"]="This is a value"
my_map[0]="ZERO"
my_map[1.3]="ONE THREE"

print(my_map)
try:
    print(my_map[10])
except:
    print("key doesn't exist")
print(my_map[1.3])
del my_map[0]
print(my_map)
if "key" in my_map:
    print("key key is present")
else:
    print("key do exist")

    