

howMany = input("how many even numbers do you want?")
# print (*range(5))
# print (*range(3, 5))

print("even numbers are numbers that can be divided by two")

for num in range(int(howMany)+1):
    if (num % 2 == 0):
        print(num)