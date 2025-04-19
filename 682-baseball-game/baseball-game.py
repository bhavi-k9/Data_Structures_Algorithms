class Solution:
    def calPoints(self, operations: List[str]) -> int:
        
        # while interating push/pop
        # you bring certain elements of array closer to each other
        # story of question
        '''
        x > 
        + > add last two record
        D > 2x record
        c > pop(x)

        total sum in end

        '''

        st = deque()

        for i in operations:

            if i == "+" :
                a = st[-1] # 5,10,+ a=10
                b = st[-2] # b = 5
                x =  a + b  #sum
                st.append(x) #it has to be added


            elif i == "D":
                a = st[-1]
                st.append(2*a)  

            elif i == "C":      
                st.pop()

            else  :
                num = int(i)
                st.append(num)

        sumi = 0        

        for num in st:
            sumi = sumi + num

        return sumi    


