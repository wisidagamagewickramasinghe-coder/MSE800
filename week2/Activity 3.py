
# Part 1
def fib_series(n):
  f0 =0
  f1=1
  
  print(f0)
  print(f1)
  
  i=1
  while(i<=n):
      fib=f0+f1
      print(fib)
      f0=f1
      f1=fib
      i=i+1
      

def factorial(n):
    
    if n < 0:
        return None  # factorial not defined for negative numbers

    result = 1
    for i in range(1, n + 1):
        result *= i  # multiply result by each number from 1 to n
    return result

# Part 2

if __name__ == "__main__":
    # Ask user to enter N
    n = int(input("Enter the value of N: "))
    fib = fib_series(n)
    print(fib)
 
    fact = factorial(n)
    print(f"\nFactorial of", n, "is:", fact)