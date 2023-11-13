def main(a,b,c):
    """
    Find how many negative numbers there are in the given numbers.
    Args:
        a: integer
        b: integer
        c: integer
    returns:
        integer: the number of negative numbers in the given numbers
    """
    manfiy = 0

    if a < 0:
        manfiy += 1
    if b < 0:
         manfiy += 1
    if c < 0:
        manfiy += 1

    return manfiy

a = -2
b = -2
c = 0

manfiy = main(a, b, c)
print("Berilgan sonlarda", manfiy, " ta manfiy son")
    