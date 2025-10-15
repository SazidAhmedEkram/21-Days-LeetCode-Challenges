## Problem 1: Given head, the head of a linked list, determine if the linked list has a cycle in it.

Problem Link: https://leetcode.com/problems/linked-list-cycle/description/

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

## Problem 2: There is a singly-linked list head and we want to delete a node node in it.

Problem Link: https://leetcode.com/problems/delete-node-in-a-linked-list/description/

You are given the node to be deleted node. You will not be given access to the first node of head.

All the values of the linked list are unique, and it is guaranteed that the given node node is not the last node in the linked list.

Delete the given node. Note that by deleting the node, we do not mean removing it from memory. We mean:

The value of the given node should not exist in the linked list.
The number of nodes in the linked list should decrease by one.
All the values before node should be in the same order.
All the values after node should be in the same order.
Custom testing:

For the input, you should provide the entire linked list head and the node to be given node. node should not be the last node of the list and should be an actual node in the list.
We will build the linked list and pass the node to your function.
The output will be the entire list after calling your function.

## Problem 3: You are given the heads of two sorted linked lists list1 and list2.

Problem Link: https://leetcode.com/problems/merge-two-sorted-lists/description/

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.