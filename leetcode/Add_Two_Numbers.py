#TODO: incomplete
'''
https://leetcode.com/problems/add-two-numbers/description/
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.



Example 1:


Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]


Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.
'''
from typing import Optional, List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def list_node_values(self, root, arr=[]):
        if root is None:
            return None
        arr.append(root.val)
        self.list_node_values(root.next, arr)
        return arr

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]):
        result = []
        value_from_l1 = self.list_node_values(l1)
        print(value_from_l1)



if __name__ == '__main__':
    # ListNode{val: 5, next: ListNode{val: 6, next: ListNode{val: 4, next: None}}}
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)

    # ListNode{val: 5, next: ListNode{val: 6, next: ListNode{val: 4, next: None}}}
    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)

    solution = Solution()
    print(solution.addTwoNumbers(l1, l2))
