class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

       
        #have maxc
        #curr max, run this till it fails and keep length
        # max of both

        max_len = 0
        i = 0
        
        while i < len(nums):
            cur_len = 0
            while i < len(nums) and nums[i] == 1:
                cur_len += 1
                i += 1

            max_len = max(max_len,cur_len)
            i += 1

        return max_len        


