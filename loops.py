#loops
def sum_using_loop(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total
#Output 
print(sum_using_loop(5))  # 15

#while loop
def factorial_using_while(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result
#Output
print(factorial_using_while(5))  # 120
