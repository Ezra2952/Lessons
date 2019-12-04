name = input("Enter your name? ")
###with open('name.txt', 'w') as name_files using (with) keywords
name_files = open('name.txt', 'w')
name_files.write(name)
name_files.close() ## if creat the obj file with (with) keyword no need for this line

nameread_file = open('name.txt', 'r')
name = nameread_file.read()
nameread_file.close()
print("Your name is", name)

num_file = open('number.txt', 'w')
num_file.write("17\n")
num_file.write("42\n")
num_file.write("400\n")
num_file.close()

number_file = open('number.txt', 'r')
num1 = int(number_file.readline())
num2 = int(number_file.readline())
number_file.close()
print(num1 + num2)

number_file = open('number.txt', 'r')
total = 0
for i in number_file:
    num = int(i)
    total = total+num
number_file.close()
print(total)