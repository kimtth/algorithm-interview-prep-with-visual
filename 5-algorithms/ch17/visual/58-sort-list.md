# Problem 58: Sort List

## Visualization
[View Interactive Visualization](./58-sort-list.html)

## Problem Statement
Given the head of a linked list, return the list sorted in ascending order using O(n log n) time complexity.

## Layman's Explanation
Sorting a linked list efficiently requires **Merge Sort** - a divide-and-conquer approach. We split the list in half using the slow/fast runner technique, recursively sort each half, then merge them back together. Think of it like organizing a deck of cards by repeatedly splitting and combining sorted piles.

## Step-by-Step Walkthrough
1. **Find Middle**: Use slow/fast pointers to find the middle
2. **Split**: Disconnect the first half from the second
3. **Recurse**: Sort left half, sort right half
4. **Merge**: Combine two sorted halves into one sorted list
5. **Base Case**: Single node or empty is already sorted

## Visual Example
```
Original: 4 → 2 → 1 → 3

Split:
[4 → 2] and [1 → 3]

Recurse:
[4] [2] → merge → [2 → 4]
[1] [3] → merge → [1 → 3]

Final merge:
[2 → 4] + [1 → 3] → [1 → 2 → 3 → 4]
```

## Code Snippet
```python
def sortList(self, head: ListNode) -> ListNode:
    if not (head and head.next):
        return head

    # 런너 기법 활용
    half, slow, fast = None, head, head
    while fast and fast.next:
        half, slow, fast = slow, slow.next, fast.next.next
    half.next = None

    # 분할 재귀 호출
    l1 = self.sortList(head)
    l2 = self.sortList(slow)

    return self.mergeTwoLists(l1, l2)
```

## Complexity Analysis
- **Time Complexity**: O(n log n) - divide by 2 each time, merge is O(n)
- **Space Complexity**: O(log n) - recursion stack depth
