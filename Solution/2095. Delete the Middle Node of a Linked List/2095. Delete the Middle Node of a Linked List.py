from typing import Optional

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class ListNode:
     def __init__(self, val=0, next=None):
          self.val = val
          self.next = next

class Solution:
     def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
          if not head or not head.next:
               return None  # If the list is empty or has only one node, return None
          
          dummy = ListNode(next=head)
          slow, fast = dummy, head
          while fast and fast.next:
               slow = slow.next
               fast = fast.next.next
          slow.next = slow.next.next  # Remove the middle node
          return dummy.next