pno = []
print("Enter the page numbers, and enter -1 to terminate")
while(1):
    i = int(input())
    if (i == -1):
        break
    else:
        pno.append(i)

print("Missing page numbers are:")
for i in range(1, 26):
    if i in pno:
        pass
    else:
    	if i < 25:
    		print(i, end = ", ")
    	else:
    		print(i)
