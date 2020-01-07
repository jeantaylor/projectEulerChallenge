"""
Problem 3: Largest Prime Factor
  The prime factors of 13195 are 5, 7, 13 and 29.
  What is the largest prime factor of the number 600,851,475,143?

  Prime number: number that is only divisible by 1 and itself
  Factor: factor x factor = this multiplication answer

  Expected Result >>> 

  First attempt: Works on 13195. Python freezes up when testing 600,851,475,143.

    def checkPrime(num):
      for i in range(2, num):
          if num % i == 0:
              return False
      else:
          return True

      target = 13195
      #target = 6000851475
      primeFactors = []

      for i in range(2, target): 
        j = target/i
        if j.is_integer(): 
          j = round(j)
          if checkPrime(j) and j not in primeFactors: 
            primeFactors.append(j)
          if checkPrime(i) and i not in primeFactors: 
              primeFactors.append(i)

      print(primeFactors)
      print(max(primeFactors))
"""


def checkPrime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    else:
        return True

target = 13195
#target = 6000851475
primeFactors = []

for i in range(2, target): 
  if checkPrime(i):
    j = target/i
    if j.is_integer(): 
      j = round(j)
      if checkPrime(j) and j not in primeFactors: 
        primeFactors.append(j)
      if checkPrime(i) and i not in primeFactors: 
          primeFactors.append(i)

print(primeFactors)
print(max(primeFactors))