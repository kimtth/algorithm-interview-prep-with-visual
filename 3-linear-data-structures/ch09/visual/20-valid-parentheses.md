# Q20: Valid Parentheses

## Problem Description
Given a string containing just the characters (){}[], determine if the input string is valid (properly paired).

## Core Idea: Stack for Matching Pairs
**Approach:** Push opening brackets onto a stack, and when a closing bracket appears, pop from the stack and check if they match.

## How It Works (Layman's Terms)

Imagine: **Stacking Plates**
- When an opening bracket `(`, `{`, `[` appears → stack a plate
- When a closing bracket `)`, `}`, `]` appears → pop the top plate and check if it matches
- If plates remain at the end → pairs don't match!

Example: `"([])`"
1. `(` → push to stack: `[(]`
2. `[` → push to stack: `[(, []`
3. `]` → pop returns `[`, it matches! ✓
4. `)` → pop returns `(`, it matches! ✓
5. Stack is empty → **Valid!**

## Visualization

👉 [Interactive Visualization (HTML)](./20-valid-parentheses.html)

## Core Code Logic

```python
table = {')': '(', '}': '{', ']': '['}
stack = []

for char in s:
    if char not in table:  # Opening bracket
        stack.append(char)
    elif not stack or table[char] != stack.pop():  # Closing bracket
        return False
return len(stack) == 0
```

## Complexity

- **Time:** O(n) - single pass through the string
- **Space:** O(n) - stack stores up to n/2 elements

## Key Takeaways

1. **Stack's LIFO property** - matches with the most recent opening bracket
2. **Mapping table** - closing bracket → corresponding opening bracket
3. **Edge cases** - pop from empty stack, stack not empty at the end
