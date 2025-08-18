num = 5
def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num-1)

result = factorial(num)
print(f"The factorial of {num} is {result}")