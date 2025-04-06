# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    
        '''
        #linked list basics
        # basic structure/class>node/how trversal/how deletion
        class Node:
            def __init__(self, data):
                self.data = data
                self.next = None 

        cur =  listnode1
        while(cur != null):
            cur = cur.next    

        cur = head
        prev = None
        while cur and cur.val != key:
            prev = cur
            cur = cur.next

        if cur:  # Found the node
            prev.next = cur.next     
      
        temp = head
        while(temp.next.next = null):
            temp = temp.next           

        # insert at specic position> at end/head/mid
        temp = head
        while(temp.next.next = null):
            temp = temp.next

        if     
            tail.next = listnode4
            tail = listnode4

        cur = head
        prev = None
        count = 0
        while cur and count < pos:
            prev = cur
            cur = cur.next
            count += 1

        if prev:  # Found the node
            prev.next = newnode5
            newnode5.next = cur

        # how to get size of linkedlist
        count = 1
        temp = head
        while temp.next = null :
            count += 1

        # head  node1 > node2 > null
        #       temp1
        # head  node1 > node2 >
        #       temp2

        cur = none
        temp1 = head1
        temp2 = head2

        while temp1.next = null or temp2.next = null:

            if temp1 > temp2:
                cur.next = temp2
                temp2 = temp2.next

            else:
                cur.next = temp1
                temp1 = temp1.next


        '''        

        cur = None
       

        # Dummy node to help with merging
        dummy = ListNode()
        cur = dummy  

        while list1 and list2:  # Use 'and' instead of 'or'
            if list1.val < list2.val:  # Compare values, not nodes
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next  # Move the current pointer forward

        # Attach remaining nodes if any
        if list1:
            cur.next = list1
        if list2:
            cur.next = list2

        return dummy.next