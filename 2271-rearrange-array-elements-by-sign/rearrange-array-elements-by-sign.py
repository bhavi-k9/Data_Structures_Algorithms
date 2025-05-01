class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:

        #create two arrays one pos,one neg
        # merge two
        pos = []
        neg = []

        for i in nums:

            if i > 0 :
                pos.append(i)

            else:
                neg.append(i)

        res = []
        for p,n in zip(pos,neg): # check zip statement
            res.append(p)
            res.append(n)

        return res                
        