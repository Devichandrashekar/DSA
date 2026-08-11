class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        demo = []
        n = 0
        for i in nums:
            n += i
            demo.append(n)
        return demo
            
               
        
         

