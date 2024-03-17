'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]

Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]

 
'''
class node:
    def __init__(self , val=0 , next=None):
        self.val = val
        self.next = next

class sol:
    def add(self , l1 , l2):
        '''
        Make node to start linked list of total of each digit

        traverse through l1 and l2

        have a total of elements
        
        have carry which persists through to the next iteration and then add it to the latest total val
        '''

        dummy = node()
        r = dummy # points to the head of the sum linked list 
        carry = 0
        total = 0
        while l1 or l2 or carry:
            total = carry
            if l1: # while moving from one node to the next the linked list reaches last node and then val becomes None that's when the statement evals to true
                total += l1.val
                l1 = l1.next
            if l2:
                total += l2.val
                l2 = l2.next
            carry = total // 10
            num = total % 10
            dummy.next = node(num)
            dummy = dummy.next
        return r.next

    


def list_to_linked_list(lst):
    dummy = node()
    current = dummy
    for val in lst:
        current.next = node(val)
        current = current.next
    return dummy.next

# Test
l1 = [9,9,9,9,9,9,9]
l2 = [9,9,9,9]
soll = sol()
l1_linked_list = list_to_linked_list(l1)
l2_linked_list = list_to_linked_list(l2)
result_linked_list = soll.add(l1_linked_list, l2_linked_list)

# Print the result linked list
while result_linked_list:
    print(result_linked_list.val, end="->")
    result_linked_list = result_linked_list.next