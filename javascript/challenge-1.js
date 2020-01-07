/*
Problem 1: Multiples of 3 and 5
  Find the sum of all the multiples of 3 and 5 below 1000.

  Expected Result >>> 233168
*/

let multiples = []

for (i = 1; i < 1000; i++) {
  if (i % 3 === 0 || i % 5 === 0) {
    multiples.push(i)
  }
};

let sum = multiples.reduce((a, b) => a + b, 0)

console.log("The sum of all multiples of 3 and 5 below 1000 is " + sum)