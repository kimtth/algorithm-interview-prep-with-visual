# 65. Binary Search

## Problem Description
Given a sorted array of integers `nums` and a target value `target`, return the index if the target is found. If not, return -1.

## Layman's Explanation
Think of a phone book with names in alphabetical order. To find "Smith":
1. **Open to the middle** - Let's say you see "Miller"
2. **Is "Smith" before or after "Miller"?** - After! So ignore the first half
3. **Open to the middle of the remaining pages** - Maybe "Robinson"
4. **Keep halving** until you find "Smith" or run out of pages

This is the essence of **binary search** - eliminate half the remaining options with each comparison!

**Why it's powerful:**
- Linear search through 1,000 items: up to 1,000 checks
- Binary search through 1,000 items: at most 10 checks! (log₂1000 ≈ 10)

## Algorithm Walkthrough
Given: `nums = [-1, 0, 3, 5, 9, 12]`, `target = 9`

**Step 1:**
```
Array: [-1, 0, 3, 5, 9, 12]
        L        M        R
        0        2        5
```
- mid = (0+5)//2 = 2
- nums[2] = 3 < 9 → target is in RIGHT half
- Move left to mid+1

**Step 2:**
```
Array: [-1, 0, 3, 5, 9, 12]
                 L  M     R
                 3  4     5
```
- mid = (3+5)//2 = 4
- nums[4] = 9 == 9 → **FOUND!**

**Result:** Return index 4 ✓

## Code Explanation
```python
def search(self, nums: List[int], target: int) -> int:
    def binary_search(left, right):
        if left <= right:  # Base case: valid range
            mid = (left + right) // 2
            
            if nums[mid] < target:
                # Target is in right half
                return binary_search(mid + 1, right)
            elif nums[mid] > target:
                # Target is in left half
                return binary_search(left, mid - 1)
            else:
                # Found it!
                return mid
        else:
            # Range is empty, target not found
            return -1
    
    return binary_search(0, len(nums) - 1)
```

## Complexity Analysis
- **Time Complexity:** O(log n) - We halve the search space each step
- **Space Complexity:** O(log n) for recursive, O(1) for iterative version

## Key Insights
1. **Prerequisite:** Array MUST be sorted!
2. **Halving:** Each step eliminates half the remaining elements
3. **Termination:** When left > right, the range is empty
4. **Overflow Prevention:** Use `mid = left + (right - left) // 2` to avoid integer overflow in some languages
5. **Off-by-one Errors:** Be careful with `left <= right` vs `left < right` and `mid ± 1`
