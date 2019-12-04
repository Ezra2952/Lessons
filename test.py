
finished = False
while not finished:
    try:
        num1 = int(input("Enter Number: "))
        num2 = int(input("Enter Number: "))
        total = num1 + num2
        finished = True
    except ValueError:
        print("Please enter a valid integer.")
print("Valid result is:", total)