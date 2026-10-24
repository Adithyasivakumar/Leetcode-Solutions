# Here we will declare the s using self and we will the declare the helper function outside

class Solution:
    def validPalindrome(self, s: str) -> bool:

        self.s = s
        
        l, r = 0, len(s) - 1

        while l < r:

            if s[l] == s[r]:
                l += 1
                r -= 1

            else:
                return self.check(l + 1, r) or self.check(l, r - 1)

        return True
    
    # palindrome check
    def check(self, l, r):

        while l < r:

            if self.s[l] != self.s[r]:
                return False

            l += 1
            r -= 1

        return True