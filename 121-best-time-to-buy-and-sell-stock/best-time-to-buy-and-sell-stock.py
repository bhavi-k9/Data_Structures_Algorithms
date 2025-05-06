class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        #buy low sell high
        #

        maxp = 0

        for i in range(len(prices)):
            for j in range(i+1,len(prices)):
                p = prices[j] - prices[i]
                maxp = max(p,maxp)

        return maxp   

        '''

        #each time maintain min value
        # [7,1,5,3,6,4]
        #   7,1,1,1,1,1
        # evry time , profit at each , max profit at each

        minx = float('inf')

        maxp = 0

        for i in range(len(prices)):

            minx = min(prices[i],minx)
            p = prices[i] - minx
            maxp = max(p,maxp)

        return maxp    




        
        

