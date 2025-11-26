# Q26: Design Circular Deque

## Problem Description
Design a circular double-ended queue (deque) with fixed size. Support operations: insertFront, insertLast, deleteFront, deleteLast, getFront, getRear, isEmpty, isFull.

## Core Idea: Doubly Linked List
**Approach:** Use a doubly linked list for O(1) insertion/deletion at both ends, with size tracking.

## How It Works (Layman''s Terms)

Imagine: **A Train with Detachable Cars**
- Add/remove cars from either end (front or back)
- Each car connects to both the one before and after it
- Limited total length (max capacity)

Example: Capacity 3
```
insertFront(1):  [1]
insertLast(2):   [1, 2]
insertFront(3):  [3, 1, 2]
deleteLast():    [3, 1]
insertLast(4):   [3, 1, 4]
```

## Visualization

👉 [Interactive Visualization (HTML)](./26-design-circular-deque.html)

## Core Code Logic

```python
class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.prev = None
        self.next = None

class MyCircularDeque:
    def __init__(self, k: int):
        self.head, self.tail = ListNode(), ListNode()
        self.head.next, self.tail.prev = self.tail, self.head
        self.maxlen, self.len = k, 0

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        node = ListNode(value)
        node.next, node.prev = self.head.next, self.head
        self.head.next.prev, self.head.next = node, node
        self.len += 1
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        self.head.next = self.head.next.next
        self.head.next.prev = self.head
        self.len -= 1
        return True

    def getFront(self) -> int:
        return -1 if self.isEmpty() else self.head.next.val

    def getRear(self) -> int:
        return -1 if self.isEmpty() else self.tail.prev.val

    def isEmpty(self) -> bool:
        return self.len == 0

    def isFull(self) -> bool:
        return self.len == self.maxlen
```

## Complexity

- **All operations:** O(1)
- **Space:** O(k)

## Key Takeaways

1. **Sentinel nodes** - simplify edge cases with dummy head/tail
2. **Doubly linked list** - O(1) operations at both ends
3. **Size tracking** - simpler than checking pointers for full/empty
