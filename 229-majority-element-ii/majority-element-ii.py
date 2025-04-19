class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        hmp = {}
        k = len(nums)/3
        out = []

        
        for i in nums:
            hmp[i] = hmp.get(i, 0) + 1


        for key,value in hmp.items():
            if   value > k:
                out.append(key)

        return out        


        