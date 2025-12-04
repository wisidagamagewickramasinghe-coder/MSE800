class MathSeries:

    def fibonacci_series(self, n):
        if n <= 1:
            return n
        return self.fibonacci_series(n-1) + self.fibonacci_series(n-2)

    def factorial_recursive(self, n):
        if n == 0:
            return 1
        return n * self.factorial_recursive(n-1)


if __name__ == "__main__":
    obj = MathSeries()
    n = 5

    print("Fibonacci:", obj.fibonacci_series(n))
    print("Factorial:", obj.factorial_recursive(n))
