# Q27: Merge K Sorted Lists

## Problem Description
Merge k sorted linked lists into one sorted linked list and return it.

## Core Idea: Priority Queue (Min-Heap)
**Approach:** Use a min-heap to always extract the smallest element among all list heads.

## How It Works (Layman''s Terms)

Imagine: **Tournament Selection**
- k teams compete, each has players lined up by skill (ascending)
- Always pick the weakest available player from all teams
- That player''s team sends their next player to compete

Example: lists = [[1,4,5], [1,3,4], [2,6]]
1. Heap: [1, 1, 2] → pop 1 (list 0) → result: [1]
2. Heap: [1, 2, 4] → pop 1 (list 1) → result: [1,1]
3. Heap: [2, 3, 4] → pop 2 (list 2) → result: [1,1,2]
4. Continue until all lists exhausted...

Result: [1,1,2,3,4,4,5,6]

## Visualization

👉 [Interactive Visualization (HTML)](./27-merge-k-sorted-lists.html)

## Core Code Logic

```python
def mergeKLists(lists):
    heap = []
    # Initialize: add head of each list
    for i, lst in enumerate(lists):
        if lst:
            heapq.heappush(heap, (lst.val, i, lst))

    root = curr = ListNode()
    while heap:
        val, i, node = heapq.heappop(heap)
        curr.next = node
        curr = curr.next
        if node.next:
            heapq.heappush(heap, (node.next.val, i, node.next))

    return root.next
```

## Complexity

- **Time:** O(n log k) - n total elements, each heap operation is O(log k)
- **Space:** O(k) - heap stores at most k elements

## Key Takeaways

1. **Heap for k-way merge** - efficiently find minimum among k choices
2. **Index as tiebreaker** - prevents comparison errors for equal values
3. **In-place linking** - reuse existing nodes, no extra space for values
