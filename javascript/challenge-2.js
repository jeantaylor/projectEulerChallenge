/*
Problem 2: Even Fibonacci Numbers 
  Find the sum of all even Fibonacci numbers less than 4 million. 

  Expected Result >>> 4613732

  First attempt: While trying a different approach using Binet's Formula, rounding errors caused final result to be off.
    let evenFib = []
    let fib = 0
    let i = 0

    while (fib < 4000000) {
      fib = Math.round((Math.pow(1.6180339, i) - (Math.pow((1 - 1.6180339), i))) / Math.sqrt(5))
      i++
      if (fib % 2 === 0 && fib < 4000000) {
        evenFib.push(fib)
      }
    }

    let sum = evenFib.reduce((a, b) => a + b, 0)
*/

let evenFib = []
let fibx = 0
let fiby = 1
let fibz = 0

while (fibz < 4000000) {
  fibz = fibx + fiby
  fibx = fiby
  fiby = fibz
  if (fibz % 2 == 0 && fibz != 4000000) {
    evenFib.push(fibz)
  }
}

let sum = evenFib.reduce((a, b) => a + b, 0)

console.log("The sum of all even Fibonacci numbers less than 4,000,000 is " + sum)