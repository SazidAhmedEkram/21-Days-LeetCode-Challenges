# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeTwoLists(self, list1, list2):
        head1 = list1
        head2 = list2
        head3 = ListNode(0)
        check = head3

        while head1 is not None and head2 is not None:
            if head1.val < head2.val:
                newNode = ListNode(head1.val)
                head1 = head1.next
            else:
                newNode = ListNode(head2.val)
                head2 = head2.next
            check.next = newNode
            check = check.next

        if head1 is not None:
            check.next = head1
        if head2 is not None:
            check.next = head2
        return head3.next


solution = Solution()
firstNode = ListNode(1)
secondNode = ListNode(2)
thirdNode = ListNode(4)
firstNode.next = secondNode
secondNode.next = thirdNode


firstNode2 = ListNode(1)
secondNode2 = ListNode(3)
thirdNode2 = ListNode(4)
firstNode2.next = secondNode2
secondNode2.next = thirdNode2

print(solution.mergeTwoLists(firstNode, firstNode2))
