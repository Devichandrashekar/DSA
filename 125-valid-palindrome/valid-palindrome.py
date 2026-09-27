class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(char.lower() for char in s if char.isalnum())
        n = len(s) // 2
        mu = len(s)
        valid = True
        for i in range(n):
            l = s[i]
            r = s[mu - i - 1]
            if l != r:
                valid = False
                
        if valid:
            return True
        else:
            return False
