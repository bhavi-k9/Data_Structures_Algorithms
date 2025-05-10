class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        # skip non - alphanumeric and convert upper to lower
        
        s = s.lower() #change to lower

        i = 0
        j = len(s) - 1

        while i <= j:
            if  s[i].isalnum() and s[j].isalnum():
                if s[i] == s[j]:  
                    #mis-used the flow #also did not check each alnum case
                    i += 1
                    j -= 1
                    continue
                else:
                    return False   
            # non alpha has to be skipped
            #only fail if alnum are not equal

            elif not s[i].isalnum():
                i += 1

            elif not s[j].isalnum():
                j -= 1

        return True    
             
