str = input("enter elements separated by comma:").split(",")
lst=[int(x) for x in str]
t=tuple(lst)
z=[int(input("enter a elementto be added"))]
c=tuple(z)
t=t+c
print(t)

