# 84. Different Ways to Add Parentheses

## Problem Description
Given a string expression with numbers and operators (+, -, *), compute all possible results from different ways to group the expression with parentheses.

## Layman's Explanation
Different ways to put parentheses in an expression give different results.

**Example:** `"2-1-1"`

```
(2-1)-1 = 1-1 = 0
2-(1-1) = 2-0 = 2
```

**Result:** `[0, 2]`

**Example:** `"2*3-4*5"`
```
(2*(3-(4*5))) = 2*(3-20) = 2*(-17) = -34
((2*3)-(4*5)) = 6-20 = -14
((2*(3-4))*5) = (2*(-1))*5 = -10
(2*((3-4)*5)) = 2*((-1)*5) = -10
(((2*3)-4)*5) = (6-4)*5 = 10
```

**Result:** `[-34, -14, -10, -10, 10]`

## Algorithm: Divide and Conquer
For each operator, split the expression into left and right parts, recursively compute all results for each part, then combine them.

### Walkthrough: `"2*3-4*5"`

**Split at '*' (position 1):**
- Left: `"2"` → [2]
- Right: `"3-4*5"` → recurse...
  - Split at '-': `"3"` * `"4*5"` = [3] * [20] → [3-20 = -17]
  - Split at '*': `"3-4"` * `"5"` = [-1] * [5] → [-5]
- Combine: 2 * [-17, -5] = [-34, -10]

**Split at '-' (position 3):**
- Left: `"2*3"` → [6]
- Right: `"4*5"` → [20]
- Combine: 6 - 20 = -14

**Split at '*' (position 5):**
- Left: `"2*3-4"` → recurse...
  - [2, 6-4] and [2*3-4] → [2, -4]... actually [-2, 2]
- Right: `"5"` → [5]
- Combine: [-2, 2] * 5 = [-10, 10]

**Final:** `[-34, -14, -10, -10, 10]`

## Code Explanation
```python
def diffWaysToCompute(self, input: str) -> List[int]:
    def compute(left, right, op):
        results = []
        for l in left:
            for r in right:
                results.append(eval(str(l) + op + str(r)))
        return results

    # Base case: single number
    if input.isdigit():
        return [int(input)]

    results = []
    # Try splitting at each operator
    for index, value in enumerate(input):
        if value in "-+*":
            left = self.diffWaysToCompute(input[:index])
            right = self.diffWaysToCompute(input[index + 1:])
            results.extend(compute(left, right, value))
    
    return results
```

**Recursion structure:**
1. **Base case:** If expression is just a number, return it
2. **Divide:** Split at each operator
3. **Conquer:** Recursively solve left and right subproblems
4. **Combine:** Apply operator to all pairs of left and right results

## Complexity Analysis
- **Time Complexity:** O(n × Catalan(n)) - Catalan number of ways to parenthesize
- **Space Complexity:** O(Catalan(n)) - Storing all results

## Key Insights
1. **Operator as split point:** Each operator can be the "last" operation
2. **Recursive structure:** Left and right subexpressions are independent
3. **Cartesian product:** Combine all results from left with all from right
4. **Memoization:** Can add caching to avoid recomputing same subexpressions
5. **Base case:** Single number returns list with just that number
