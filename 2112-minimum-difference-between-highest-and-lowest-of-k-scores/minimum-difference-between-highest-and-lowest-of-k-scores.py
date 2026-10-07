class Solution:
    def minimumDifference(self, nums: list[int], k: int) -> int:
    
        nums.sort()
     
        n = len(nums)
        ans = float("inf")
        l = 0
        for r in range(n):
          if (r-l == k):
            l+=1
          if (r-l+1==k):
           
            ans = min(ans,nums[r]-nums[l])
        return ans 
   
