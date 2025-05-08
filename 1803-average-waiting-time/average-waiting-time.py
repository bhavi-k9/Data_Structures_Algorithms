class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:

        #arr
        #wait
        #iterate over both arr and waiting
        arr = 0
        cooking = customers[0][0]
        wait_time = []

        for i in range(len(customers)):
            arr = customers[i][0]
            if cooking < arr:
                cooking = arr
            cooking = cooking + customers[i][1]
            wait = cooking - arr
            wait_time.append(wait)
        
        print(wait_time)
        sumi = 0
        for i in wait_time:
            sumi = sumi + i

        res = sumi/len(wait_time)

        return res    


        