class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num <= 1:
            return False
        sum_of_divisors: int = 1
        i: int = 2
 
        while i * i <= num:
            # Only exact divisors can contribute to the divisor sum.
            if num % i == 0:
                # Add the divisor only once when i is the square root of n.
                if i * i == num:
                    sum_of_divisors += i
                else:
                    # Add both paired divisors because both are proper divisors.
                    sum_of_divisors += i + (num // i)
            i += 1
 
        return sum_of_divisors == num
    
        