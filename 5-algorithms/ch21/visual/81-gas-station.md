# 81. Gas Station

## Problem Description
There are `n` gas stations along a circular route. Station `i` has `gas[i]` fuel and costs `cost[i]` to travel to the next station. Find the starting station index to complete the circuit, or return -1 if impossible.

## Layman's Explanation
You're driving around a circular road with gas stations. At each station, you fill up some gas and then use some gas to reach the next station. Can you find a starting point that lets you complete the full circle?

**Example:** `gas = [1,2,3,4,5]`, `cost = [3,4,5,1,2]`

```
Station:  0    1    2    3    4
Gas:      1    2    3    4    5
Cost:     3    4    5    1    2
Net:     -2   -2   -2   +3   +3
```

Starting from station 3:
- Station 3: +4 gas, -1 cost → tank = 3
- Station 4: +5 gas, -2 cost → tank = 6
- Station 0: +1 gas, -3 cost → tank = 4
- Station 1: +2 gas, -4 cost → tank = 2
- Station 2: +3 gas, -5 cost → tank = 0 ✓

**Result:** 3

## Algorithm Walkthrough

### Key Insight
If total gas ≥ total cost, a solution exists!

**Why?** If overall you have enough gas, then there must be a starting point where you never run out.

### Greedy Approach
1. Track running sum of `gas[i] - cost[i]`
2. If sum goes negative at station i, start fresh from i+1
3. Continue until you find a valid start

**Given:** `gas = [1,2,3,4,5]`, `cost = [3,4,5,1,2]`

| Station | gas-cost | Running Sum | Action |
|---------|----------|-------------|--------|
| 0       | -2       | -2          | Reset, try from 1 |
| 1       | -2       | -2          | Reset, try from 2 |
| 2       | -2       | -2          | Reset, try from 3 |
| 3       | +3       | 3           | Keep going |
| 4       | +3       | 6           | Keep going |

**Start = 3** ✓

## Code Explanation

### Solution 1: Brute Force
```python
def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
    for start in range(len(gas)):
        fuel = 0
        for i in range(start, len(gas) + start):
            index = i % len(gas)
            if gas[index] + fuel < cost[index]:
                break
            fuel += gas[index] - cost[index]
        else:
            return start
    return -1
```

### Solution 2: Greedy O(n)
```python
def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
    if sum(gas) < sum(cost):
        return -1
    
    start = 0
    fuel = 0
    
    for i in range(len(gas)):
        fuel += gas[i] - cost[i]
        if fuel < 0:
            start = i + 1
            fuel = 0
    
    return start
```

**Key:** If we can't reach station i+1 from start, then any station between start and i also can't work (because we arrive there with positive fuel and still fail).

## Complexity Analysis
- **Brute Force:** O(n²) time
- **Greedy:** O(n) time, O(1) space

## Key Insights
1. **Total check first:** If total gas < total cost, impossible
2. **Reset on failure:** When tank goes negative, start over from next station
3. **Proof of correctness:** If we fail at station i, all stations from start to i are invalid
4. **Circular handling:** Use modulo for circular indexing in brute force
5. **Single valid answer:** Problem guarantees unique solution if one exists
