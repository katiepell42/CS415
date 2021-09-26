from random import randint

# Problem 1 - Check if a number is prime
# Solves x^y mod p
def modular_expo(x, y, N):
    if y == 0:
        return 1
    z = modular_expo(x, y//2, N)
    if y % 2 == 0:
        return (z**2) % N
    else:
        return x * (z**2) % N

def primality(N):
    # Check if number is prime, return yes if true
    a = randint(1, N - 1)

    if modular_expo(a, N - 1, N) != 1:
        return True
    return False

def primality2(N, k):
    # Check the probality function k times to make sure its a valid return
    for i in range(1, k):
        if primality(N):
            return True
    return False
            
# Checks for prime number
def primality3(N, k):
    checklist = [2, 3, 5, 7]
    for item in checklist:
        if N % item == 0:
            return False
    
    return primality2(N, k)

# Problem 2 - Generate a random prime number
def n_digit_num(n):
    start = 10 ** (n - 1)
    end = (10 ** n) - 1

    return randint(start, end)

def n_digit_prime(n, k):
    N = n_digit_num(n)
    while not primality(N):
        N = n_digit_num(n)

    return N

# Problem 3 - Encryption algorithm

#Euclid's Extended Algorithim for GCD
def gcd(a,b):
    if b == 0:
        return (1,0,a)
    else:
        x, y, extended_gcd = gcd(b, a % b)

        return y, x - (a//b)*y, extended_gcd

def encryption(n, k, message):
    p = n_digit_prime(n, k)
    q = n_digit_prime(n, k)
    N = p * q
    S = (p - 1) * (q - 1)
    E = n_digit_prime(n, k)
    lowest_divisor = gcd(E, S)[2]
    while lowest_divisor != 1:
        E = n_digit_prime(n, k)
        lowest_divisor = gcd(E, S)[2]

    d = 1 / (E % S)
    print("\nN:", N)
    print("e:", E)
    print("d:", d)

    encrypted_message = modular_expo(message, E, N)
    decrypted_message = modular_expo(message, d, N)

    print("Encrypted message:", encrypted_message)
    print("Decrypted message: ", decrypted_message)

# Problem 4 - Precise arithmetic operations
def hsum(n):
    j = 1
    sum = 0
    while sum < n:
        sum = sum + 1/j
        j = j + 1
    return j - 1

def equal(a, b, c, d):
    return a/b == c/d

def less(a, b, c, d):
    return a/b < c/d

# Part A
def hsum2(n):
    j = 1
    sum = 0
    while sum < n:
        sum = sum + 1/j
        j = j + 1
    return j

# Part B
def g_series(n):
    if n == 0:
        return (1, 19)
    elif n == 1:
        return (3, 7)

    numerator_first_term = 3 * g_series(n - 1)[0] * g_series(n - 2)[1]
    numerator_second_term = 2 * g_series(n - 1)[1] * g_series(n - 2)[0]
    numerator = numerator_first_term + numerator_second_term
    denominator = 2 * g_series(n - 1)[1] * g_series(n - 2)[1]

    return (numerator, denominator)


def printMenu():
    print("1. Solve problem 3")
    print("2. Solve problem 4a")
    print("3. Solve problem 4b")
    print("4. Quit")

def main():
    printMenu()
    userInput = int(input("Enter an option from the menu: "))
    while userInput != 4:
        if userInput == 1:
            n = int(input("Enter a value for n: "))
            k = int(input("Enter a value for k: "))
            M = int(input("Enter a message to encode: "))
            encryption(n, k, M)
        elif userInput == 2:
            n = int(input("Enter a number: "))
            print("It takes ", hsum2(n), " elements of the harmonic series in order for the sum to be greater than ", n, ".", sep="")
        elif userInput == 3:
            n = int(input("Enter a number: "))
            if n % 10 == 1:
                suffix = "st"
            elif n % 10 == 2:
                suffix = "nd"
            elif n % 10 == 3:
                suffix = "rd"
            else:
                suffix = "th"
                
            print("The ", n, suffix, " element of the G series is ", g_series(n), ".", sep="")
        else:
            userInput = int(input(("Please select a valid menu option: ")))

        printMenu()
        userInput = int(input("\nEnter another option from the menu: "))

main()