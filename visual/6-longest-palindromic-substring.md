# Question 6: Longest Palindromic Substring

## Layman's Explanation
We want to find the longest piece inside a string that reads the same forwards and backwards. For example, in "babad", "bab" is a palindrome, and "aba" is also a palindrome. Both have length 3.

### How the Algorithm Works (Solution 6-1)
The "Expand Around Center" approach is like planting a seed and watching it grow.
1.  **Centers:** Every character in the string can be the center of a palindrome.
    -   Odd length palindromes have a single character center (e.g., "aba" centers on 'b').
    -   Even length palindromes have a center *between* two characters (e.g., "abba" centers between 'b' and 'b').
2.  **Expansion:** For every possible center, we try to expand outwards to the left and right simultaneously.
    -   We keep expanding as long as the character on the left matches the character on the right.
    -   If they don't match (or we hit the edge of the string), we stop.
3.  **Tracking the Best:** We remember the longest palindrome we've found so far.
4.  **Result:** After checking all centers, we return the longest one we found.

## Visualization
I have created an interactive visualization to help you see this expansion process.

[Open Visualization (6-longest-palindromic-substring.html)](./6-longest-palindromic-substring.html)

*(Open the HTML file in your browser to interact with the visualization)*
