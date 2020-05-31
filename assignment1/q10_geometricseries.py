r = int(input("Enter the common ratio in the geometric series: "))
a = int(input("Enter the first element of the series: "))

for i in range(10):
    print(a * (r ** i))