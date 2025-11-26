# Question 5: Group Anagrams

## Layman's Explanation
An **anagram** is a word formed by rearranging the letters of another word. For example, "eat", "tea", and "ate" are all anagrams of each other because they all contain exactly one 'a', one 'e', and one 't'.

The goal is to group these words together.

### How the Algorithm Works (Solution 5-1)
1.  **The "Signature" (Key):** To know if two words are anagrams, we need a standard way to represent them. If we **sort the letters** of a word alphabetically, all anagrams will look exactly the same.
    -   "eat" sorted -> "aet"
    -   "tea" sorted -> "aet"
    -   "ate" sorted -> "aet"
    -   "tan" sorted -> "ant"
    -   "nat" sorted -> "ant"
2.  **Buckets (Dictionary):** We create a collection of buckets (a dictionary or hash map). The label on each bucket is the sorted version of the word (the "signature").
3.  **Grouping:** We go through our list of words one by one:
    -   Take a word (e.g., "tea").
    -   Sort it to find its signature ("aet").
    -   Find the bucket labeled "aet". If it doesn't exist, create it.
    -   Drop the original word ("tea") into that bucket.
4.  **Result:** Once we finish all words, we just collect the contents of all the buckets.

## Visualization
I have created an interactive visualization to help you see how words are sorted and dropped into their respective buckets.

[Open Visualization (5-group-anagrams.html)](./5-group-anagrams.html)

*(Open the HTML file in your browser to interact with the visualization)*
