def generateDivisors(n):
    arr = []
    for i in range(1, n + 1):
        if n % i == 0:
            arr.append(i)
    return arr
		
def harmonicMean(n): 
	arr = generateDivisors(n) 
	sum = 0
	length = len(arr) 

	for i in range(0, length): 
		sum = sum + (n / arr[i]) 
	sum = sum / n 
	return length / sum

count = 0
i = 1
while(1):
    hmin = harmonicMean(i)
    if hmin - int(hmin) == 0:
        print(i)
        count = count + 1
    if count == 10:
        break
    i = i + 1