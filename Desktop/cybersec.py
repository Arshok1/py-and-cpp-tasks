import datetime
#1
a = 4
b = 6
c = a + b
print(c)
#2
print(a+1)
#3
time = datetime.datetime.now()
min_to_sec = time.strftime("%M")
print(int(min_to_sec)*60)
#4
side = 8
height = 5
area = (side*height)/2
print(area)
#5 
current = 1200 
voltage = 6
power = voltage*current
print(power)
#6
hour_to_sec = time.strftime("%H")
print(int(hour_to_sec)*60)
#7
side1 = 4
side2 = 5
prob_side3 = side1 + side2
print("third side is less than", prob_side3)
#8
print(a%b)
#10
perim = side1*2+side2*2
print(perim)

#11!!
# def isSameNum(num1, num2):
# 	if(num1 === num2):
# 		return true
# 	else:
# 		return false
# 	

#12!!
# def lessThanOrEqualToZero(num):
# 	if(num<=0):
# 		return true
# 	else:
# 		return false

#13!!
# def animals(chickens, cows, pigs):
# 	return chickens*2+cows*4+pigs*4
# 

#14!!
# def isSameNum(num1, num2):
#  if(num1===num2):
#     return True
#  else:
#     return False
#  
#
#15!!
# def flipBool(b):
# 	return (!b)*1;
#

#16!!
# def isSeven(x):
# 	return x === 7;
#isSeven(8)

#17!!
# def lessThan100(a, b):
# 	if(a+b<100):
# 		return true
# 	else:
# 		return false
#

#18!!
# def convert(hours, minutes):
# 	return hours*3600+minutes*60
# 

#19!!
# def sumPolygon(n):
# 	return (n-2)*180
# 

#20!!
# def points(twoPointers, threePointers):
#	return twoPointers * 2 + threePointers * 3
