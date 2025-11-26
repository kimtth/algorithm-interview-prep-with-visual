# 68. Two Sum II - Input Array Is Sorted

## Problem Description
Given a **sorted** array of integers `numbers` and a `target`, find two numbers such that they add up to the target. Return their **1-indexed** positions.

## Layman's Explanation
Imagine you have a sorted row of cards with different point values, and you need to pick exactly TWO cards that add up to a target score.

**The Two-Pointer Strategy:**
1. Start with one finger on the **leftmost** (smallest) card
2. Put another finger on the **rightmost** (largest) card
3. Calculate the sum:
   - **Too small?** Move the left finger right (need a bigger number)
   - **Too big?** Move the right finger left (need a smaller number)
   - **Just right?** Found it!

Because the array is sorted, this works perfectly - you're adjusting in the right direction each time!

## Algorithm Walkthrough
Given: `numbers = [2, 7, 11, 15]`, `target = 9`

**Step 1:**
```
Array:  [2,  7,  11, 15]
         ↑           ↑
        left       right
```
- sum = 2 + 15 = 17
- 17 > 9 → Too big! Move right pointer left.

**Step 2:**
```
Array:  [2,  7,  11, 15]
         ↑       ↑
        left   right
```
- sum = 2 + 11 = 13
- 13 > 9 → Still too big! Move right pointer left.

**Step 3:**
```
Array:  [2,  7,  11, 15]
         ↑   ↑
        left right
```
- sum = 2 + 7 = 9
- 9 == 9 → **FOUND!**

**Result:** Return `[1, 2]` (1-indexed positions)

## Code Explanation
```python
def twoSum(self, numbers: List[int], target: int) -> List[int]:
    left, right = 0, len(numbers) - 1
    
    while not left == right:  # or: while left < right
        current_sum = numbers[left] + numbers[right]
        
        if current_sum < target:
            left += 1   # Need bigger sum, move left right
        elif current_sum > target:
            right -= 1  # Need smaller sum, move right left
        else:
            # Return 1-indexed positions
            return left + 1, right + 1
```

## Complexity Analysis
- **Time Complexity:** O(n) - Each pointer moves at most n times total
- **Space Complexity:** O(1) - Only two pointer variables

## Key Insights
1. **Sorted Array is Key:** Two pointers only work because the array is sorted!
2. **Why it works:** 
   - If sum is too small, the only way to increase it is to pick a larger left value
   - If sum is too big, the only way to decrease it is to pick a smaller right value
3. **One-indexed Output:** The problem uses 1-based indexing (add 1 to results)
4. **Exactly One Solution:** Problem guarantees exactly one valid pair exists
5. **Comparison to Hash Table:** Two pointers use O(1) space vs O(n) for hash table approach
