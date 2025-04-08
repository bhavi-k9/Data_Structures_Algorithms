# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        '''
        #list [::-1]
        #iterate range(1,1,-1) -- new out
        # inplace j = len(n)
        # 12345
        # 54321 
        #i = 0 j = len[n]-1
             while i < j:
                list[i],list[j] = list[j],list[i]
                 i +=1
                 j -=1

        <1>2>3>4>5
        <1<2 <3 <4 <5
        '''

        prev = None
        cur = head
        temp = None
        while cur != None : 
            temp = cur.next
            cur.next = prev
            prev = cur  #move temp as well
            cur = temp  #how to move cur?

        return prev



        
        