# Question 19: Reverse Linked List II

## Layman's Explanation
Unlike Question 15 where we reverse the entire list, here we only reverse a **portion** of the list - from position `m` to position `n`.

For example: `1 -> 2 -> 3 -> 4 -> 5`, reverse from position 2 to 4:
Result: `1 -> 4 -> 3 -> 2 -> 5`

### How the Algorithm Works (Solution 19-1)
1.  **Find the Start:** Walk to position `m-1` (the node just before the reversal starts).
2.  **Reverse the Segment:** One by one, take nodes from positions `m+1` to `n` and insert them right after the start position.
3.  **Reconnect:** The original connections handle themselves through the reversal logic.

## Visualization
I have created an interactive visualization to help you see how a portion of the list is reversed.

[Open Visualization (19-reverse-linked-list-ii.html)](./19-reverse-linked-list-ii.html)

*(Open the HTML file in your browser to interact with the visualization)*
