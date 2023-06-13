#Program to perform if esle if statement
math=81
phy=75
comp=69
eng=68
total=360
gain=math+phy+comp+eng
print("your gain marks are=",gain)
per=(gain/total)*100
if(per>=90):
	print("your grade is A+")
elif(per>=80):
	print("your grade is A")
elif(per>=70):
	print("your grade is B")
elif (per>=60):
	print("yoir grade is C")
