# Use number = [1,2,3,4,5] to calculate the factorial
def factorial_loop(n):
    result = 1
    if n == 0:
        return result
    for i in range(1, n + 1):
        result = result * i
    return result

number = [1, 2, 3, 4, 5]
factorial_result = [factorial_loop(i) for i in number]
print(factorial_result)

factorial_result = {str(num): factorial_loop(num) for num in number}
print(factorial_result)

# Only use list generator expression
# :=  Walrus operator
# There is an if-else expression in front of the for-loop in case num is zero
# the expression in else condition is to use tuple and walrus operator to calculate the factorial result
# walrus operator will make f visible in the whole expression, so it can be used in the second item of the tuple
# in result, it returns the final item using [-1]
# eg: if num = 3, the tuple is (1, [1, 2, 6], 6), so it needs to return the final item.
factorial_result = [1 if num == 0 else (f := 1, [f := f * i for i in range(1, num + 1)], f)[-1] for num in number]
print(factorial_result)