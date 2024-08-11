import math
def primeCheck(number):
    if (number%2 == 0 and number != 2) or (number%3 == 0 and number != 3) or (number%5 == 0 and number != 5) or (number%7 == 0 and number != 7): 
        return False
    if number == 1:
        return False
    for i in range(8, math.floor(math.sqrt(number)+1), 2):
        if i%3==0 or i%5==0 or i%7 == 0:
            continue
        e = number/i
        print(e)
        if e.is_integer() and i != number:
            return False
    return True
