s = input("enter the list of numbers")
L = s.split(",")
t = tuple(L)

print("given list of values is", L)
print( (t[0],  t[-1]))
