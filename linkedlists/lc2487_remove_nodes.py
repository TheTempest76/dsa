# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNodes(self, head: [ListNode]) -> [ListNode]: # type: ignore
        # the question asks you to keep iterating through the nodes and when you find a node val which is greater than the previous ones then remove all previous ones, do this and return a linked list which contains only the greater ones
        # keep adding values to a stack and when you find a val which is greater than the ones in the stack and pop the rest of em
        # convert the stack into a linked list to return it 

        while head.next:
            s=[]
            while s and s[-1]>head.val:
                s.pop()
            s.append(head.val)
            head = head.next
        return s
s = Solution()
n = ListNode([5,2,13,3,8] , )
s.removeNodes()