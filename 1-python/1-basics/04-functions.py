def sum(a, b, c=0):
    return a+b+c

print(sum(1,2))
print(sum(1,2,3))
print(sum(a=1, b=2,c=3))

arg1, arg2, arg3 = 1,2,3
print(sum(arg1, b=arg2, c=arg3))