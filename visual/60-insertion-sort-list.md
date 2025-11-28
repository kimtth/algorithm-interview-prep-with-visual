# 60. Insertion Sort List

## Problem Description
Sort a linked list using insertion sort algorithm. Unlike array insertion sort where we shift elements, in a linked list we manipulate pointers to insert each node in its correct sorted position.

## Layman's Explanation
Imagine you're sorting a hand of cards, but instead of physical cards that you can slide around, each card is connected to the next by a string. To sort them:

1. **Take one card at a time** from your unsorted pile
2. **Walk through your sorted pile** from the beginning
3. **Find where this card belongs** (first position where the next card is bigger)
4. **Re-tie the strings** to insert this card in that position

The key insight is that we need a "parent" pointer - we track the node BEFORE where we want to insert, so we can redirect its "next" pointer.

## Algorithm Walkthrough
Given: `4 → 2 → 1 → 3`

**Initial Setup:**
- Create a dummy `parent` node pointing to head
- `cur` starts at position 1 (first node to potentially move)

**Step 1: Process node 2**
- Compare 2 with 4 (previous node)
- 2 < 4, so we need to move it
- Find insertion point: Walk from `parent` until we find where 2 belongs
- Insert 2 before 4: `2 → 4 → 1 → 3`

**Step 2: Process node 1**
- Compare 1 with 4 (previous node)
- 1 < 4, so we need to move it
- Find insertion point: Walk from `parent` until we find where 1 belongs
- Insert 1 at beginning: `1 → 2 → 4 → 3`

**Step 3: Process node 3**
- Compare 3 with 4 (previous node)
- 3 < 4, so we need to move it
- Find insertion point: Walk from `parent` until we find where 3 belongs
- Insert 3 between 2 and 4: `1 → 2 → 3 → 4`

**Result:** `1 → 2 → 3 → 4` ✓

## Code Explanation
```python
def insertionSortList(self, head: ListNode) -> ListNode:
    parent = ListNode(None)  # Dummy node before head
    cur = head
    
    while cur:
        # Walk from parent to find insertion point
        while parent.next and parent.next.val < cur.val:
            parent = parent.next
        
        # Save next node to process
        next_node = cur.next
        
        # Insert cur after parent
        cur.next = parent.next
        parent.next = cur
        
        # Reset parent to dummy for next iteration
        parent = ListNode(None)
        parent.next = head  # Update head if changed
        
        cur = next_node  # Move to next unsorted node
    
    return parent.next
```

## Complexity Analysis
- **Time Complexity:** O(n²) - For each of n nodes, we may traverse up to n nodes to find insertion point
- **Space Complexity:** O(1) - Only use a few pointers, no extra data structures

## Key Insights
1. **Dummy Parent Node:** Having a dummy node before head simplifies insertion at the beginning
2. **Pointer Manipulation:** Unlike array insertion sort, we don't shift elements - we just redirect pointers
3. **In-place Sorting:** No extra memory needed beyond a few tracking pointers
4. **Stable Sort:** Equal elements maintain their relative order (we use `<` not `<=`)
