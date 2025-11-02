
a = 1
arr = []
while a != 0:
    print("write a >>" , end="")
    a = int(input())
    arr.append(a)

for i in range(len(arr)):
    if arr[i] > 0:
        print(arr[i], end=" ")
print()

for a in arr:
    print(a, end=" ")
print()

phones = {}

name = ""
while True:
    print("Write name >>", end="")
    name = input()
    if name == "end":
        break
    if name in phones:
        print(f"Do you want to change phone for {name}? (y/n) >>", end="")
        ans = input()
        if ans.lower() != 'y':
            continue
    print("Write phone >>", end="")
    phone = input()
    phones[name] = phone

# for name in phones:
#     print(f"{name}: {phones[name]}")

for name, phone in phones.items():
    print(f"{name}: {phone}")

    
print("The End")