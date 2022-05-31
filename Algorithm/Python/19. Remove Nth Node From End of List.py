# Given the head of a linked list,
# remove the nth node from the end of the list and return its head.
# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]

# Input: head = [1], n = 1
# Output: []
from typing import Optional, ListNode
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #find length of the linked list
        currentNode = head
        length = 1
        while currentNode.next != None:
            currentNode = currentNode.next
            length += 1

        #edge case
        if length == n:
            return head.next #which is None. Because the pointer walked to the end in the last while loop

        #find the node to remove
        #index = length - n - 1
        # because we want to find the node before the removed node,
        # and link it to the node after the removed node

        index = length - n - 1
        currentNode = head
        for i in range(index):
            currentNode = currentNode.next
        currentNode.next = currentNode.next.next

        return head
