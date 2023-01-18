import os
x=0
name=input("name of files \n")
NuMs=input("amount (can't be less that zero) \n")

while x<int(NuMs):
	with open(name+str(x), mode="w+"): pass
	x=x+1
exit()

