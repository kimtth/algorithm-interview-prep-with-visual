# Question 8: Trapping Rain Water

## Layman's Explanation
Imagine a landscape made of bars of different heights. When it rains, water gets trapped in the "valleys" between the bars. We want to calculate exactly how much water is trapped.

### How the Algorithm Works (Two Pointers)
Think of this as two walls moving towards each other from the far left and far right.
1.  **The Walls:** We have a `left` pointer starting at the beginning and a `right` pointer starting at the end.
2.  **Max Heights:** We keep track of the highest bar we've seen so far from the left (`left_max`) and from the right (`right_max`).
3.  **The Logic:** Water level is determined by the *shorter* of the two walls enclosing a valley.
    -   If the `left_max` is shorter than (or equal to) `right_max`, we know that any water at the `left` position is limited by `left_max` (because there's a taller wall somewhere on the right).
    -   So, if the current bar at `left` is shorter than `left_max`, the difference is filled with water.
    -   We then move the `left` pointer inward.
    -   (Same logic applies if `right_max` is shorter, but we move the `right` pointer inward).
4.  **Result:** We keep adding up the water until the two pointers meet.

## Visualization
I have created an interactive visualization to help you see the walls moving and water filling up.

[Open Visualization (8-trapping-rain-water.html)](./8-trapping-rain-water.html)

*(Open the HTML file in your browser to interact with the visualization)*
