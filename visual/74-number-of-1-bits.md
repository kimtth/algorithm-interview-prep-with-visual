# 74. Number of 1 Bits (Hamming Weight)

## Problem Description
Given an unsigned integer, return the number of '1' bits it has (also known as the Hamming weight).

## Layman's Explanation
We want to count how many 1s are in the binary representation of a number.

**Example:** n = 11
```
11 in binary = 00001011
                    ↑ ↑↑
Count of 1s = 3
```

**Simple approach:** Convert to binary string and count '1's
```python
bin(11) = '0b1011'
bin(11).count('1') = 3
```

**Bit manipulation approach:** Use `n & 1` to check last bit, then right-shift
```
1011 & 1 = 1  (count = 1)
 101 & 1 = 1  (count = 2)
  10 & 1 = 0  (count = 2)
   1 & 1 = 1  (count = 3)
   0      → done!
```

## Algorithm Walkthrough
Given: `n = 11` (binary: `1011`)

### Method 1: String Counting
```
bin(11) = '0b1011'
'0b1011'.count('1') = 3
```
Done! Simple and readable.

### Method 2: Bit Manipulation
| Step | n (binary) | n & 1 | Count |
|------|------------|-------|-------|
| 1    | `1011`     | 1     | 1     |
| 2    | `0101`     | 1     | 2     |
| 3    | `0010`     | 0     | 2     |
| 4    | `0001`     | 1     | 3     |
| 5    | `0000`     | -     | done! |

**Result:** 3

### Method 3: Brian Kernighan's Algorithm
This clever trick clears the rightmost 1-bit in each iteration:
```
n = n & (n - 1)
```

| Step | n      | n - 1  | n & (n-1) | Count |
|------|--------|--------|-----------|-------|
| 1    | `1011` | `1010` | `1010`    | 1     |
| 2    | `1010` | `1001` | `1000`    | 2     |
| 3    | `1000` | `0111` | `0000`    | 3     |
| 4    | `0000` | -      | done!     | 3     |

**Why it works:** `n - 1` flips all bits from the rightmost 1-bit to the end.
ANDing with n clears that rightmost 1-bit.

## Code Explanation

### Solution 1: Built-in
```python
def hammingWeight(self, n: int) -> int:
    return bin(n).count('1')
```

### Solution 2: Bit-by-bit
```python
def hammingWeight(self, n: int) -> int:
    count = 0
    while n:
        count += n & 1  # Add 1 if last bit is 1
        n >>= 1         # Shift right
    return count
```

### Solution 3: Brian Kernighan
```python
def hammingWeight(self, n: int) -> int:
    count = 0
    while n:
        n &= (n - 1)    # Clear rightmost 1-bit
        count += 1
    return count
```

## Complexity Analysis
- **Time Complexity:** 
  - Method 1 & 2: O(log n) or O(32) for 32-bit integers
  - Method 3: O(k) where k is the number of 1-bits
- **Space Complexity:** O(1)

## Key Insights
1. **n & 1:** Extracts the least significant bit (0 or 1)
2. **n >> 1:** Right shift divides by 2, moves to next bit
3. **n & (n-1):** Clears the rightmost 1-bit (Brian Kernighan's trick)
4. **Trade-offs:** Built-in is cleanest; Kernighan is fastest for sparse bits
5. **Applications:** Error detection, cryptography, data compression
