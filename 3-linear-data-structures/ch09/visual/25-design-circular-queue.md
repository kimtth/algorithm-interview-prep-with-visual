# Q25: Design Circular Queue

## Problem Description
Design a circular queue implementation with fixed size. Support operations: enQueue, deQueue, Front, Rear, isEmpty, isFull.

## Core Idea: Ring Buffer with Pointers
**Approach:** Use two pointers (front and rear) that wrap around the array using modulo arithmetic.

## How It Works (Layman''s Terms)

Imagine: **A Circular Conveyor Belt**
- Fixed number of slots on the belt
- Items added at rear, removed from front
- When reaching the end, wrap back to the beginning
- Full when rear catches up to front

Example: Size 3 queue
```
enQueue(1): [1, _, _] front=0, rear=1
enQueue(2): [1, 2, _] front=0, rear=2
enQueue(3): [1, 2, 3] front=0, rear=0 (wrapped)
deQueue():  [_, 2, 3] front=1, rear=0
enQueue(4): [4, 2, 3] front=1, rear=1 (inserted at position 0)
```

## Visualization

👉 [Interactive Visualization (HTML)](./25-design-circular-queue.html)

## Core Code Logic

```python
class MyCircularQueue:
    def __init__(self, k: int):
        self.q = [None] * k
        self.maxlen = k
        self.front = 0
        self.rear = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.q[self.rear] = value
        self.rear = (self.rear + 1) % self.maxlen
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.q[self.front] = None
        self.front = (self.front + 1) % self.maxlen
        return True

    def Front(self) -> int:
        return -1 if self.isEmpty() else self.q[self.front]

    def Rear(self) -> int:
        return -1 if self.isEmpty() else self.q[self.rear - 1]

    def isEmpty(self) -> bool:
        return self.front == self.rear and self.q[self.front] is None

    def isFull(self) -> bool:
        return self.front == self.rear and self.q[self.front] is not None
```

## Complexity

- **All operations:** O(1)
- **Space:** O(k) - fixed size

## Key Takeaways

1. **Modulo arithmetic** - enables circular wrapping
2. **Distinguish empty vs full** - both have front == rear
3. **Space efficiency** - reuses memory slots
