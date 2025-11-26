# Q29: Jewels and Stones

## Problem Description
Given a string `jewels` representing types of jewels and a string `stones` representing stones you have, count how many of your stones are jewels. Letters are case sensitive.

## Core Idea: Hash Set Lookup
**Approach:** Store jewels in a set, then count stones that exist in the set.

## How It Works (Layman''s Terms)

Imagine: **Sorting Gems from Rocks**
- You have a list of "valuable" gem types (jewels)
- You have a bag of mixed items (stones)
- Check each item: is it in the valuable list?

Example: jewels = "aA", stones = "aAAbbbb"
1. Jewel set: {''a'', ''A''}
2. Check each stone:
   - ''a'' → in set ✓ (count: 1)
   - ''A'' → in set ✓ (count: 2)
   - ''A'' → in set ✓ (count: 3)
   - ''b'' → not in set
   - ''b'' → not in set
   - ''b'' → not in set
   - ''b'' → not in set
3. Result: 3

## Visualization

👉 [Interactive Visualization (HTML)](./29-jewels-and-stones.html)

## Core Code Logic

```python
def numJewelsInStones(jewels: str, stones: str) -> int:
    jewel_set = set(jewels)
    return sum(s in jewel_set for s in stones)
```

Or even more Pythonic:
```python
return sum(s in jewels for s in stones)  # O(j) lookup each time
```

## Complexity

- **Time:** O(j + s) where j = len(jewels), s = len(stones)
- **Space:** O(j) for the jewel set

## Key Takeaways

1. **Set for O(1) lookup** - much faster than linear search in list
2. **Generator expression** - memory efficient counting
3. **Case sensitivity** - ''a'' and ''A'' are different
