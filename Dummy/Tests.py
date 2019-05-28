

def check_commons(a,b):

	s1=set(a)
	s2=set(b)
	s3=set()

	s3=s1.difference(s2)
	print(s3)


if __name__ == '__main__':
	a = [1, 2,  4, 5,8,9]
	b = [6, 7, 8, 9]
	check_commons(a,b)