# Q28: Design HashMap

## Problem Description
Design a HashMap without using built-in hash table libraries. Implement put, get, and remove operations.

## Core Idea: Chaining with Linked Lists
**Approach:** Use an array of buckets, each containing a linked list to handle collisions.

## How It Works (Layman''s Terms)

Imagine: **Filing Cabinet with Folders**
- Cabinet has fixed number of drawers (buckets)
- Each item goes to drawer number = key % num_drawers
- Multiple items in same drawer are chained together
- To find: go to correct drawer, search through chain

Example: Size 1000
```
put(1, 10):    bucket 1 → [(1,10)]
put(1001, 20): bucket 1 → [(1,10), (1001,20)]  (collision!)
get(1):        bucket 1 → search → find (1,10) → return 10
remove(1):     bucket 1 → [(1001,20)]
```

## Visualization

👉 [Interactive Visualization (HTML)](./28-design-hashmap.html)

## Core Code Logic

```python
class ListNode:
    def __init__(self, key=-1, val=-1):
        self.key = key
        self.val = val
        self.next = None

class MyHashMap:
    def __init__(self):
        self.size = 1000
        self.table = [ListNode() for _ in range(self.size)]

    def put(self, key: int, value: int):
        node = self.table[key % self.size]
        while node.next:
            if node.next.key == key:
                node.next.val = value
                return
            node = node.next
        node.next = ListNode(key, value)

    def get(self, key: int) -> int:
        node = self.table[key % self.size].next
        while node:
            if node.key == key:
                return node.val
            node = node.next
        return -1

    def remove(self, key: int):
        node = self.table[key % self.size]
        while node.next:
            if node.next.key == key:
                node.next = node.next.next
                return
            node = node.next
```

## Complexity

- **Average case:** O(1) for put/get/remove
- **Worst case:** O(n/k) where k is number of buckets
- **Space:** O(k + n)

## Key Takeaways

1. **Hash function** - distributes keys across buckets
2. **Collision handling** - chaining with linked lists
3. **Sentinel nodes** - simplify insertion/deletion logic
