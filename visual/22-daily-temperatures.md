# Q22: Daily Temperatures

## Problem Description
Given an array of daily temperatures, return an array where each element indicates **how many days until a warmer temperature**. If no warmer day exists, return 0.

## Core Idea: Monotonic Stack
**Approach:** Maintain a stack of indices with decreasing temperatures. When a warmer day appears, pop and calculate the difference.

## How It Works (Layman''s Terms)

Imagine: **A Line of People by Height**
- Each person looks forward for someone taller
- When a taller person appears, all shorter ones find their answer
- Store indices, not values

Example: `[73, 74, 75, 71, 69, 72, 76, 73]`
- Day 0 (73): stack=[0]
- Day 1 (74): 74>73, pop 0, result[0]=1, stack=[1]
- Day 2 (75): 75>74, pop 1, result[1]=1, stack=[2]
- Day 3 (71): stack=[2, 3]
- Day 4 (69): stack=[2, 3, 4]
- Day 5 (72): 72>69, result[4]=1; 72>71, result[3]=2, stack=[2, 5]
- Day 6 (76): 76>72, result[5]=1; 76>75, result[2]=4, stack=[6]

Result: `[1, 1, 4, 2, 1, 1, 0, 0]`

## Visualization

👉 [Interactive Visualization (HTML)](./22-daily-temperatures.html)

## Core Code Logic

```python
answer = [0] * len(T)
stack = []  # indices

for i, cur in enumerate(T):
    while stack and cur > T[stack[-1]]:
        last = stack.pop()
        answer[last] = i - last
    stack.append(i)
```

## Complexity

- **Time:** O(n) - each index pushed/popped once
- **Space:** O(n) - worst case all indices in stack

## Key Takeaways

1. **Monotonic stack pattern** - efficient for "next greater element" problems
2. **Store indices** - calculate distance from index difference
3. **Stack maintains order** - decreasing temperatures in this case
