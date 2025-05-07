class Solution:
    def frequencySort(self, s: str) -> str:

        hmp = {}
        for i in s:
            hmp[i] = hmp.get(i,0) + 1

        print(hmp)    

        # {'t': 1, 'r': 1, 'e': 2}
        #  rev --> fre to letters

        nhmp = {}

        for key,freq in hmp.items():
            if freq not in nhmp:    
                nhmp[freq] = []
            nhmp[freq].append(key)    
            
        print(nhmp)    
        out = []
        for freq in sorted(nhmp.keys(), reverse=True):
            for i in range(len(nhmp[freq])):
                #append the nuber of times the frequency
                out.append(nhmp[freq][i] * freq)


        return  ''.join(out)            