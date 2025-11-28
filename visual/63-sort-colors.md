# 63. Sort Colors (Dutch National Flag)

## Problem Description
Given an array with n objects colored red (0), white (1), or blue (2), sort them in-place so that objects of the same color are adjacent, in the order red, white, and blue.

## Layman's Explanation
Imagine you have a row of colored balls: 🔴 ⚪ 🔵 mixed randomly. You want to arrange them as:
- All red (0) on the left
- All white (1) in the middle  
- All blue (2) on the right

The **Dutch National Flag algorithm** uses THREE pointers:
1. **red pointer:** Marks where the next red should go (starts at left)
2. **white pointer:** Current ball being examined (starts at left)
3. **blue pointer:** Marks where the next blue should go (starts at right)

Rules:
- If current is RED (0): Swap with red pointer position, move both red and white right
- If current is WHITE (1): Already in the right place, just move white right
- If current is BLUE (2): Swap with blue pointer position, move blue left (don't move white - need to check the swapped value)

## Algorithm Walkthrough
Given: `[2, 0, 2, 1, 1, 0]`

**Initial state:**
```
Index:    0   1   2   3   4   5
Array:   [2,  0,  2,  1,  1,  0]
          ↑                   ↑
         red,white           blue
```

**Step 1:** white=0, value=2 (BLUE) → Swap with blue position
```
Array:   [0,  0,  2,  1,  1,  2]
          ↑               ↑
         r,w            blue
```

**Step 2:** white=0, value=0 (RED) → Swap with red (same position), move both right
```
Array:   [0,  0,  2,  1,  1,  2]
              ↑           ↑
             r,w        blue
```

**Step 3:** white=1, value=0 (RED) → Swap with red position, move both right
```
Array:   [0,  0,  2,  1,  1,  2]
                  ↑       ↑
                 r,w    blue
```

**Step 4:** white=2, value=2 (BLUE) → Swap with blue position
```
Array:   [0,  0,  1,  1,  2,  2]
                  ↑   ↑
                 r,w blue
```

**Step 5:** white=2, value=1 (WHITE) → Just move white right
```
Array:   [0,  0,  1,  1,  2,  2]
                  ↑   ↑   ↑
                  r  w,blue
```

**Step 6:** white=3, value=1 (WHITE) → Move white right, white > blue, STOP!

**Result:** `[0, 0, 1, 1, 2, 2]` ✓

## Code Explanation
```python
def sortColors(self, nums: List[int]) -> None:
    red, white, blue = 0, 0, len(nums) - 1
    
    while white <= blue:
        if nums[white] < 1:  # RED (0)
            nums[red], nums[white] = nums[white], nums[red]
            red += 1
            white += 1
        elif nums[white] > 1:  # BLUE (2)
            nums[white], nums[blue] = nums[blue], nums[white]
            blue -= 1
            # Don't increment white! Need to check swapped value
        else:  # WHITE (1)
            white += 1
```

## Complexity Analysis
- **Time Complexity:** O(n) - Single pass through the array
- **Space Complexity:** O(1) - Only three pointer variables

## Key Insights
1. **Three-way Partition:** Dijkstra's Dutch National Flag algorithm
2. **Invariant Maintained:**
   - Everything left of `red` is RED (0)
   - Everything right of `blue` is BLUE (2)
   - Between `red` and `white-1` is WHITE (1)
3. **Why not increment white on blue swap?** The swapped value could be any color - need to check it!
4. **Generalization:** This pattern extends to any 3-way partitioning problem
