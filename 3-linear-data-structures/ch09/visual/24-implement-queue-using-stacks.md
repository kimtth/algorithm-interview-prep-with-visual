# Q24: Implement Queue Using Stacks

## Problem Description
Implement a **FIFO (First-In-First-Out) queue** using only two stacks with standard stack operations (push, top, pop, empty).

## Core Idea: Two-Stack Pipeline
**Approach:** Use an input stack for push and an output stack for pop. Transfer elements when output stack is empty.

## How It Works (Layman''s Terms)

Imagine: **Two Boxes of Plates**
- Input box: Stack new plates on top
- Output box: When empty, flip all plates from input box
- This reverses the order twice → original order preserved

Example: push(1), push(2), pop(), push(3), pop()
1. push(1): input=[1], output=[]
2. push(2): input=[1,2], output=[]
3. pop(): output empty → transfer → input=[], output=[2,1] → pop returns 1
4. push(3): input=[3], output=[2]
5. pop(): output not empty → returns 2

## Visualization

👉 [Interactive Visualization (HTML)](./24-implement-queue-using-stacks.html)

## Core Code Logic

```python
class MyQueue:
    def __init__(self):
        self.input = []
        self.output = []

    def push(self, x):
        self.input.append(x)

    def pop(self):
        self.peek()
        return self.output.pop()

    def peek(self):
        if not self.output:
            while self.input:
                self.output.append(self.input.pop())
        return self.output[-1]

    def empty(self):
        return not self.input and not self.output
```

## Complexity

- **Push:** O(1)
- **Pop/Peek:** Amortized O(1) - each element transferred at most once
- **Space:** O(n)

## Key Takeaways

1. **Lazy transfer** - only move elements when output is empty
2. **Amortized analysis** - expensive operations happen infrequently
3. **Double reversal** - two LIFO stacks simulate FIFO queue
