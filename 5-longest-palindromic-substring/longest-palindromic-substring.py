class Solution:
    def longestPalindrome(self, s: str) -> str:

        #how to check end points
        #index is center
        #every point as center
        #check either sides - odd
        # abccba - even two point
        # odd even is not about len(s) its about palindrome possibility
        
      
        
        out = ''
         
        for x in range(len(s)):
            i = x-1
            j = x+1
            while i >= 0 and j < len(s):
                
                if s[i] == s[j]:  
                    i -= 1
                    j += 1

                else:
                    break
        
            ans = s[i+1:j]    
            if len(ans) > len(out):
                out = ans

                   
        # abcba  abccba
        # abbad

        for x in range(len(s)):
            i = x
            j = x+1
            while i >= 0 and j < len(s):
                
                if s[i] == s[j]:  
                    i -= 1
                    j += 1

                else:
                    break

            ans = s[i+1:j]    
            if len(ans) > len(out):
                out = ans

        return out       

    


            
            

            
            
