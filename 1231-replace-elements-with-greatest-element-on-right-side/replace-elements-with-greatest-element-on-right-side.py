class Solution:
    def replaceElements(self, arr: list[int]) -> list[int]:
        
        n=len(arr)
        rmax= -1
        for i in range(n-1,-1,-1):
            temp = arr[i]
            arr[i] = rmax
            rmax = max(rmax,temp)
        return arr
  
     

  
    
    

      
      
    
        