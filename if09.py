def main(a):
    """
    The two-digit integer is given.
    Replace the digits of the number.
    True if the resulting number is less than or equal to the old number, otherwise return False.
    
    Args:
        a: integer
    Returns:
        boolean: True if the resulting number is less than or equal to the old number, otherwise return False.
    Ikki xonali butun son berilgan.
     Raqamning raqamlarini almashtiring.
     Agar olingan son eski raqamdan kichik yoki teng bo'lsa, rost, aks holda False qaytariladi.
    
     Args:
         a: butun son
     Qaytaradi:
         mantiqiy: agar olingan son eski raqamdan kichik yoki teng bo'lsa, rost, aks holda False qaytariladi.
         """
    birinchi_raqam = a % 10
    ikkinchi_raqam = a // 10
    if birinchi_raqam <= ikkinchi_raqam:
        return True
    
    return False
print(main(57))
print(main(21))