class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        demo = []
        for i in accounts:
            x = 0
            for j in i:
                x +=j
                demo.append(x)
        return max(demo)    
