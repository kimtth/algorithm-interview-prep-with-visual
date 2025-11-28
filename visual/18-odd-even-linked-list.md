# Question 18: Odd Even Linked List

## Layman's Explanation
We want to rearrange a linked list so that all the nodes at **odd positions** (1st, 3rd, 5th...) come first, followed by all the nodes at **even positions** (2nd, 4th, 6th...).

For example: `1 -> 2 -> 3 -> 4 -> 5` becomes `1 -> 3 -> 5 -> 2 -> 4`

### How the Algorithm Works (Solution 18-1)
1.  We maintain two separate chains: one for odd-positioned nodes, one for even-positioned nodes.
2.  We walk through the list, alternating between adding to odd and even chains.
3.  At the end, we connect the last odd node to the head of the even chain.

## Visualization
I have created an interactive visualization to help you see how odd and even nodes separate and reconnect.

[Open Visualization (18-odd-even-linked-list.html)](./18-odd-even-linked-list.html)

*(Open the HTML file in your browser to interact with the visualization)*
