def odd_value():
	i =-1
	while(i !=0):
		i=i+2
		yield i
n = odd_value()
print(next(n))
print(next(n))
print(next(n))
print(next(n))
print(next(n))
print(next(n))
print(next(n))
print(next(n))
