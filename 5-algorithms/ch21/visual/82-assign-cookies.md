# 82. Assign Cookies

## Problem Description
You have children with greed factors `g` and cookies with sizes `s`. A child is content if cookie size ≥ their greed factor. Maximize the number of content children.

## Layman's Explanation
Each child has a minimum cookie size they'll accept (their greed). Each cookie has a size. Match cookies to children to make as many children happy as possible.

**Example:** `g = [1, 2, 3]`, `s = [1, 1]`
- Child 0 wants at least size 1
- Child 1 wants at least size 2
- Child 2 wants at least size 3
- We have two size-1 cookies

Only Child 0 can be satisfied (size 1 ≥ greed 1).

**Result:** 1

**Greedy Strategy:** 
1. Sort both arrays
2. Give smallest sufficient cookie to least greedy child

## Algorithm Walkthrough
Given: `g = [1, 2, 3]`, `s = [1, 2, 3]`

After sorting:
- Children (greed): [1, 2, 3]
- Cookies (size): [1, 2, 3]

| Child | Greed | Cookie | Size | Match? |
|-------|-------|--------|------|--------|
| 0     | 1     | 0      | 1    | Yes! 1≥1 |
| 1     | 2     | 1      | 2    | Yes! 2≥2 |
| 2     | 3     | 2      | 3    | Yes! 3≥3 |

**Result:** 3 content children

**Another example:** `g = [1, 2]`, `s = [1, 2, 3]`
- Child 0 (greed 1) ← Cookie 0 (size 1) ✓
- Child 1 (greed 2) ← Cookie 1 (size 2) ✓
- Cookie 2 (size 3) unused

**Result:** 2

## Why Greedy Works
- **Least greedy first:** The least greedy child can be satisfied by the smallest cookies
- **Don't waste big cookies:** Giving a size-3 cookie to a child who only needs 1 wastes potential
- **Optimal substructure:** Each greedy choice leaves an optimal subproblem

## Code Explanation
```python
def findContentChildren(self, g: List[int], s: List[int]) -> int:
    g.sort()  # Sort children by greed
    s.sort()  # Sort cookies by size
    
    child_i = cookie_j = 0
    
    while child_i < len(g) and cookie_j < len(s):
        if s[cookie_j] >= g[child_i]:
            # This cookie satisfies this child
            child_i += 1
        # Move to next cookie (whether used or not)
        cookie_j += 1
    
    return child_i  # Number of satisfied children
```

**Key logic:**
- If current cookie satisfies current child → both pointers advance
- If current cookie is too small → only cookie pointer advances (skip this cookie)

## Complexity Analysis
- **Time Complexity:** O(n log n + m log m) for sorting, O(n + m) for matching
- **Space Complexity:** O(1) extra space (in-place sort)

## Key Insights
1. **Sort both arrays:** Essential for greedy matching
2. **Two-pointer technique:** Move through both arrays together
3. **Don't skip children:** A child is skipped only if no cookie works
4. **Skip small cookies:** If a cookie can't satisfy least greedy remaining child, it's useless
5. **Greedy proof:** Using minimum sufficient cookie for each child is optimal
