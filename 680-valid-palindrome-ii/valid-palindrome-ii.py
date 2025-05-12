class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        #check each charecter has pair
        #more than one charecter miss pair not palindrome


        i = 0
        j = len(s) - 1
        ct = 0

        while i <= j:

            #asbcba
            #check remaining two parts 
            #by removing i or removing j if palindrome
            #one jump
            if  s[i] != s[j]:
                if self.ispali(s, i+1, j):
                    return True
                if self.ispali(s, i, j-1):
                    return True
                else:
                    return False

            i += 1
            j -= 1
                             

        return True    
             

    def ispali(self,s:str,i:int,j:int) -> bool:
        while i <= j:
            if s[i] == s[j]:  
                i += 1
                j -= 1

            else:
                return False

        return True      


        