# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        head = ListNode(0)
        temp = head
        while list1 is not None and list2 is not None:
            if list1.val < list2.val:
                newNode = ListNode(list1.val)
                list1 = list1.next
            else:
                newNode = ListNode(list2.val)
                list2 = list2.next
            temp.next = newNode
            temp = temp.next
        if list1 is not None:
            temp.next = list1
        if list2 is not None:
            temp.next = list2
        return head.next