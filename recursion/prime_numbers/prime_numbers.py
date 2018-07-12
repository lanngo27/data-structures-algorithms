import math

def is_prime_number(n):
    divider = n-1 #Which is the first number to start finding divider?
    if not has_divisors(n, divider):
        print("Number", n, "is a prime number.")
    else:
        print("Number", n, "is NOT a prime number.")

def has_divisors(n, divider):
    #Write your code here
    if divider==1:
        return False
    if n%divider!=0:
        return has_divisors(n, divider-1)
    else: return True


if __name__ == "__main__":
    #Some examples
    is_prime_number(13) #yes
    is_prime_number(21) #no
