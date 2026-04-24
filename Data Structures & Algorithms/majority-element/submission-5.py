class Solution:
    def majorityElement(self, nums: List[int]) -> int:
       count={}
       maxCount=0
       res=0
       for i in nums:
           count[i]=count.get(i,0)+1
           if count[i]>maxCount:
              maxCount=count[i]
              res=i
       return res
            