# Q21: Remove Duplicate Letters

## Problem Description
Remove duplicate characters from a string and return the **lexicographically smallest** possible result.

## Core Idea: Stack + Greedy
**Approach:** Push characters onto a stack, but if the current character is lexicographically smaller than the stack top AND the top character appears later in the string, pop it for a better ordering.

## How It Works (Layman''s Terms)

Imagine: **Optimal Business Card Arrangement**
- Each character must appear exactly once
- Prefer a, b, c... order at the front
- But can only rearrange if the same character appears later

Example: `"cbacdcbc"` → Result: `"acdb"`
1. Count each character: c=4, b=2, a=1, d=1
2. ''c'' → stack: [c]
3. ''b'' → b < c and c appears later → remove c, stack: [b]
4. ''a'' → a < b and b appears later → remove b, stack: [a]
5. ''c'' → stack: [a, c]
6. ''d'' → stack: [a, c, d]
7. ''c'' → already in result, skip
8. ''b'' → stack: [a, c, d, b]
9. ''c'' → already in result, skip

## Visualization

👉 [Interactive Visualization (HTML)](./21-remove-duplicate-letters.html)

## Core Code Logic

```python
counter, seen, stack = Counter(s), set(), []

for char in s:
    counter[char] -= 1
    if char in seen:
        continue
    # Pop larger characters that appear later
    while stack and char < stack[-1] and counter[stack[-1]] > 0:
        seen.remove(stack.pop())
    stack.append(char)
    seen.add(char)
```

## Complexity

- **Time:** O(n) - each character pushed/popped at most once
- **Space:** O(1) - at most 26 characters (alphabet)

## Key Takeaways

1. **Greedy choice** - make the best possible decision at each position
2. **Track remaining count** - determines if we can safely remove a character
3. **Seen set** - skip characters already in the result
