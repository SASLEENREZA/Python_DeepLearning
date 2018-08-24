def reverse(s):
    str=""
    for i in s:
        str = i+str
    return str

s=input("enter the string")
print("the input string is : ", end="")
print(s)

print("the reveresed string is : " , end ="")
print(reverse(s))
 