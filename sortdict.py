dict={}
n=int(input("Enter the number of elements"))
for i in range(0,n):
    key=input(f"Enter the key of{i+1}:")
    value=input(f"Enter the value of{i+1}:")
    dict[key]=value

keys=[i for i in dict.keys()]
keys.sort()

for i in keys:
    print(dict[i])

keys.sort(reverse=True)

for i in keys:
    print(dict[i])
   