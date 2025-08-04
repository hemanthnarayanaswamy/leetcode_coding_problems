<h2><a href="https://leetcode.com/problems/fruit-into-baskets">940. Fruit Into Baskets</a></h2><h3>Medium</h3><hr><p>You are visiting a farm that has a single row of fruit trees arranged from left to right. The trees are represented by an integer array <code>fruits</code> where <code>fruits[i]</code> is the <strong>type</strong> of fruit the <code>i<sup>th</sup></code> tree produces.</p>

<p>You want to collect as much fruit as possible. However, the owner has some strict rules that you must follow:</p>

<ul>
	<li>You only have <strong>two</strong> baskets, and each basket can only hold a <strong>single type</strong> of fruit. There is no limit on the amount of fruit each basket can hold.</li>
	<li>Starting from any tree of your choice, you must pick <strong>exactly one fruit</strong> from <strong>every</strong> tree (including the start tree) while moving to the right. The picked fruits must fit in one of your baskets.</li>
	<li>Once you reach a tree with fruit that cannot fit in your baskets, you must stop.</li>
</ul>

<p>Given the integer array <code>fruits</code>, return <em>the <strong>maximum</strong> number of fruits you can pick</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> fruits = [<u>1,2,1</u>]
<strong>Output:</strong> 3
<strong>Explanation:</strong> We can pick from all 3 trees.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> fruits = [0,<u>1,2,2</u>]
<strong>Output:</strong> 3
<strong>Explanation:</strong> We can pick from trees [1,2,2].
If we had started at the first tree, we would only pick from trees [0,1].
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> fruits = [1,<u>2,3,2,2</u>]
<strong>Output:</strong> 4
<strong>Explanation:</strong> We can pick from trees [2,3,2,2].
If we had started at the first tree, we would only pick from trees [1,2].
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= fruits.length &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= fruits[i] &lt; fruits.length</code></li>
</ul>

# Fruit Into Baskets - Sliding Window Notes

"""
PROBLEM: Find the maximum number of fruits you can collect with at most 2 baskets
- Each basket can hold only one type of fruit
- Pick fruits contiguously (subarray)
- Return maximum fruits collected

REAL PROBLEM: Find longest subarray with at most 2 distinct elements

EXAMPLES:
fruits = [1,2,1]     → Answer: 3 (all fruits, 2 types)
fruits = [0,1,2,1]   → Answer: 3 (subarray [1,2,1] or [0,1])
fruits = [1,2,3,2,2] → Answer: 4 (subarray [2,3,2,2])

KEY INSIGHTS:
1. This is a sliding window problem
2. Maintain window with ≤ 2 distinct fruit types
3. Expand window by moving right pointer
4. Contract window when > 2 types by moving left pointer
5. Track maximum window size seen

SLIDING WINDOW PATTERN:
1. Use two pointers: start (left) and end (right)
2. Use frequency map to track fruit types in current window
3. Expand: Add fruits[end] to window
4. Contract: Remove fruits[start] when constraint violated
5. Update: Track maximum valid window size
"""

# APPROACH EXPLANATION:

def totalFruit(fruits):
    fruit_count = {}    # Frequency map for current window
    start = 0          # Left pointer of sliding window
    max_fruits = 0     # Maximum fruits collected so far
    
    for end, fruit in enumerate(fruits):  # Right pointer
        # STEP 1: EXPAND - Add current fruit to window
        fruit_count[fruit] = fruit_count.get(fruit, 0) + 1
        
        # STEP 2: CONTRACT - Shrink window if constraint violated
        while len(fruit_count) > 2:  # More than 2 fruit types
            # Remove leftmost fruit
            fruit_count[fruits[start]] -= 1
            
            # Clean up frequency map
            if fruit_count[fruits[start]] == 0:
                del fruit_count[fruits[start]]
            
            start += 1  # Move left pointer right
        
        # STEP 3: UPDATE - Track maximum valid window size
        max_fruits = max(max_fruits, end - start + 1)
    
    return max_fruits

"""
TRACE EXAMPLE: fruits = [1,2,3,2,2]

end=0, fruit=1: fruit_count={1:1}, start=0, window=[1], size=1
end=1, fruit=2: fruit_count={1:1,2:1}, start=0, window=[1,2], size=2
end=2, fruit=3: fruit_count={1:1,2:1,3:1}, start=0
    len > 2, contract: remove fruits[0]=1
    fruit_count={2:1,3:1}, start=1, window=[2,3], size=2
end=3, fruit=2: fruit_count={2:2,3:1}, start=1, window=[2,3,2], size=3
end=4, fruit=2: fruit_count={2:3,3:1}, start=1, window=[2,3,2,2], size=4

Answer: 4
"""

# SLIDING WINDOW TEMPLATE:
def sliding_window_template(arr, constraint_check):
    window_data = {}  # Track window state
    start = 0
    result = 0
    
    for end in range(len(arr)):
        # EXPAND: Add arr[end] to window
        update_window_add(window_data, arr[end])
        
        # CONTRACT: Shrink window while constraint violated
        while constraint_violated(window_data):
            update_window_remove(window_data, arr[start])
            start += 1
        
        # UPDATE: Track optimal result
        result = update_result(result, end - start + 1)
    
    return result

# TIME & SPACE COMPLEXITY:
"""
TIME: O(n)
- Each element is added once and removed at most once
- Total operations: 2n = O(n)

SPACE: O(k) where k = number of distinct elements
- In this problem: O(3) = O(1) since at most 3 fruit types stored
- Frequency map stores at most k distinct keys
"""

# COMMON VARIATIONS:
"""
1. At most K distinct characters: Change condition to len(freq) > k
2. Exactly K distinct characters: Different shrinking logic
3. Longest substring without repeating: K = 1
4. Minimum window substring: Different expansion/contraction logic
"""

# KEY DEBUGGING TIPS:
"""
1. Always clean up frequency map when count becomes 0
2. Use while loop for contraction (not if) - may need multiple contractions
3. Update result after ensuring window is valid
4. Be careful with indexing: window size = end - start + 1
"""

# Code 

```python
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        fruitsFreq = defaultdict(int)
        startIdx = 0
        ans = 0

        for end, fruit in enumerate(fruits):
            fruitsFreq[fruit] += 1

            if len(fruitsFreq) > 2: # use if instead of while because we only need to remove one excess element
                fruitsFreq[fruits[startIdx]] -= 1

                if fruitsFreq[fruits[startIdx]] == 0:
                    del fruitsFreq[fruits[startIdx]]
                
                startIdx += 1
                ans = max(ans, end - startIdx + 1) # need to compute the ans only then 
        
        return max(ans, end - startIdx + 1)
```

# Optimal Solution 
```python
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        result = 0
        f1, f2 = -1, -1
        count1, count2 = 0, 0
        prev = 0
        for f in fruits:
            if f == f1:
                count1 += 1
                prev += 1
            elif f == f2:
                f1, f2 = f2, f1
                count1, count2 = count2 + 1, count1
                prev = 1
            else:
                result = max(result, count1 + count2)
                f1, f2 = f, f1
                count1, count2 = 1, prev
                prev = 1
        return max(result, count1 + count2)
```

"""
ALTERNATIVE APPROACH: Track two most recent fruit types + their states
Instead of sliding window, maintain state transitions

CORE VARIABLES:
f1, f2     = Two most recent fruit types (f1 = latest)
count1, count2 = Total counts of f1, f2 in current valid sequence  
prev       = Length of consecutive sequence of current fruit type
result     = Maximum fruits collected so far

ALGORITHM LOGIC:
3 Cases based on current fruit:

CASE 1: fruit == f1 (continue same fruit)
- count1++, prev++

CASE 2: fruit == f2 (switch back to previous fruit)  
- Swap f1↔f2, swap count1↔count2
- count1++, prev=1

CASE 3: fruit is NEW (3rd distinct fruit - break sequence)
- Update result = max(result, count1+count2)
- Reset: f1=new_fruit, f2=old_f1, count1=1, count2=prev
- prev=1

"""
