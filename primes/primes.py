def is_prime(n):
    """ Return True if n is a prime number, else False. """
    if n>1:
        for i in range(2, n):
            if (n%i)==0:
                return False
        else:
            return True
    else:
        return False


