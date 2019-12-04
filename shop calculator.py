total = 0
num_item = int(input("Number of items: "))
while num_item < 0:
    print("Invalid number of items!")
    num_item = int(input("Number of items: "))
for i in range(num_item):
    pri_item = float(input("Price of item: "))
    total = total + pri_item

if total > 100:
    Dis = total * 10/100
    total = total - Dis

print("Total price for ", num_item, " items is $"   , total)