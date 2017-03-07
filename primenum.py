def primenum():
	y=[1,2,3,4,5,6,7,8,9]
	result=[]
	for x in y:
		if x % x == 0 and x % 1 == x :
			result.append(x)
	return result 	