# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        a = []
        curr_node = head
        
        while (curr_node != None):
            a.append(curr_node.val)
            curr_node = curr_node.next
            
        if a[:] == a[::-1]:
            return True
        else:
            return False
