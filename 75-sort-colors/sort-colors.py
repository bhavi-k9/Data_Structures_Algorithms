class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #one pass
        #create a dict -- o(n)
        hmp = {}
        for i in nums:
            hmp[i] = hmp.get(i,0) + 1

        listo = []  
        # 0: 2 1:3 2:1
        #write numbers from dict in particular oredr -- ?? 
        #key.value -- wrong
        for i in range(0,3):
            val = hmp.get(i,0) #to esc key error
            for x in range(val):
                listo.append(i)

        # print(listo)  
        for i  in range(len(nums)):
            nums[i] = listo[i]   


