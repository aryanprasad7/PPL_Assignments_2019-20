start = int(input("Enter the starting number of the range: "))
end = int(input("Enter the ending number of the range: "))

for n in range(start, end + 1):
    temp = n
    sum = 0
    while(temp != 0):
        rem = temp % 10
        temp = int(temp / 10)
        sum = sum + (rem ** 3)
    if sum == n:
        print(sum)
    