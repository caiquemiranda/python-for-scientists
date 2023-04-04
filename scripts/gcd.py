# File scripts/gcd.py Implementing the GCD Euclidean algorithm.

""" Module gcd: contains two implementations of the Euclid
GCD algorithm, gcdr and gcd.
"""

def gcdr(a,b):
    """ Euclidean algorithm, recursive vers., returns GCD. """
    
    if b == 0:
        return a
    else:
        return gcdr(b, a%b)

def gcd(a,b):
    """ Euclidean algorithm, non-recursive vers., returns GCD. """
    
    while b:
        a, b = b, a%b
    
    return a

##########################################################
if __name__ == "__main__":
    import fib

    for i in range(984):
        print(i, '', gcdr(fib.fib(i), fib.fib(i + 1)))
