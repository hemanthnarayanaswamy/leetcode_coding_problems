<h2><a href="https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii">1320. Remove All Adjacent Duplicates in String II</a></h2><h3>Medium</h3><hr><p>You are given a string <code>s</code> and an integer <code>k</code>, a <code>k</code> <strong>duplicate removal</strong> consists of choosing <code>k</code> adjacent and equal letters from <code>s</code> and removing them, causing the left and the right side of the deleted substring to concatenate together.</p>

<p>We repeatedly make <code>k</code> <strong>duplicate removals</strong> on <code>s</code> until we no longer can.</p>

<p>Return <em>the final string after all such duplicate removals have been made</em>. It is guaranteed that the answer is <strong>unique</strong>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;abcd&quot;, k = 2
<strong>Output:</strong> &quot;abcd&quot;
<strong>Explanation: </strong>There&#39;s nothing to delete.</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;deeedbbcccbdaa&quot;, k = 3
<strong>Output:</strong> &quot;aa&quot;
<strong>Explanation: 
</strong>First delete &quot;eee&quot; and &quot;ccc&quot;, get &quot;ddbbbdaa&quot;
Then delete &quot;bbb&quot;, get &quot;dddaa&quot;
Finally delete &quot;ddd&quot;, get &quot;aa&quot;</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;pbbcggttciiippooaais&quot;, k = 2
<strong>Output:</strong> &quot;ps&quot;
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>5</sup></code></li>
	<li><code>2 &lt;= k &lt;= 10<sup>4</sup></code></li>
	<li><code>s</code> only contains lowercase English letters.</li>
</ul>

# Remove All Adjacent Duplicates in String II - Logic Notes

## Problem Understanding
- Remove k consecutive identical characters from a string
- Continue removing until no more k consecutive duplicates exist
- Return the final string after all removals

## Algorithm: Stack-Based Approach

### Core Logic
Use a stack to track characters and their consecutive counts:
- Each stack element: `[character, count]`
- When count reaches `k`, remove the entire group

### Step-by-Step Process

#### 1. Character Processing
```python
for char in s:
    if stack and stack[-1][0] == char:
        stack[-1][1] += 1  # Increment count of same character
    else:
        stack.append([char, 1])  # New character, start count at 1
```

#### 2. Removal Check
```python
if stack[-1][1] == k:
    stack.pop()  # Remove entire group when count reaches k
```

#### 3. Result Construction
```python
return ''.join(char * count for char, count in stack)
```

## Key Insights

### Why Stack Works
- **LIFO nature**: Most recent characters are processed first
- **Grouping**: Consecutive identical characters are naturally grouped
- **Efficient removal**: O(1) removal when k duplicates found

### Example Walkthrough
For `s = "deeedbbcccbdaa"`, `k = 3`:

```
Input: d-e-e-e-d-b-b-c-c-c-b-d-a-a
Stack operations:
- 'd': [['d',1]]
- 'e': [['d',1], ['e',1]]
- 'e': [['d',1], ['e',2]]
- 'e': [['d',1], ['e',3]] → Remove 'eee': [['d',1]]
- 'd': [['d',2]]
- 'b': [['d',2], ['b',1]]
- 'b': [['d',2], ['b',2]]
- 'c': [['d',2], ['b',2], ['c',1]]
- 'c': [['d',2], ['b',2], ['c',2]]
- 'c': [['d',2], ['b',2], ['c',3]] → Remove 'ccc': [['d',2], ['b',2]]
- 'b': [['d',2], ['b',3]] → Remove 'bbb': [['d',2]]
- 'd': [['d',3]] → Remove 'ddd': []
- 'a': [['a',1]]
- 'a': [['a',2]]

Result: "aa"
```

## Time & Space Complexity
- **Time**: O(n) - single pass through string
- **Space**: O(n) - worst case stack size

## Edge Cases to Consider
- Empty string
- k = 1 (remove all characters)
- No removals needed
- String becomes empty

```python
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        
        for char in s:
            if stack and stack[-1][0] == char:
                stack[-1][1] += 1
            else:
                stack.append([char, 1])
            
            if stack[-1][1] == k:
                stack.pop()
        
        return ''.join(char * count for char, count in stack)
```
---
```python
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        
        for char in s:
            if stack and stack[-1][0] == char:
                stack[-1][1] += 1

                if stack[-1][1] == k:
                    stack.pop()
            else:
                stack.append([char, 1])
        
        return ''.join(s[0] * s[1] for s in stack)
```
