def fibonacci(n):
    if not isinstance(n, int) or n <= 0:
        return []
    elif n == 1:
        return [0]

    fib_sequence = [0, 1]
    for _ in range(2, n):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])

    print("oi");

    return fib_sequence