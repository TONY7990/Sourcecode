def fibonacci_sequence(n):
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

# Input
n = int(input("Enter the number of terms in the Fibonacci sequence: "))
fibonacci_series = fibonacci_sequence(n)
print(f"Fibonacci sequence with {n} terms: {fibonacci_series}")
