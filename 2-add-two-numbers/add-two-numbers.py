# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        #get sum
        #two pointer
        123    123 567 790
        3 2 1
        567
        7 6 5

        #add nums if greater than 10 what to do
        """
        
        
        
        
        #initiate new list
        dummy = ListNode()
        cur = dummy  

        carry = 0
        while l1 and l2:

            sum = l1.val + l2.val + carry  
            #carry = 0
            digit = sum % 10
            cur.next = ListNode(digit)
            cur = cur.next

            if sum >= 10 :
                carry = 1
            else:
                carry = 0

            l1 = l1.next
            l2 = l2.next    


        #9 and 999 

        while l1:
            
            sum = l1.val + carry  
            #carry = 0
            digit = sum % 10
            cur.next = ListNode(digit)
            cur = cur.next

            if sum >= 10 :
                carry = 1
            else:
                carry = 0

            l1 = l1.next   

        while l2:
            sum = l2.val + carry  
            #carry = 0
            digit = sum % 10
            cur.next = ListNode(digit)
            cur = cur.next

            if sum >= 10 :
                carry = 1
            else:
                carry = 0

            l2 = l2.next 

        if carry != 0:
            cur.next = ListNode(carry)
                

        return  dummy.next    


        #99 99


          
        

        

        