# 73. UTF-8 Validation

## Problem Description
Given an array of integers representing bytes, determine if it's a valid UTF-8 encoding.

## Layman's Explanation
UTF-8 is a way to encode text where characters can use 1-4 bytes. Each character follows specific patterns:

| Bytes | First Byte Pattern | Continuation Bytes |
|-------|--------------------|--------------------|
| 1     | `0xxxxxxx`         | None               |
| 2     | `110xxxxx`         | `10xxxxxx`         |
| 3     | `1110xxxx`         | `10xxxxxx` × 2     |
| 4     | `11110xxx`         | `10xxxxxx` × 3     |

**Rules:**
1. **First byte** tells you how many bytes the character uses
2. **Continuation bytes** always start with `10`
3. Each integer represents ONE byte (so we only care about the lower 8 bits)

**Example:** `[197, 130, 1]`
- 197 = `11000101` → starts with `110` → 2-byte character, need 1 continuation
- 130 = `10000010` → starts with `10` → valid continuation!
- 1 = `00000001` → starts with `0` → valid 1-byte character

All valid! ✓

## Algorithm Walkthrough
Given: `data = [197, 130, 1]`

**Step 1: Check byte 197**
```
197 = 11000101
      ↑↑↑
      110 → This starts a 2-byte sequence
```
Expect 1 continuation byte.

**Step 2: Check byte 130**
```
130 = 10000010
      ↑↑
      10 → Valid continuation byte!
```
2-byte character complete.

**Step 3: Check byte 1**
```
1 = 00000001
    ↑
    0 → 1-byte character (ASCII)
```

**Result:** All bytes validated! Return `True` ✓

**Invalid example:** `[235, 140, 4]`
- 235 = `11101011` → starts with `1110` → 3-byte, need 2 continuations
- 140 = `10001100` → valid continuation (1 of 2)
- 4 = `00000100` → NOT `10...` → Invalid! ✗

## Code Explanation
```python
def validUtf8(self, data: List[int]) -> bool:
    def check(size):
        # Verify 'size' continuation bytes all start with 10
        for i in range(start + 1, start + size + 1):
            if i >= len(data) or (data[i] >> 6) != 0b10:
                return False
        return True

    start = 0
    while start < len(data):
        first = data[start]
        
        if (first >> 3) == 0b11110 and check(3):      # 4-byte
            start += 4
        elif (first >> 4) == 0b1110 and check(2):     # 3-byte
            start += 3
        elif (first >> 5) == 0b110 and check(1):      # 2-byte
            start += 2
        elif (first >> 7) == 0:                        # 1-byte
            start += 1
        else:
            return False
    
    return True
```

**Key bit operations:**
- `first >> 7` - Check if top bit is 0 (1-byte char)
- `first >> 5` - Check top 3 bits for `110` (2-byte char)
- `first >> 4` - Check top 4 bits for `1110` (3-byte char)
- `first >> 3` - Check top 5 bits for `11110` (4-byte char)
- `data[i] >> 6` - Check top 2 bits for `10` (continuation)

## Complexity Analysis
- **Time Complexity:** O(n) - Single pass through the array
- **Space Complexity:** O(1) - Only pointers and counters

## Key Insights
1. **UTF-8 Structure:** Leading 1s in first byte count total bytes; continuations are `10xxxxxx`
2. **Bit Shifting:** Right-shift to check prefix bits without masking
3. **Only Lower 8 Bits:** Input integers may have more than 8 bits; use masking if needed
4. **Order Matters:** Check 4-byte pattern before 3-byte, etc. (longer patterns first)
5. **Invalid Cases:** First byte pattern doesn't exist, or not enough continuation bytes
