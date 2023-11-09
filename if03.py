def main(a):
    """
    If the number is positive, increase it to 1, else decrease it to 2. If it is 0, assign 10.
    Args:
        a: integer
    Returns:
        a: integer
 
     Agar raqam ijobiy bo'lsa, uni 1 ga oshiring, aks holda 2 ga kamaytiring. Agar u 0 bo'lsa, 10 ni belgilang.
     Args:
         a: butun son
     Qaytaradi:
         a: butun son
    """

    if a > 0:
        return a + 1
    elif a < 0:
        return a - 2
    else:
        return 10 
print(main(3))
print(main(-9))  # Natija: -5
print(main(0))  # Natija: 10    