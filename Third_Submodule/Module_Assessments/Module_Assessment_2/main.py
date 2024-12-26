num = int(input("Please enter the number : "))

res = 1

for i in range(2, num + 1):
    res *= i
print("Factorial of", num, "is", res)