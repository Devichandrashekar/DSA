class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:

        n = len(nums)
        ans = []
        for i in range(n):
          if nums[i] not in ans:
            ans.append(nums[i])
        k = len(ans)
        for i in range(k):
            nums[i] = ans[i]
        return k
        
        
  
        