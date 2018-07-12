

def power(base, exponent):
    #Write your code here
    if exponent==1:
        return base
    else: return power(base, exponent-1)*base
    
def main():
    #Try your function
    base = 5
    exponent = 3
    print("{} ^ {} = {}".format(base, exponent, power(base, exponent)))
    
if __name__ == "__main__":    
    main()
