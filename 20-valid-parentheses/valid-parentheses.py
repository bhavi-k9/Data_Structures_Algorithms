class Solution:
    def isValid(self, s: str) -> bool:

        # push,top,pop,size
        # python  = deque
        # see how to use deque in python
        
        # add openings to stack
        st = deque()

        for i in range(len(s)):   
            if s[i] in '([{':
                st.append(s[i])

            else:
                if not st:  #no opeings for closings
                    return False

                ch = st[-1] ##how to check the position??

                #"()[]{}"
                

                # check each closing to top most opening
                if ((s[i] == ')' and ch == '(') or
                    (s[i] == ']' and ch == '[') or
                    (s[i] == '}' and ch == '{')):

                    st.pop()

        
                # non empty stack return false
                else:
                    return False  

        return not st      




       


       



        