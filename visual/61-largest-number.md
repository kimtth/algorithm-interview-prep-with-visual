# 61. Largest Number

## Problem Description
Given a list of non-negative integers, arrange them such that they form the largest number. Return the result as a string (since the number could be very large).

## Layman's Explanation
Imagine you have number tiles and want to arrange them to make the biggest possible number. For example, with [3, 30, 34]:
- Option 1: 3-30-34 = 33034
- Option 2: 3-34-30 = 33430
- Option 3: 30-3-34 = 30334
- Option 4: 30-34-3 = 30343
- Option 5: 34-3-30 = 34330 ← **Winner!**
- Option 6: 34-30-3 = 34303

The trick is **not** just comparing numbers directly (34 > 30 > 3), but comparing what happens when you concatenate them!

**Key Insight:** Compare "AB" vs "BA"
- For 3 and 30: "330" vs "303" → "330" > "303" → 3 comes first!
- For 3 and 34: "334" vs "343" → "343" > "334" → 34 comes first!
- For 34 and 30: "3430" vs "3034" → "3430" > "3034" → 34 comes first!

## Algorithm Walkthrough
Given: `[3, 30, 34, 5, 9]`

**Step 1: Convert to strings**
- `["3", "30", "34", "5", "9"]`

**Step 2: Custom sort using concatenation comparison**
- Compare by checking `a+b` vs `b+a`
- Example: "3" vs "30" → "330" vs "303" → "330" wins → "3" before "30"

**Step 3: Sort result**
- After sorting: `["9", "5", "34", "3", "30"]`

**Step 4: Join and handle edge case**
- Join: `"9534330"`
- Edge case: If result starts with "0", return "0" (all zeros input)

**Result:** `"9534330"` ✓

## Code Explanation
```python
from functools import cmp_to_key

def largestNumber(self, nums: List[int]) -> str:
    # Custom comparator: compare a+b vs b+a
    def compare(n1, n2):
        # Return negative if n1 should come first
        # Return positive if n2 should come first
        if str(n1) + str(n2) > str(n2) + str(n1):
            return -1  # n1 comes first
        else:
            return 1   # n2 comes first
    
    # Sort using custom comparator
    nums.sort(key=cmp_to_key(compare))
    
    # Join and handle all-zeros case
    result = ''.join(map(str, nums))
    return result if result[0] != '0' else '0'
```

## Complexity Analysis
- **Time Complexity:** O(n log n) - Sorting dominates, each comparison is O(k) where k is digit length
- **Space Complexity:** O(n) - Space for string conversion

## Key Insights
1. **Concatenation Comparison:** The key is comparing `a+b` vs `b+a`, not just `a` vs `b`
2. **cmp_to_key:** Python 3 requires this to use old-style comparator with `sort()`
3. **Edge Case:** All zeros should return "0", not "0000..."
4. **Transitivity:** If a > b and b > c, then a > c (this comparison is transitive!)
