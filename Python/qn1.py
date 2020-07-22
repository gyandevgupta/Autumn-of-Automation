outF = open("myFirstFile.txt","w+")
d = int(input())
number_range = list(range(10**(d-1),10**d))

c = 0
new = -1
for num in number_range:
	# all prime numbers are greater than 1
	if num > 1:
		for i in range(2, num):
			if (num % i) == 0:
				c = 0
				break
			else:
				c = 1
		if num-new == 2 and c == 1:
			outF.write(f"{new} {num}")
			outF.write("\n")
		if c==1:
			new = num
outF.close()