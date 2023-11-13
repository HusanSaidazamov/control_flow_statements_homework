def main(a,b,c):
    """
    Find how many positive numbers there are in the given numbers.
    Args:
        a: integer
        b: integer
        c: integer
    returns:
        integer: the number of positive numbers in the given numbers

    
     """ 
    musbat = 0

    if a > 0:
        musbat += 1
    if b > 0:
        musbat += 1
    if c > 0:
        musbat += 1

    return musbat

a = 4
b = -2
c = 1

musbat = main(a, b, c)
print("Berilgan sonlarda", musbat, " ta musbat son")