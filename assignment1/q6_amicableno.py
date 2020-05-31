count = 0
num = 1
l = []
while count < 10:
    num += 1
    sum = 0
    for i in range(1, num):
        if num % i == 0:
            sum = sum + i
        i += 1
    tempnum = sum
    sum = 0
    for i in range(1, tempnum):
        if tempnum % i == 0:
            sum = sum + i
        i += 1
    if num == sum and tempnum != num:
        count += 1
        l.append([num, tempnum])
print(l)