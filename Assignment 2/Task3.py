import time
import sys

sys.setrecursionlimit(6000)

# naive approach
def fib_naive(n):
    if n <= 1:
        return n
    return fib_naive(n-1) + fib_naive(n-2)

start = time.time()
result = fib_naive(40)
end = time.time()
print("Naive recursion result:", result)
print("Execution time:", end - start, "seconds")


def fib_memo(n, memo=None):
    if memo is None:  # Added because of python caching
        memo = {}
    if n in memo:
        return memo[n]
    if n <= 1:
        memo[n] = n
        return n
    memo[n] = fib_memo(n-1, memo) + fib_memo(n-2, memo)
    return memo[n]

repeats = 100000
start = time.perf_counter()
for _ in range(repeats):
    result = fib_memo(40)
end = time.perf_counter()

avg_time = (end - start) / repeats

print("Top-down result:", result)
print(f"Execution time: {avg_time:.20f} seconds")


def fib_bottom_up(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n+1):
        a, b = b, a + b
    return b


repeats = 1000
start = time.perf_counter()
for _ in range(repeats):
    result = fib_bottom_up(40)
end = time.perf_counter()

avg_time = (end - start) / repeats

print("Bottom-Up result:", result)
print(f"Execution time: {avg_time:.20f} seconds")

