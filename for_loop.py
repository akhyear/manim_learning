basket = ["apple", "Banana", "Orange"]
nums = [2,5,7,-9,2]
for i in basket:
    print(i)

for i in nums:
    print(i)

for num in nums:
     if num<0:
        break
     print(num)

for num in nums:
    if num%2==0:
        continue
    print(num)