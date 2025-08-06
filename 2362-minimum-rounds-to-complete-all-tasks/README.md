<h2><a href="https://leetcode.com/problems/minimum-rounds-to-complete-all-tasks/">2362. Minimum Rounds to Complete All Tasks</a></h2><h3>Medium</h3><hr><p>You are given a <strong>0-indexed</strong> integer array <code>tasks</code>, where <code>tasks[i]</code> represents the difficulty level of a task. In each round, you can complete either 2 or 3 tasks of the <strong>same difficulty level</strong>.</p>

<p>Return <em>the <strong>minimum</strong> rounds required to complete all the tasks, or </em><code>-1</code><em> if it is not possible to complete all the tasks.</em></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> tasks = [2,2,3,3,2,4,4,4,4,4]
<strong>Output:</strong> 4
<strong>Explanation:</strong> To complete all the tasks, a possible plan is:
- In the first round, you complete 3 tasks of difficulty level 2. 
- In the second round, you complete 2 tasks of difficulty level 3. 
- In the third round, you complete 3 tasks of difficulty level 4. 
- In the fourth round, you complete 2 tasks of difficulty level 4.  
It can be shown that all the tasks cannot be completed in fewer than 4 rounds, so the answer is 4.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> tasks = [2,3,3]
<strong>Output:</strong> -1
<strong>Explanation:</strong> There is only 1 task of difficulty level 2, but in each round, you can only complete either 2 or 3 tasks of the same difficulty level. Hence, you cannot complete all the tasks, and the answer is -1.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= tasks.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= tasks[i] &lt;= 10<sup>9</sup></code></li>
</ul>

<p>&nbsp;</p>
<p><strong>Note:</strong> This question is the same as <a href="https://leetcode.com/problems/minimum-number-of-operations-to-make-array-empty/description/" target="_blank">2870: Minimum Number of Operations to Make Array Empty.</a></p>

# Solution 
* https://leetcode.com/problems/minimum-number-of-operations-to-make-array-empty/
* Refer to this problem
```python
class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        tasksFreq = Counter(tasks)
        count = 0

        for v in tasksFreq.values():
            if v == 1:
                return -1 
            
            q = v // 3
            r = v % 3

            if r == 0:
                count += q
            else:
                count += q + 1
        
        return count
```

"""
KEY INSIGHTS:
1. If any task count = 1 → impossible (-1)
2. For count ≥ 2 → always possible
3. Minimize rounds = use groups of 3 when possible

MATHEMATICAL APPROACHES:

METHOD 1 - Ceiling Formula:
rounds = (count - 1) // 3 + 1

val=2: (2-1)//3 + 1 = 0 + 1 = 1 round  ✅ (one group of 2)
val=3: (3-1)//3 + 1 = 0 + 1 = 1 round  ✅ (one group of 3)  
val=4: (4-1)//3 + 1 = 1 + 1 = 2 rounds ✅ (two groups of 2)
val=5: (5-1)//3 + 1 = 1 + 1 = 2 rounds ✅ (one group of 3, one group of 2)
val=6: (6-1)//3 + 1 = 1 + 1 = 2 rounds ✅ (two groups of 3)

METHOD 2 - Division + Remainder:
q, r = count // 3, count % 3
rounds = q + (1 if r > 0 else 0)

Both give same result!

PATTERN FOR ANY COUNT:
count % 3 == 0 → count/3 rounds (all groups of 3)
count % 3 == 1 → count/3 rounds (convert 3+1 → 2+2)  
count % 3 == 2 → count/3 + 1 rounds (groups of 3 + one group of 2)

TIME: O(n) for counting + O(k) for processing = O(n)
SPACE: O(k) where k = unique task types
"""

# Optimal Solution
```python
class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        tasksFreq = Counter(tasks)
        count = 0

        for _, v in tasksFreq.items():
            if v < 2:
                return -1 
            
            count += (v - 1)//3 + 1

        return count
```
