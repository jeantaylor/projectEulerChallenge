"""
Problem 2: Even Fibonacci Numbers 
  Find the sum of all even Fibonacci numbers less than 4 million. 

  Expected Result >>> 4613732

  First attempt: Doesn't take into account the first even number in the sequence.

    evenFib = []
    fibx = 1 
    fiby = 2 
    fibz = 0 

    while fibz < 4000000:
      fibz = fibx + fiby 
      fibx = fiby 
      fiby = fibz 
      if fibz%2==0 and fibz!=4000000: 
        evenFib.append(fibz)

    print("The sum of all even Fibonacci numbers less than 4,000,000 is " + str(sum(evenFib)))
"""

evenFib = []
fibx = 0
fiby = 1
fibz = 0

while fibz < 4000000:
    fibz = fibx + fiby
    fibx = fiby
    fiby = fibz
    if fibz % 2 == 0 and fibz != 4000000:
        evenFib.append(fibz)

print("The sum of all even Fibonacci numbers less than 4,000,000 is " + str(sum(evenFib)))
