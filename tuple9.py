t=eval(input("enter a elaments separated by comma and in ():"))
z=int(input("enter element to be separated :"))
c=0
for i in t:
	c=t.count(z)
	if c!=0:
		print("YES")
		break
	else:
		print("not found")
		break
