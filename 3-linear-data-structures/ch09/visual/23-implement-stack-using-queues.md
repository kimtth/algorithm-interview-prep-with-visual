# Q23: Implement Stack Using Queues

## Problem Description
Implement a **LIFO (Last-In-First-Out) stack** using only two queues with standard queue operations (push, peek, pop, empty).

## Core Idea: Queue Rotation
**Approach:** After each push, rotate the queue so the newest element is at the front.

## How It Works (Layman''s Terms)

Imagine: **A Single-File Line Rearrangement**
- Queue: First person in line gets served first (FIFO)
- Stack: Last person in line gets served first (LIFO)
- Solution: After new person joins, everyone in front moves to the back

Example: Push 1, 2, 3
1. Push 1: q=[1]
2. Push 2: q=[1,2] → rotate 1 time → q=[2,1]
3. Push 3: q=[2,1,3] → rotate 2 times → q=[3,2,1]

Now pop returns 3, then 2, then 1 - Stack behavior!

## Visualization

👉 [Interactive Visualization (HTML)](./23-implement-stack-using-queues.html)

## Core Code Logic

```python
class MyStack:
    def __init__(self):
        self.q = collections.deque()

    def push(self, x):
        self.q.append(x)
        # Rotate: move all previous elements to the back
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())

    def pop(self):
        return self.q.popleft()

    def top(self):
        return self.q[0]

    def empty(self):
        return len(self.q) == 0
```

## Complexity

- **Push:** O(n) - rotate all existing elements
- **Pop/Top/Empty:** O(1)
- **Space:** O(n)

## Key Takeaways

1. **Rotation technique** - transforms FIFO to LIFO
2. **Trade-off** - O(n) push enables O(1) pop
3. **Alternative** - could make pop O(n) and push O(1) instead
