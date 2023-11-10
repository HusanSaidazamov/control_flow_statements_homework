def main(a, b, c):
    """
    Find how many positive and how many negative numbers there are in the given numbers.
    check the following conditions:
    "there are a lot of positive numbers",
    "there are a lot of negative numbers"

    Args:
        a: first number
        b: second number
        c: third number

    Returns:
        string: string with the result
    """

    musbat_sonlar = 0
    manfiy_sonlar = 0

    if a > 0:
        musbat_sonlar += 1
    if a < 0:
        manfiy_sonlar += 1

    if b > 0:
        musbat_sonlar += 1
    if b < 0:
        manfiy_sonlar += 1

    if c > 0:
        musbat_sonlar += 1
    if c < 0:
        manfiy_sonlar += 1

    if musbat_sonlar > manfiy_sonlar:
        return "Ijobiy raqamlar juda ko'p"
    if manfiy_sonlar > musbat_sonlar:
        return "Manfiy raqamlar juda ko'p"
a =3
b = 2
c = -1

Z = main(a, b, c)
print(Z)
