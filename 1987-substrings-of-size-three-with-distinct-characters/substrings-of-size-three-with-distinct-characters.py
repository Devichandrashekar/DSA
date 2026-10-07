class Solution:
    def countGoodSubstrings(self, s: str) -> int:

        n = len(s)
        ans = ""
        k = 3
        count = 0
        for i in range(n-k+1):
              temp = []
              for j in range(i,n):
                    temp.append(s[j])
                    if len(temp)==k :
                          if len(set(temp))==k:
                                count+=1
        return count
            
        