"""
Problem 1: Multiples of 3 and 5 
  Find the sum of all the multiples of 3 and 5 below 1000. 

  Expected Result >>> 233168
"""

multiples = []

for i in range(1000):
    if i % 3 == 0 or i % 5 == 0:
        multiples.append(i)

print("The sum of all multiples of 3 and 5 below 1000 is " + str(sum(multiples)))
