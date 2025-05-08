class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        
        out = []
        seen = set()

        for i in range(len(nums)):
            if nums[i] in seen:
                out.append(nums[i])
            seen.add(nums[i])    

        return out        
        