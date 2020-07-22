pd = int(input())
num = pd
while True :
	rev = 0
	temp = num + 1
	while temp>0 :
		rem = temp%10;
		rev = rev*10 + rem
		temp = temp//10
	if rev == num+1 :
		print(num+1)
		break
	num += 1