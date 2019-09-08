"""
Given integers a and b , each greater than 1 , find the  base b expansion of integer a

"""

import math
def convert(number , base) :
    """
    converts an integer "number" to a given "base"
    :param number: the integer to be converted
    :param base: the base to which the integer is converted
    :return: the conversion of the number to the given base
    """
    remainder = []
    while number > 0 :
        remainder.append(number%base)
        number = math.floor(number/base)

    remainder.reverse()
    return remainder


def expand (number , *,base) :
    """
    gives the base exoansion of given number
    :param number: number to be expanded
    :param base: the base to which the number is expanded
    :return: a list of strings-each composite multiplicative term in the expansion
    """
    converted = convert(number , base)
    expansionIndices = []
    expansion = []

    counter = len(converted)
    copy_conv = list.copy(converted)
    for a in copy_conv :
        counter -= 1
        if a==0 :
            converted.remove(a)
            continue
        expansionIndices.append(counter)

    for i in range(len(expansionIndices)) :
        expansion.append("{}*{}^{}".format(converted[i] ,base ,expansionIndices[i])   )
    expansion= " + ".join(expansion)

    return expansion


if __name__ =="__main__":
    print(expand(2345, base=3))
