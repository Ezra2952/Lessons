for i in range(1, 21, 2):
    print(i, end=' ')
print()

for a in range(0, 101, 10):
    print(a, end=' ')
print()

for i in range(20, 0, -1):
    print(i, end=' ')
print()

star = int(input("Number of star for show:"))
for i in range(star):
    print('*', end='')
print()

star = int(input("Number of line for show:"))
for i in range(1, star + 1):
    print('*' * i)
print()
