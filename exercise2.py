"""
Given the positive integers a,b and m with m > 1 , find (a^b)modm

"""
from exercise1 import convert
def mod_exp(a,b,m) :
    """
    Does just as the question asked..lol
    :param a: the base number
    :param b: the exponent
    :param m:  the modulus
    :return: the value of (a^b)modm
    """

    #i will be using the modular exponentiation principle by treating the exponent as its binary expansion
    #...get the binary equivalent of the exponent by using the convert function of exercise1
    converted_b =   convert(b,2)
    multiplier = a
    if converted_b[len(converted_b)-1] ==1 :
        result = a%m
    else :
        result = 1

    for  i in range (len(converted_b)-2 ,-1 , -1) :
        if converted_b[i]== 0 :
            multiplier=(multiplier**2) %m
        else :
            multiplier = (multiplier ** 2) % m
            result = (result*multiplier) % m



    return result


if __name__=="__main__":
    print(mod_exp(7, 2, 3))