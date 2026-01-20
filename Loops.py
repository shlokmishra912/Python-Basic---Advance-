# using while loops
# 1. Countdown game
def Countdown():
    n = int(input("Enter a number to countdown: "))
    while n >= 0:
        print(n)
        n -= 1
    print("Blast Off!")

# 2. Sum of numbers
def SumNumbers():
    total = 0
    a = 1
    while a <= 10:
        total += a
        a += 1
    print("Sum of first 10 numbers:", total)

# 3. Guessing game
def GuessNumber():
    secret = 7
    guess = 0
    while guess != secret:
        guess = int(input("Guess the number (1-10): "))
        if guess == secret:
            print("Correct!")
        else:
            print("Try again!")

# 4. Even numbers
def EvenNumbers():
    a = 2
    while a <= 20:
        print(a)
        a += 2

# 5. Factorial
def Factorial():
    n = int(input("Enter a number: "))
    fact = 1
    while n > 0:
        fact *= n
        n -= 1
    print("Factorial is:", fact)

# 6. Multiples of 5
def MultiplesOfFive():
    a = 5
    while a <= 50:
        print(a)
        a += 5


#Using for Loops
# 1. Print squares
def Squares():
    for i in range(1, 11):
        print(f"{i}^2 = {i*i}")

# 2. Reverse counting
def ReverseCount():
    for i in range(10, 0, -1):
        print(i)

# 3. Multiplication table (user input)
def UserTable():
    num = int(input("Enter a number: "))
    for i in range(1, 11):
        print(f"{num} X {i} = {num*i}")

# 4. Sum of even numbers
def SumEven():
    total = 0
    for i in range(2, 21, 2):
        total += i
    print("Sum of even numbers up to 20:", total)

# 5. Pattern printing
def StarPattern():
    for i in range(1, 6):
        print("*" * i)

# 6. Fibonacci series
def Fibonacci():
    n = int(input("Enter how many terms: "))
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b
    print()

# 7. Odd numbers
def OddNumbers():
    for i in range(1, 20, 2):
        print(i)

#Making factorial
