def fibonacci(n):
    if n <= 0:
        print("Number of fibonacci")
        return
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib = [0, 1]
        for i in range(2, n):
            fib.append(fib[i - 1] + fib[i - 2])
        return fib


while True:
    n = input(" Enter a number of fibonacci or 'p' to end program")
    if n.lower() == "p":
        break
    try:
        n = int(n)
        result = fibonacci(n)
        print(result)
    except ValueError:
        print("Please enter a number of fibonacci or 'p' to end program")
