dict1 = {0 : "",1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine",10:"ten",11:"eleven",12:"twelve",13:"thirteen",14:"fourteen",15:"fifteen",16:"sixteen",17:"sventeen",18:"eighteen",19:"nineteen"}
dict2 = {20:"twenty",30:"thirty",40:"forty",50:"fifty",60:"sixty",70:"seventy",80:"eighty",90:"ninety"}

def below100(n):
	if n < 20:
		return len(dict1[n])
	return len(dict[n/10-2 | 0]) + len(dict1[n%10])

def numberLength(n):
	if n < 100:
		return below100(n)
	res = 0
	h = floor(n/100)%10
	t = floor(n/1000)
	s = n%100
	if n > 999:
		res += below100(t) + len("thousands")
	if h != 0:
		res += dict1[h] + len("hundred")
	if s != 0:
		res += len("and") + below100(s)
	return res
def solutation(n):
	num = 0
	for i in range(1,1001):
		num += numberLength(i)
	return num
print(solutation(1001))

