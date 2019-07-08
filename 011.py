def Factorial():
    result = 1
    num = 5

    while num > 0:
        result *= num
        num -= 1

    return result

rest = Factorial()
print(rest)



#import math
#def fact(num):
#   result = math.factorial(num)
#   return result

#result = fact(5)
#print(result)
