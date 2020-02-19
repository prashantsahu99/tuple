t=eval(input("enter elements to be separated by comma and in():"))
z=int(input("enter pos  to be removed"))
y=()
y=t[:z-1]
y=y+t[z:]
print(y)
