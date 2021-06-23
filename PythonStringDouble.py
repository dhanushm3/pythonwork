#doubling of the number
s = "12345"
for char in s:
    if(char.isnumeric()):
        print((int(char) * 2 ), end=",")

print(" ")

#squaring of number
s = "12345"
for char in s:
    if(char.isnumeric()):
        print((int(char) * int(char) ), end=",")

#reverse
print (" ")
for i in range(1, len(s) + 1):
        if(s[len(s) - i].isnumeric()):
            print((int(s[len(s) - i]) * 2), end=",")
print(" ")
#input
a = input("enter string:")
for char in a:
    if(char.isnumeric()):
        print((int(char) * 2 ), end=',')