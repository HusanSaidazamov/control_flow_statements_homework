def main(a):
    """
    Given an integer a, check the following conditions:
    "two-digit odd number",
    "two-digit even number",
    "three-digit odd number",
    "three-digit even number"

    Args:
        a: integer
    Returns:
        string: the message to print
     Agar butun a soni berilgan bo'lsa, quyidagi shartlarni tekshiring:
     "ikki xonali toq raqam",
     "ikki xonali juft son",
     "uch xonali toq son",
     "uch xonali juft son"

     Args:
         a: butun son
     Qaytaradi:
         string: chop etish uchun xabar
     """
    if (a%2==1 and a//10) and 100>a:
        return     "two-digit odd number" 
    if (a%2==0 and a//10) and 100>a:
        return      "two-digit even number"
    if (a%2==1 and a//100) and 100<a<1000:
        return       "three-digit odd number"
    if (a%2==0 and a//100) and 100<a<1000:
        return       "three-digit even number" 
print(main(157))
print(main(-257))