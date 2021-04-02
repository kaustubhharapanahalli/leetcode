###############################################################################
# SOLUTION 1
###############################################################################
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num1 = self.fetch_vals(l1)
        num2 = self.fetch_vals(l2)
        sum_ = num1 + num2

        len_ = len(str(sum_))
        val = None
        flag = True

        for n in str(sum_):
            val = ListNode(n, val)

        return val

    def fetch_vals(self, l: ListNode) -> List:
        tmp = 0
        exp = 0
        while l.next != None:
            val, l = l.val, l.next
            tmp += val * (10 ** exp)
            exp += 1

        tmp += l.val * (10 ** exp)

        return tmp


###############################################################################
# SOLUTION 2
###############################################################################
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        res = n = ListNode(0)
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            carry, val = divmod(carry, 10)
            n.next = n = ListNode(val)
        return res.next
