def main(a):
    """
    Given an integer a, check the following conditions:
    "positive odd number",
    "positive even number",
    "negative odd number",
    "negative even number",
    "the number is zero"

    Args:
        a: integer
    Returns:
        string: the message to print
           Agar butun a soni berilgan bo'lsa, quyidagi shartlarni tekshiring:
     "musbat toq raqam",
     "musbat juft son",
     "salbiy toq raqam",
     "salbiy juft son",
     "raqam nol"
             Args:
         a: butun son
     Qaytaradi:
         string: chop etish uchun xabar
    """
    if a>0 and a%2==1:
        return "positive odd number" 
    if a>0 and a%2==0:
        return  "positive even number"
    if a<0 and  a%2==1:
        return   "negative odd number"
    if a<0 and  a%2==0:
        return   "negative even number" 
    if a==0:
        return   "the number is zero"
print(main(57))

              


    