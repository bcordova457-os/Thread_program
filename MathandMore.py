# simple program to implement the use of multiple
# processes to computer various different information
# about a number input from the user:
# prime, squared, even/odd, binary representation
# and factorial of that number.

from multiprocessing import Process, Value
import math


def isPrime(x):

    sqrtx = int(math.ceil(math.sqrt(x)))
    for i in range(2, sqrtx + 1):
        if x % i == 0:
            print(x, " is not a prime.")
            break
        else:
            print(x, " is a prime.")
            break


def squared(y):

    sqrty = y*y
    print(y, " squared: ", sqrty)


def evenOrOdd(z):

    if(z % 2) == 0:
        print(z, "is even.")
    else:
        print(z, "is odd.")


def binarynHex(a):

    bin_a = bin(a)
    print(a, " in binary: ", bin_a.replace('0b', ''))

    hexnum = hex(a)
    print(a, "in hex: ", hexnum)

def Factorization(b):

    factorial = 1
    for i in range(1, b+1):
        factorial = factorial * i

    print(b, "factorial is: ", factorial)

def createThreads():

    n = input("Enter in a number: ")

    x = int(n)
    y = int(n)
    z = int(n)
    a = int(n)
    b = int(n)

    process1 = Process(target=isPrime, args=(x,))
    process2 = Process(target=squared, args=(y,))
    process3 = Process(target=evenOrOdd, args=(z,))
    process4 = Process(target=binarynHex, args=(a,))
    process5 = Process(target=Factorization, args=(b,))

    process1.start()
    process2.start()
    process3.start()
    process4.start()
    process5.start()

    process1.join()
    process2.join()
    process3.join()
    process4.join()
    process5.join()


createThreads()
