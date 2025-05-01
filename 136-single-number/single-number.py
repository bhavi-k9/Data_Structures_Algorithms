class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        hmp = {}
        for i in nums:
            hmp[i] = hmp.get(i,0) + 1

        
        for key,value in hmp.items():

            if value < 2:
                return key