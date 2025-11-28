# 71. Hamming Distance

## Problem Description
The Hamming distance between two integers is the number of positions at which the corresponding bits are different. Given two integers `x` and `y`, return the Hamming distance.

## Layman's Explanation
Imagine two binary strings representing two numbers:
```
x = 1 (binary: 0001)
y = 4 (binary: 0100)
```

**Question:** In how many bit positions do they differ?

Compare position by position:
```
0001
0100
↑ ↑   ← Different at positions 0 and 2
```

**Answer:** 2 differences = Hamming distance of 2

**The XOR Trick:**
XOR gives 1 where bits differ, 0 where they're the same!
```
0001 XOR 0100 = 0101
                ↑ ↑   ← The 1s show where differences are!
```

Just count the 1s in the XOR result!

## Algorithm Walkthrough
Given: `x = 1`, `y = 4`

**Step 1: XOR the numbers**
```
x = 1 = 0001
y = 4 = 0100
        ----
x^y   = 0101
```

**Step 2: Count the 1s**
- `0101` has two 1s
- Hamming distance = 2 ✓

**Another example:** `x = 3`, `y = 1`
```
x = 3 = 011
y = 1 = 001
        ---
x^y   = 010  ← One bit different
```
Hamming distance = 1

## Code Explanation
```python
def hammingDistance(self, x: int, y: int) -> int:
    return bin(x ^ y).count('1')
```

Breaking it down:
1. `x ^ y` - XOR to get bits that differ
2. `bin(...)` - Convert to binary string (e.g., "0b101")
3. `.count('1')` - Count the 1s

**Alternative using bit manipulation:**
```python
def hammingDistance(self, x: int, y: int) -> int:
    xor = x ^ y
    count = 0
    while xor:
        count += xor & 1  # Check last bit
        xor >>= 1         # Shift right
    return count
```

**Brian Kernighan's algorithm (fastest):**
```python
def hammingDistance(self, x: int, y: int) -> int:
    xor = x ^ y
    count = 0
    while xor:
        xor &= (xor - 1)  # Remove rightmost 1
        count += 1
    return count
```

## Complexity Analysis
- **Time Complexity:** O(1) - Fixed 32 bits for integers
- **Space Complexity:** O(1) - Only a few variables

## Key Insights
1. **XOR for Differences:** XOR produces 1 exactly where bits differ
2. **Population Count:** Counting 1s is called "popcount" or "bit count"
3. **Built-in Methods:** Python's `bin().count('1')` is concise but creates a string
4. **Brian Kernighan:** `n & (n-1)` removes the rightmost 1 bit, making counting faster
5. **Applications:** Error detection/correction codes, similarity metrics
