def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def factorial(a: int) -> int:
    """
    This function is to calculate factorial of a number
    :param a:
    :return:
    """
    if a == 0:
        raise ValueError("Cannot calculate factorial of 0")
    result = 1
    for i in range(1, a + 1):
        result = result * i
    return result

def is_prime(a: int) -> bool:
    """
    Check if a number is a prime;
    prime number is a number that is greater than 1 and divided by 1 or itself
    :param a:
    :return:
    """
    if a <= 1:
        return False
    for i in range(2, a):
        if a % i == 0:
            return False

    return True

def power(a, b):
    """
    Calculate a powers b
    :param a:
    :param b:
    :return:
    """
    return a ** b


def calculate():
    numbers = input("Please input one or two numbers separated by a space: ")
    numbers = numbers.split(" ")
    if len(numbers) == 1:
        a = int(numbers[0])
        print(f"Factorial of {a} is {factorial(a)}")
        print(f"Is {a} a prime number? {is_prime(a)}")
    elif len(numbers) == 2:
        a = int(numbers[0])
        b = int(numbers[1])
        print(f"Power: {power(a, b)}")
    else:
        print("Invalid input")

if __name__ == '__main__':
    calculate()
