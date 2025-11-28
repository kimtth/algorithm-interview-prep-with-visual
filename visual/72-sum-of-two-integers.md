# 72. Sum of Two Integers (Without + or -)

## Problem Description
Given two integers `a` and `b`, return the sum of them without using the `+` and `-` operators.

## Layman's Explanation
How do you add numbers when you can't use the `+` operator? Go back to basics - **binary addition**!

When you add two bits:
- 0 + 0 = 0
- 0 + 1 = 1
- 1 + 0 = 1
- 1 + 1 = 10 (which means 0 with a **carry** of 1)

This is exactly what XOR and AND do:
- **XOR (^):** Gives the sum without carry (like adding without the "carry over")
- **AND (&):** Gives where carries happen (both bits are 1)
- **Shift left (<<):** Moves carries to the next position

Keep adding until there are no more carries!

## Algorithm Walkthrough
Given: `a = 3`, `b = 5`

**Binary:**
```
a = 3 = 011
b = 5 = 101
```

**Round 1:**
- Sum without carry: `3 ^ 5 = 011 ^ 101 = 110 = 6`
- Carry: `(3 & 5) << 1 = (001) << 1 = 010 = 2`
- Now add 6 and 2...

**Round 2:**
- Sum without carry: `6 ^ 2 = 110 ^ 010 = 100 = 4`
- Carry: `(6 & 2) << 1 = (010) << 1 = 100 = 4`
- Now add 4 and 4...

**Round 3:**
- Sum without carry: `4 ^ 4 = 000 = 0`
- Carry: `(4 & 4) << 1 = (100) << 1 = 1000 = 8`
- Now add 0 and 8...

**Round 4:**
- Sum without carry: `0 ^ 8 = 8`
- Carry: `(0 & 8) << 1 = 0`
- **Carry is 0, we're done!**

**Result:** 8 = 3 + 5 ✓

## Code Explanation
```python
def getSum(self, a: int, b: int) -> int:
    MASK = 0xFFFFFFFF  # 32-bit mask
    INT_MAX = 0x7FFFFFFF  # Max positive 32-bit int
    
    # Simulate full adder with 32-bit integers
    while b != 0:
        # Sum without carry (XOR)
        temp = (a ^ b) & MASK
        # Carry (AND + shift left)
        b = ((a & b) << 1) & MASK
        a = temp
    
    # Handle negative numbers (two's complement)
    if a > INT_MAX:
        a = ~(a ^ MASK)
    
    return a
```

**Why the mask?** Python integers are arbitrary precision, so we need to simulate 32-bit behavior for proper carry handling and negative numbers.

## Complexity Analysis
- **Time Complexity:** O(1) - At most 32 iterations for 32-bit integers
- **Space Complexity:** O(1) - Only a few variables

## Key Insights
1. **XOR for Bitwise Sum:** `a ^ b` adds each bit position without considering carry
2. **AND for Carry Detection:** `a & b` shows where both bits are 1 (would cause carry)
3. **Left Shift for Carry Position:** Carry goes to the next higher bit position
4. **Repeat Until No Carry:** When carry becomes 0, we're done
5. **32-bit Constraint:** Python needs masking to handle overflow and negative numbers
6. **Full Adder:** This mimics how hardware adds numbers using logic gates!
