# Recursion

# Divide the big problem into small and simple problem
# Find a base condition with simple answer
# Return base condition answer to solve all sub problems

# Iterative approach
def find_sum(n):
    sum = 0
    for i in range(1, n+1):
        sum +=i
    return sum

if __name__ == "__main__":
    print(f"Iterative Approach: {find_sum(5)}")


def find_sum_recursive(n):
    # Base case: if n is 0, the sum is 0
    if n == 0:
        return 0
    # Recursive case: sum of numbers up to n is n plus the sum of numbers up to n-1
    else:
        return n + find_sum_recursive(n-1)

if __name__ == "__main__":
    # Test the recursive function with an example
    print(f"Recursive Approach: {find_sum_recursive(5)}")


# Recursion Approach
def recursive_sum(n):
    if n == 1:
        return 1
    return n + recursive_sum(n - 1)

if __name__ == "__main__":
    print(f"Recursive Approach {recursive_sum(5 )}")

# Fibonacci Calculation with recursive
# 0,1,1,2,3,5,8
# - - - - - - -
# 0,1,2,3,4,5,6

def fib(n):
    # Base case: if n is 0 or 1, return n (0 or 1)
    if n == 0 or n == 1:
        return n
    # Recursive case: return the sum of the previous two Fibonacci numbers
    else:
        return fib(n-1) + fib(n-2)

if __name__ == "__main__":
    # Test the function with an example (n=6)
    print(f"Fib: {fib(6)}")


