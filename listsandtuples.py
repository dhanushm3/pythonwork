#lists

n = int(input())
l = []
for _ in range(n):
    s = input().strip().split(' ')
    cmd = s[0]
    args = s[1:]
    if cmd != "print":
        cmd += "("+",".join(args)+ ")"
        eval("l."+cmd)
    else:
        print(l)

#tuples

if __name__ == '__main__':
    n = int(input())
s = [int(num) for num in input().strip().split(' ')]
s = tuple(s)
print(hash(s))
