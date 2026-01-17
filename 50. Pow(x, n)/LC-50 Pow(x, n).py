#Recursive Approach
class Solution:
    def myPow(self, x: float, n: int) -> float:

        def power(x, n):

            if n == 0:
                return 1
            
            if x == 0:
                return 0

            res = power(x, n // 2)

            res = res * res

            if n % 2 != 0:
                return x * res
            
            else:
                return res     

        res = power(x, abs(n))

        if n >= 0:
            return res
        else:
            return 1 / res