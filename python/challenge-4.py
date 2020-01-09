"""
Problem 4: Largest Palindrome Product
  A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

  Find the largest palindrome made from the product of two 3-digit numbers.

  Expected Result >>> 906609
"""
from itertools import combinations_with_replacement


def isPallendrome(val):
    if type(val) != str:
        val = str(val)

    for i in range(0, len(val)):
        if val[i] == val[len(val)-1-i]:
            continue
        else:
            return False
    return True


factorList = []
pallendromicProducts = []

for i in range(100, 999+1):
    factorList.append(i)

factorCombos = combinations_with_replacement(factorList, 2)

for i in list(factorCombos):
    product = i[0]*i[1]
    if isPallendrome(product):
        pallendromicProducts.append(product)

biggest = max(pallendromicProducts)
print(biggest)
