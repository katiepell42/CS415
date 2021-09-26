from random import randint
from time import time
from math import sqrt, floor

# Problem 1 - Check if a number is prime
# Solves x^y mod p using Figure 1.4 Modular Exponentiation
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
            
#checks for prime number
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

# Euclids Algo
# def gcd(a, b):
#     if b == 0:
#         return a
    
#     return gcd(b, a%b)

def encryption(n, k):
    p = n_digit_prime(n, k)
    q = n_digit_prime(n, k)
    N = p * q
    S = (p - 1) * (q - 1)
    E = n_digit_prime(n, k)
    lowest_divisor = gcd(E, S)
    while lowest_divisor != 1:
        E = n_digit_prime(n, k)
        lowest_divisor = gcd(E, S)

    d = 1 / (E % S)
    print("\nN:", N)
    print("e:", E)
    print("d:", d)

    message = int(input("enter a message: "))
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
def function4b(n):
    if n == 0:
        return (1, 19)
    elif n == 1:
        return (3, 7)


    # return 1.5 *(function4b(n - 1)[0]/function4b(n - 1)[1]) + function4b(n - 2)[0]/function4b(n - 2)[1]

    numerator_first_term = 3 * function4b(n - 1)[0] * function4b(n - 2)[1]
    numerator_second_term = 2 * function4b(n - 1)[1] * function4b(n - 2)[0]
    numerator = numerator_first_term + numerator_second_term
    denominator = 2 * function4b(n - 1)[1] * function4b(n - 2)[1]

    return (numerator, denominator)


    # (3/2)(a/b) + (c/d)
    # 3a/2b + c/d
    # (3ad + 2bc)/2bd




def main():
    # encryption(50,20)
    print(function4b(2))

main()