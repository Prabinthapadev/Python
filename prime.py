num = int(input("Enter a number:"))

def prime(num):
    count = 0
    for i in range(1,num+1):
        if num % i == 0:
            count+=1
    if count == 2:
        print(f"{num} is prime")
    else:
        print(f"{num} is composite")

prime(num)