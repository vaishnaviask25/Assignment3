num = int(input("Enter a number: "))
def factorial(number):
    if number == 1 or number ==0:
        return 1
    else:
        return (number*factorial(number-1))
    
result = factorial(num)
print(f"Factorial of {num} is: {result}.")