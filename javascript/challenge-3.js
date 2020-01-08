/*
Problem 3: Largest Prime Factor
  The prime factors of 13195 are 5, 7, 13 and 29.
  What is the largest prime factor of the number 600,851,475,143?

  Prime number: number that is only divisible by 1 and itself
  Factor: factor x factor = this multiplication answer

  Expected Result >>> 6857
*/

// Below solution works for test case, but freezes when testing 600,851,475,143.
checkFactor = (target, i) => {
  if (target % i === 0) {
    return true
  } else return false
}

checkPrime = val => {
  for (let i = 2; i < val; i++) {
    if (val % i === 0) {
      return false;
    }
  }
  return true
}

let target = 13195;
//let target = 600851475143; 
let primeFactors = [];

for (let i = 0; i < target; i++) {
  if (checkFactor(target, i)) {
    if (checkPrime(i)) {
      primeFactors.push(i)
    }
  }
}

console.log(primeFactors);
console.log(primeFactors[primeFactors.length - 1]); 