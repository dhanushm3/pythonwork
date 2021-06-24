def swap(str):
    return str.swapcase()

alpha = [input("Enter alphabetical string:")]
result = map(swap, alpha)
print(list(result))

