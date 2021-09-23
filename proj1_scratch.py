from random import randint


# Problem 1 - Implement primality, primality2 and primality3
def primality(N):
    a = randint(1, N) # Get a random int between 1 and n
    return (a ** (N - 1) % N) == 1 % N
        

def primality2(N, k):
    for x in range(1, k):
        if not primality(N):
            return False
    
    return True



def primality3(N, k):
    if N % 2 == 0 or N % 3 == 0 or N % 5 == 0 or N % 7 == 0:
        return False
    
    return primality2(N, k)





def check():
    # userNum = int(input("Enter a number:"))
    # conf = int(input("Enter confidence parameter:"))
    userNum = 587
    conf = 100

    return primality3(userNum, conf)


def main():
    primes = 0
    composites = 0
    for i in range(1, 100):
        if check():
            primes += 1
        else:
            composites += 1

    print("Prime:", primes)
    print("Composite:", composites)
    print("Error:", composites/primes)



main()