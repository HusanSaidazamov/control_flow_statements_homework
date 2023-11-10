def main(temp):
    """
    Display the message according to the following temperature conditions given to you in Celsius:
    Temp<0: "Freezing"
    Temp 1-10: "Very Cold"
    Temp 11-20: "Cold"
    Temp 21-30: "Normal"
    Temp 31-40: "Hot"
    Temp >40: "Very Hot"

    Args:
        temp: integer
    Returns:
        string: the message to print
    """
    if temp<0:
       return "Freezing"
    if temp>0 and 1<=temp<=10:
        return  "Very Cold"
    if  temp>0 and 11<=temp<=20:
        return   "Cold"
    if temp>0 and 21<=temp<=30:
        return   "Normal" 
    if temp>0 and 31<=temp<=40:
        return  "Hot"
    if temp>40:
        return "Very Hot"
print(main(-5))
print(main(5))
print(main(14))
print(main(25))
print(main(32))
print(main(60))