def main(a):
    """
    If the number is positive, increase it to 1, else decrease it to 2.
    Args:
        a: integer
    Returns:
        a: a increased by 1 if positive, else decreased by 2.
    
     Agar raqam ijobiy bo'lsa, uni 1 ga oshiring, aks holda 2 ga kamaytiring.
     Args:
         a: butun son
     Qaytaradi:
         a: agar ijobiy bo'lsa, 1 ga ko'tariladi, aks holda 2 ga kamayadi.
    
    """
    if a > 0:
        return a + 1
    
    return a - 2
print(main(5))
print(main(-1))