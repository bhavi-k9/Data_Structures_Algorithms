class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # words with same letter frq together

        #freq first  hmp1 = hmp2 
        #sorting
        #aet
        #aet
        #aet
        #atn
        #atn
        
        out = []
        for  i in range(len(strs)):

            l = list(strs[i])
            l.sort()
            x = "".join(l)
            out.append([x,i])   # how to not lose the position

        out.sort()
        print(out)

        #iterate and get group,help of index
        i = 0
        res = []
        while i < len(out):
            temp = []
            cur = out[i][0]
            while i < len(out) and cur == out[i][0]:
                    #i == 0 or (out[i][0] == out[i+1][0]):
                x = out[i][1]
                temp.append(strs[x])
                i += 1

            res.append(temp)    
               
        return res       






        




       
        
       

        