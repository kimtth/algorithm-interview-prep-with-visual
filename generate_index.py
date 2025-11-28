#!/usr/bin/env python3
"""
Script to generate index.html with problem table and visualization links.
Scans the visual/ directory for all HTML files.
"""

from pathlib import Path
import re

# Problem data from README.md - now without visual_dir since all files are in /visual
PROBLEMS = [
    {"num": 1, "title": "Valid Palindrome", "leetcode": "https://leetcode.com/problems/valid-palindrome/", "difficulty": "★", "chapter": "Ch6. String Manipulation"},
    {"num": 2, "title": "Reverse String", "leetcode": "https://leetcode.com/problems/reverse-string/", "difficulty": "★", "chapter": "Ch6. String Manipulation"},
    {"num": 3, "title": "Reorder Data in Log Files", "leetcode": "https://leetcode.com/problems/reorder-data-in-log-files/", "difficulty": "★", "chapter": "Ch6. String Manipulation"},
    {"num": 4, "title": "Most Common Word", "leetcode": "https://leetcode.com/problems/most-common-word/", "difficulty": "★", "chapter": "Ch6. String Manipulation"},
    {"num": 5, "title": "Group Anagrams", "leetcode": "https://leetcode.com/problems/group-anagrams/", "difficulty": "★★", "chapter": "Ch6. String Manipulation"},
    {"num": 6, "title": "Longest Palindromic Substring", "leetcode": "https://leetcode.com/problems/longest-palindromic-substring/", "difficulty": "★★", "chapter": "Ch6. String Manipulation"},
    {"num": 7, "title": "Two Sum", "leetcode": "https://leetcode.com/problems/two-sum/", "difficulty": "★", "chapter": "Ch7. Arrays"},
    {"num": 8, "title": "Trapping Rain Water", "leetcode": "https://leetcode.com/problems/trapping-rain-water/", "difficulty": "★★★", "chapter": "Ch7. Arrays"},
    {"num": 9, "title": "3Sum", "leetcode": "https://leetcode.com/problems/3sum/", "difficulty": "★★", "chapter": "Ch7. Arrays"},
    {"num": 10, "title": "Array Partition I", "leetcode": "https://leetcode.com/problems/array-partition/", "difficulty": "★", "chapter": "Ch7. Arrays"},
    {"num": 11, "title": "Product of Array Except Self", "leetcode": "https://leetcode.com/problems/product-of-array-except-self/", "difficulty": "★★", "chapter": "Ch7. Arrays"},
    {"num": 12, "title": "Best Time to Buy and Sell Stock", "leetcode": "https://leetcode.com/problems/best-time-to-buy-and-sell-stock/", "difficulty": "★", "chapter": "Ch7. Arrays"},
    {"num": 13, "title": "Palindrome Linked List", "leetcode": "https://leetcode.com/problems/palindrome-linked-list/", "difficulty": "★", "chapter": "Ch8. Linked Lists"},
    {"num": 14, "title": "Merge Two Sorted Lists", "leetcode": "https://leetcode.com/problems/merge-two-sorted-lists/", "difficulty": "★", "chapter": "Ch8. Linked Lists"},
    {"num": 15, "title": "Reverse Linked List", "leetcode": "https://leetcode.com/problems/reverse-linked-list/", "difficulty": "★", "chapter": "Ch8. Linked Lists"},
    {"num": 16, "title": "Add Two Numbers", "leetcode": "https://leetcode.com/problems/add-two-numbers/", "difficulty": "★★", "chapter": "Ch8. Linked Lists"},
    {"num": 17, "title": "Swap Nodes in Pairs", "leetcode": "https://leetcode.com/problems/swap-nodes-in-pairs/", "difficulty": "★★", "chapter": "Ch8. Linked Lists"},
    {"num": 18, "title": "Odd Even Linked List", "leetcode": "https://leetcode.com/problems/odd-even-linked-list/", "difficulty": "★★", "chapter": "Ch8. Linked Lists"},
    {"num": 19, "title": "Reverse Linked List II", "leetcode": "https://leetcode.com/problems/reverse-linked-list-ii/", "difficulty": "★★", "chapter": "Ch8. Linked Lists"},
    {"num": 20, "title": "Valid Parentheses", "leetcode": "https://leetcode.com/problems/valid-parentheses/", "difficulty": "★", "chapter": "Ch9. Stack, Queue"},
    {"num": 21, "title": "Remove Duplicate Letters", "leetcode": "https://leetcode.com/problems/remove-duplicate-letters/", "difficulty": "★★★", "chapter": "Ch9. Stack, Queue"},
    {"num": 22, "title": "Daily Temperatures", "leetcode": "https://leetcode.com/problems/daily-temperatures/", "difficulty": "★★", "chapter": "Ch9. Stack, Queue"},
    {"num": 23, "title": "Implement Stack using Queues", "leetcode": "https://leetcode.com/problems/implement-stack-using-queues/", "difficulty": "★", "chapter": "Ch9. Stack, Queue"},
    {"num": 24, "title": "Implement Queue using Stacks", "leetcode": "https://leetcode.com/problems/implement-queue-using-stacks/", "difficulty": "★", "chapter": "Ch9. Stack, Queue"},
    {"num": 25, "title": "Design Circular Queue", "leetcode": "https://leetcode.com/problems/design-circular-queue/", "difficulty": "★★", "chapter": "Ch9. Stack, Queue"},
    {"num": 26, "title": "Design Circular Deque", "leetcode": "https://leetcode.com/problems/design-circular-deque/", "difficulty": "★★", "chapter": "Ch10. Deque, Priority Queue"},
    {"num": 27, "title": "Merge k Sorted Lists", "leetcode": "https://leetcode.com/problems/merge-k-sorted-lists/", "difficulty": "★", "chapter": "Ch10. Deque, Priority Queue"},
    {"num": 28, "title": "Design HashMap", "leetcode": "https://leetcode.com/problems/design-hashmap/", "difficulty": "★", "chapter": "Ch11. Hash Table"},
    {"num": 29, "title": "Jewels and Stones", "leetcode": "https://leetcode.com/problems/jewels-and-stones/", "difficulty": "★", "chapter": "Ch11. Hash Table"},
    {"num": 30, "title": "Longest Substring Without Repeating Characters", "leetcode": "https://leetcode.com/problems/longest-substring-without-repeating-characters/", "difficulty": "★★", "chapter": "Ch11. Hash Table"},
    {"num": 31, "title": "Top K Frequent Elements", "leetcode": "https://leetcode.com/problems/top-k-frequent-elements/", "difficulty": "★★", "chapter": "Ch11. Hash Table"},
    {"num": 32, "title": "Number of Islands", "leetcode": "https://leetcode.com/problems/number-of-islands/", "difficulty": "★★", "chapter": "Ch12. Graph"},
    {"num": 33, "title": "Letter Combinations of a Phone Number", "leetcode": "https://leetcode.com/problems/letter-combinations-of-a-phone-number/", "difficulty": "★★", "chapter": "Ch12. Graph"},
    {"num": 34, "title": "Permutations", "leetcode": "https://leetcode.com/problems/permutations/", "difficulty": "★★", "chapter": "Ch12. Graph"},
    {"num": 35, "title": "Combinations", "leetcode": "https://leetcode.com/problems/combinations/", "difficulty": "★★", "chapter": "Ch12. Graph"},
    {"num": 36, "title": "Combination Sum", "leetcode": "https://leetcode.com/problems/combination-sum/", "difficulty": "★★", "chapter": "Ch12. Graph"},
    {"num": 37, "title": "Subsets", "leetcode": "https://leetcode.com/problems/subsets/", "difficulty": "★★", "chapter": "Ch12. Graph"},
    {"num": 38, "title": "Reconstruct Itinerary", "leetcode": "https://leetcode.com/problems/reconstruct-itinerary/", "difficulty": "★★", "chapter": "Ch12. Graph"},
    {"num": 39, "title": "Course Schedule", "leetcode": "https://leetcode.com/problems/course-schedule/", "difficulty": "★★", "chapter": "Ch12. Graph"},
    {"num": 40, "title": "Network Delay Time", "leetcode": "https://leetcode.com/problems/network-delay-time/", "difficulty": "★★", "chapter": "Ch13. Shortest Path"},
    {"num": 41, "title": "Cheapest Flights Within K Stops", "leetcode": "https://leetcode.com/problems/cheapest-flights-within-k-stops/", "difficulty": "★★", "chapter": "Ch13. Shortest Path"},
    {"num": 42, "title": "Maximum Depth of Binary Tree", "leetcode": "https://leetcode.com/problems/maximum-depth-of-binary-tree/", "difficulty": "★", "chapter": "Ch14. Tree"},
    {"num": 43, "title": "Diameter of Binary Tree", "leetcode": "https://leetcode.com/problems/diameter-of-binary-tree/", "difficulty": "★", "chapter": "Ch14. Tree"},
    {"num": 44, "title": "Longest Univalue Path", "leetcode": "https://leetcode.com/problems/longest-univalue-path/", "difficulty": "★", "chapter": "Ch14. Tree"},
    {"num": 45, "title": "Invert Binary Tree", "leetcode": "https://leetcode.com/problems/invert-binary-tree/", "difficulty": "★", "chapter": "Ch14. Tree"},
    {"num": 46, "title": "Merge Two Binary Trees", "leetcode": "https://leetcode.com/problems/merge-two-binary-trees/", "difficulty": "★", "chapter": "Ch14. Tree"},
    {"num": 47, "title": "Serialize and Deserialize Binary Tree", "leetcode": "https://leetcode.com/problems/serialize-and-deserialize-binary-tree/", "difficulty": "★★★", "chapter": "Ch14. Tree"},
    {"num": 48, "title": "Balanced Binary Tree", "leetcode": "https://leetcode.com/problems/balanced-binary-tree/", "difficulty": "★", "chapter": "Ch14. Tree"},
    {"num": 49, "title": "Minimum Height Trees", "leetcode": "https://leetcode.com/problems/minimum-height-trees/", "difficulty": "★★", "chapter": "Ch14. Tree"},
    {"num": 50, "title": "Convert Sorted Array to Binary Search Tree", "leetcode": "https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/", "difficulty": "★", "chapter": "Ch14. Tree"},
    {"num": 51, "title": "Binary Search Tree to Greater Sum Tree", "leetcode": "https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/", "difficulty": "★★", "chapter": "Ch14. Tree"},
    {"num": 52, "title": "Range Sum of BST", "leetcode": "https://leetcode.com/problems/range-sum-of-bst/", "difficulty": "★", "chapter": "Ch14. Tree"},
    {"num": 53, "title": "Minimum Distance Between BST Nodes", "leetcode": "https://leetcode.com/problems/minimum-distance-between-bst-nodes/", "difficulty": "★", "chapter": "Ch14. Tree"},
    {"num": 54, "title": "Construct Binary Tree from Preorder and Inorder Traversal", "leetcode": "https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/", "difficulty": "★★", "chapter": "Ch14. Tree"},
    {"num": 55, "title": "Kth Largest Element in an Array", "leetcode": "https://leetcode.com/problems/kth-largest-element-in-an-array/", "difficulty": "★★", "chapter": "Ch15. Heap"},
    {"num": 56, "title": "Implement Trie (Prefix Tree)", "leetcode": "https://leetcode.com/problems/implement-trie-prefix-tree/", "difficulty": "★★", "chapter": "Ch16. Trie"},
    {"num": 57, "title": "Palindrome Pairs", "leetcode": "https://leetcode.com/problems/palindrome-pairs/", "difficulty": "★★★", "chapter": "Ch16. Trie"},
    {"num": 58, "title": "Sort List", "leetcode": "https://leetcode.com/problems/sort-list/", "difficulty": "★★", "chapter": "Ch17. Sorting"},
    {"num": 59, "title": "Merge Intervals", "leetcode": "https://leetcode.com/problems/merge-intervals/", "difficulty": "★★", "chapter": "Ch17. Sorting"},
    {"num": 60, "title": "Insertion Sort List", "leetcode": "https://leetcode.com/problems/insertion-sort-list/", "difficulty": "★★", "chapter": "Ch17. Sorting"},
    {"num": 61, "title": "Largest Number", "leetcode": "https://leetcode.com/problems/largest-number/", "difficulty": "★★", "chapter": "Ch17. Sorting"},
    {"num": 62, "title": "Valid Anagram", "leetcode": "https://leetcode.com/problems/valid-anagram/", "difficulty": "★", "chapter": "Ch17. Sorting"},
    {"num": 63, "title": "Sort Colors", "leetcode": "https://leetcode.com/problems/sort-colors/", "difficulty": "★★", "chapter": "Ch17. Sorting"},
    {"num": 64, "title": "K Closest Points to Origin", "leetcode": "https://leetcode.com/problems/k-closest-points-to-origin/", "difficulty": "★★", "chapter": "Ch17. Sorting"},
    {"num": 65, "title": "Binary Search", "leetcode": "https://leetcode.com/problems/binary-search/", "difficulty": "★", "chapter": "Ch18. Binary Search"},
    {"num": 66, "title": "Search in Rotated Sorted Array", "leetcode": "https://leetcode.com/problems/search-in-rotated-sorted-array/", "difficulty": "★★", "chapter": "Ch18. Binary Search"},
    {"num": 67, "title": "Intersection of Two Arrays", "leetcode": "https://leetcode.com/problems/intersection-of-two-arrays/", "difficulty": "★", "chapter": "Ch18. Binary Search"},
    {"num": 68, "title": "Two Sum II - Input Array Is Sorted", "leetcode": "https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/", "difficulty": "★", "chapter": "Ch18. Binary Search"},
    {"num": 69, "title": "Search a 2D Matrix II", "leetcode": "https://leetcode.com/problems/search-a-2d-matrix-ii/", "difficulty": "★★", "chapter": "Ch18. Binary Search"},
    {"num": 70, "title": "Single Number", "leetcode": "https://leetcode.com/problems/single-number/", "difficulty": "★", "chapter": "Ch19. Bit Manipulation"},
    {"num": 71, "title": "Hamming Distance", "leetcode": "https://leetcode.com/problems/hamming-distance/", "difficulty": "★", "chapter": "Ch19. Bit Manipulation"},
    {"num": 72, "title": "Sum of Two Integers", "leetcode": "https://leetcode.com/problems/sum-of-two-integers/", "difficulty": "★★★", "chapter": "Ch19. Bit Manipulation"},
    {"num": 73, "title": "UTF-8 Validation", "leetcode": "https://leetcode.com/problems/utf-8-validation/", "difficulty": "★★", "chapter": "Ch19. Bit Manipulation"},
    {"num": 74, "title": "Number of 1 Bits", "leetcode": "https://leetcode.com/problems/number-of-1-bits/", "difficulty": "★", "chapter": "Ch19. Bit Manipulation"},
    {"num": 75, "title": "Sliding Window Maximum", "leetcode": "https://leetcode.com/problems/sliding-window-maximum/", "difficulty": "★★★", "chapter": "Ch20. Sliding Window"},
    {"num": 76, "title": "Minimum Window Substring", "leetcode": "https://leetcode.com/problems/minimum-window-substring/", "difficulty": "★★★", "chapter": "Ch20. Sliding Window"},
    {"num": 77, "title": "Longest Repeating Character Replacement", "leetcode": "https://leetcode.com/problems/longest-repeating-character-replacement/", "difficulty": "★★", "chapter": "Ch20. Sliding Window"},
    {"num": 78, "title": "Best Time to Buy and Sell Stock II", "leetcode": "https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/", "difficulty": "★", "chapter": "Ch21. Greedy Algorithm"},
    {"num": 79, "title": "Queue Reconstruction by Height", "leetcode": "https://leetcode.com/problems/queue-reconstruction-by-height/", "difficulty": "★★", "chapter": "Ch21. Greedy Algorithm"},
    {"num": 80, "title": "Task Scheduler", "leetcode": "https://leetcode.com/problems/task-scheduler/", "difficulty": "★★", "chapter": "Ch21. Greedy Algorithm"},
    {"num": 81, "title": "Gas Station", "leetcode": "https://leetcode.com/problems/gas-station/", "difficulty": "★★", "chapter": "Ch21. Greedy Algorithm"},
    {"num": 82, "title": "Assign Cookies", "leetcode": "https://leetcode.com/problems/assign-cookies/", "difficulty": "★", "chapter": "Ch21. Greedy Algorithm"},
    {"num": 83, "title": "Majority Element", "leetcode": "https://leetcode.com/problems/majority-element/", "difficulty": "★", "chapter": "Ch22. Divide and Conquer"},
    {"num": 84, "title": "Different Ways to Add Parentheses", "leetcode": "https://leetcode.com/problems/different-ways-to-add-parentheses/", "difficulty": "★★", "chapter": "Ch22. Divide and Conquer"},
    {"num": 85, "title": "Fibonacci Number", "leetcode": "https://leetcode.com/problems/fibonacci-number/", "difficulty": "★", "chapter": "Ch23. Dynamic Programming"},
    {"num": 86, "title": "Maximum Subarray", "leetcode": "https://leetcode.com/problems/maximum-subarray/", "difficulty": "★", "chapter": "Ch23. Dynamic Programming"},
    {"num": 87, "title": "Climbing Stairs", "leetcode": "https://leetcode.com/problems/climbing-stairs/", "difficulty": "★", "chapter": "Ch23. Dynamic Programming"},
    {"num": 88, "title": "House Robber", "leetcode": "https://leetcode.com/problems/house-robber/", "difficulty": "★", "chapter": "Ch23. Dynamic Programming"},
]


def find_html_files(base_dir, problem_num):
    """Find HTML visualization files for a problem in the visual directory."""
    visual_path = Path(base_dir) / "visual"
    if not visual_path.exists():
        return []
    
    # Look for files that start with the problem number
    html_files = []
    
    for f in visual_path.glob(f"{problem_num}-*.html"):
        html_files.append(f"visual/{f.name}")
    
    return sorted(html_files)


def generate_html(base_dir):
    """Generate the index.html content."""
    
    html_template = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Python Algorithm Interview - Visualization Index</title>
    <style>
        :root {
            --bg-primary: #f8f9fa;
            --bg-secondary: #ffffff;
            --bg-card: #ffffff;
            --text-primary: #212529;
            --text-secondary: #6c757d;
            --accent: #0d6efd;
            --accent-hover: #0b5ed7;
            --success: #198754;
            --border: #dee2e6;
        }
        
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: var(--bg-primary);
            color: var(--text-primary);
            min-height: 100vh;
            padding: 2rem;
        }
        
        .container {
            max-width: 1400px;
            margin: 0 auto;
        }
        
        header {
            text-align: center;
            margin-bottom: 1rem;
            padding: 0.75rem 1rem;
            background: var(--bg-card);
            border-radius: 12px;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
            border: 1px solid var(--border);
            display: flex;
            align-items: center;
            justify-content: space-between;
            flex-wrap: wrap;
            gap: 0.5rem;
        }
        
        h1 {
            font-size: 1.4rem;
            margin: 0;
            color: var(--text-primary);
        }
        
        .subtitle {
            color: var(--text-secondary);
            font-size: 0.9rem;
            margin-left: 0.5rem;
        }
        
        .header-left {
            display: flex;
            align-items: center;
            flex-wrap: wrap;
        }
        
        .controls {
            display: flex;
            gap: 1rem;
            margin-bottom: 1.5rem;
            flex-wrap: wrap;
            align-items: center;
            justify-content: center;
        }
        
        .filters {
            display: flex;
            gap: 0.5rem;
            flex-wrap: wrap;
        }
        
        .filter-btn {
            padding: 0.5rem 1rem;
            border: 2px solid var(--border);
            background: var(--bg-secondary);
            color: var(--text-primary);
            border-radius: 20px;
            cursor: pointer;
            transition: all 0.3s ease;
        }
        
        .filter-btn:hover, .filter-btn.active {
            background: var(--accent);
            border-color: var(--accent);
            color: #fff;
        }
        
        .search-box {
            width: 300px;
            padding: 0.5rem 1rem;
            border: 2px solid var(--border);
            background: var(--bg-secondary);
            color: var(--text-primary);
            border-radius: 20px;
            font-size: 0.95rem;
        }
        
        .search-box:focus {
            outline: none;
            border-color: var(--accent);
        }
        
        table {
            width: 100%;
            border-collapse: collapse;
            background: var(--bg-card);
            border-radius: 12px;
            overflow: hidden;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
            border: 1px solid var(--border);
        }
        
        th, td {
            padding: 1rem;
            text-align: left;
            border-bottom: 1px solid var(--border);
        }
        
        th {
            background: var(--bg-primary);
            font-weight: 600;
            text-transform: uppercase;
            font-size: 0.85rem;
            letter-spacing: 0.5px;
            color: var(--text-secondary);
        }
        
        tr:hover {
            background: rgba(13, 110, 253, 0.05);
        }
        
        .problem-num {
            font-weight: bold;
            color: var(--accent);
            font-size: 1.1rem;
        }
        
        .problem-title a {
            color: var(--text-primary);
            text-decoration: none;
            transition: color 0.3s;
        }
        
        .problem-title a:hover {
            color: var(--accent);
        }
        
        .difficulty {
            color: #f59e0b;
        }
        
        .chapter {
            color: var(--text-secondary);
            font-size: 0.9rem;
        }
        
        .viz-links {
            display: flex;
            gap: 0.5rem;
            flex-wrap: wrap;
        }
        
        .viz-link {
            display: inline-block;
            padding: 0.4rem 0.8rem;
            background: var(--success);
            color: #fff;
            text-decoration: none;
            border-radius: 4px;
            font-size: 0.85rem;
            font-weight: 500;
            transition: all 0.3s ease;
        }
        
        .viz-link:hover {
            background: var(--accent);
            transform: translateY(-2px);
        }
        
        .no-viz {
            color: var(--text-secondary);
            font-style: italic;
        }
        
        .stats {
            display: flex;
            gap: 1.5rem;
            flex-wrap: wrap;
        }
        
        .stat {
            text-align: center;
        }
        
        .stat-value {
            font-size: 1.2rem;
            font-weight: bold;
            color: var(--accent);
        }
        
        .stat-label {
            color: var(--text-secondary);
            font-size: 0.75rem;
        }
        
        @media (max-width: 768px) {
            body {
                padding: 1rem;
            }
            
            h1 {
                font-size: 1.8rem;
            }
            
            th, td {
                padding: 0.5rem;
                font-size: 0.85rem;
            }
            
            .viz-link {
                padding: 0.3rem 0.6rem;
                font-size: 0.75rem;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <header>
            <div class="header-left">
                <h1>🐍 Python Algorithm Interview</h1>
                <span class="subtitle">Interactive Visualizations for 88 Algorithm Problems</span>
            </div>
            <div class="stats">
                <div class="stat">
                    <div class="stat-value" id="total-problems">88</div>
                    <div class="stat-label">Problems</div>
                </div>
                <div class="stat">
                    <div class="stat-value" id="total-viz">0</div>
                    <div class="stat-label">Visualizations</div>
                </div>
                <div class="stat">
                    <div class="stat-value">23</div>
                    <div class="stat-label">Chapters</div>
                </div>
            </div>
        </header>
        
        <div class="controls">
            <input type="text" class="search-box" id="search" placeholder="🔍 Search problems...">
            <div class="filters">
                <button class="filter-btn active" data-filter="all">All</button>
                <button class="filter-btn" data-filter="★">Easy ★</button>
                <button class="filter-btn" data-filter="★★">Medium ★★</button>
                <button class="filter-btn" data-filter="★★★">Hard ★★★</button>
            </div>
        </div>
        
        <table id="problem-table">
            <thead>
                <tr>
                    <th>#</th>
                    <th>Title</th>
                    <th>Difficulty</th>
                    <th>Chapter</th>
                    <th>Visualization</th>
                </tr>
            </thead>
            <tbody>
'''
    
    # Generate table rows
    total_viz = 0
    for problem in PROBLEMS:
        html_files = find_html_files(base_dir, problem["num"])
        total_viz += len(html_files)
        
        viz_html = ""
        if html_files:
            viz_html = " ".join([f'<a href="{f}" class="viz-link" target="_blank">View {i+1}</a>' 
                                for i, f in enumerate(html_files)])
        else:
            viz_html = '<span class="no-viz">-</span>'
        
        html_template += f'''                <tr data-difficulty="{problem["difficulty"]}">
                    <td class="problem-num">{problem["num"]}</td>
                    <td class="problem-title"><a href="{problem["leetcode"]}" target="_blank">{problem["title"]}</a></td>
                    <td class="difficulty">{problem["difficulty"]}</td>
                    <td class="chapter">{problem["chapter"]}</td>
                    <td class="viz-links">{viz_html}</td>
                </tr>
'''
    
    html_template += '''            </tbody>
        </table>
    </div>
    
    <script>
        // Update visualization count
        document.getElementById('total-viz').textContent = document.querySelectorAll('.viz-link').length;
        
        // Search functionality
        document.getElementById('search').addEventListener('input', function(e) {
            const searchTerm = e.target.value.toLowerCase();
            document.querySelectorAll('#problem-table tbody tr').forEach(row => {
                const text = row.textContent.toLowerCase();
                row.style.display = text.includes(searchTerm) ? '' : 'none';
            });
        });
        
        // Filter functionality
        document.querySelectorAll('.filter-btn').forEach(btn => {
            btn.addEventListener('click', function() {
                document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
                this.classList.add('active');
                
                const filter = this.dataset.filter;
                document.querySelectorAll('#problem-table tbody tr').forEach(row => {
                    if (filter === 'all') {
                        row.style.display = '';
                    } else {
                        row.style.display = row.dataset.difficulty === filter ? '' : 'none';
                    }
                });
            });
        });
    </script>
</body>
</html>
'''
    
    return html_template


def main():
    base_dir = Path(__file__).parent
    html_content = generate_html(base_dir)
    
    output_path = base_dir / "index.html"
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html_content)
    
    print(f"✓ Generated: {output_path}")
    print(f"✓ Total problems: {len(PROBLEMS)}")
    
    # Count total HTML files
    visual_dir = base_dir / "visual"
    if visual_dir.exists():
        html_count = len(list(visual_dir.glob("*.html")))
        print(f"✓ Total visualization files: {html_count}")


if __name__ == "__main__":
    main()
