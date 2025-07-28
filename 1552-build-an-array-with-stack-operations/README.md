<h2><a href="https://leetcode.com/problems/build-an-array-with-stack-operations">1552. Build an Array With Stack Operations</a></h2><h3>Medium</h3><hr><p>You are given an integer array <code>target</code> and an integer <code>n</code>.</p>

<p>You have an empty stack with the two following operations:</p>

<ul>
	<li><strong><code>&quot;Push&quot;</code></strong>: pushes an integer to the top of the stack.</li>
	<li><strong><code>&quot;Pop&quot;</code></strong>: removes the integer on the top of the stack.</li>
</ul>

<p>You also have a stream of the integers in the range <code>[1, n]</code>.</p>

<p>Use the two stack operations to make the numbers in the stack (from the bottom to the top) equal to <code>target</code>. You should follow the following rules:</p>

<ul>
	<li>If the stream of the integers is not empty, pick the next integer from the stream and push it to the top of the stack.</li>
	<li>If the stack is not empty, pop the integer at the top of the stack.</li>
	<li>If, at any moment, the elements in the stack (from the bottom to the top) are equal to <code>target</code>, do not read new integers from the stream and do not do more operations on the stack.</li>
</ul>

<p>Return <em>the stack operations needed to build </em><code>target</code> following the mentioned rules. If there are multiple valid answers, return <strong>any of them</strong>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> target = [1,3], n = 3
<strong>Output:</strong> [&quot;Push&quot;,&quot;Push&quot;,&quot;Pop&quot;,&quot;Push&quot;]
<strong>Explanation:</strong> Initially the stack s is empty. The last element is the top of the stack.
Read 1 from the stream and push it to the stack. s = [1].
Read 2 from the stream and push it to the stack. s = [1,2].
Pop the integer on the top of the stack. s = [1].
Read 3 from the stream and push it to the stack. s = [1,3].
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> target = [1,2,3], n = 3
<strong>Output:</strong> [&quot;Push&quot;,&quot;Push&quot;,&quot;Push&quot;]
<strong>Explanation:</strong> Initially the stack s is empty. The last element is the top of the stack.
Read 1 from the stream and push it to the stack. s = [1].
Read 2 from the stream and push it to the stack. s = [1,2].
Read 3 from the stream and push it to the stack. s = [1,2,3].
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> target = [1,2], n = 4
<strong>Output:</strong> [&quot;Push&quot;,&quot;Push&quot;]
<strong>Explanation:</strong> Initially the stack s is empty. The last element is the top of the stack.
Read 1 from the stream and push it to the stack. s = [1].
Read 2 from the stream and push it to the stack. s = [1,2].
Since the stack (from the bottom to the top) is equal to target, we stop the stack operations.
The answers that read integer 3 from the stream are not accepted.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= target.length &lt;= 100</code></li>
	<li><code>1 &lt;= n &lt;= 100</code></li>
	<li><code>1 &lt;= target[i] &lt;= n</code></li>
	<li><code>target</code> is strictly increasing.</li>
</ul>

# Solution 
* Convert to arr to set for lookup, here the logic is we need to do the iteration from `1, maxTarget` because the last element should be the max element as only the elements inside the target will be used, and the for loop will automatically stop. 

* The numbers that we push to the stack are ordered from 1 to n. Each number is available only once, so if we pop a number from the stack, that number is permanently gone. This means we want to pop every number that does not appear in target and should never pop any number that does appear in target
* We stop once the stack is equal to target and we are allowed to return any valid answer.
* So we only use iteration from `1, max_element_target`

```python
class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        targetSet = set(target)
        lastElement = max(target)
        res = []

        for i in range(1, lastElement+1):
            res.append('Push')

            if i not in targetSet:
                res.append('Pop')
        
        return res
```

# Optimal Solution
* Use `target[-1]` instead of `max(target)`: Since the target array is guaranteed to be sorted in the problem constraints, target[-1] is O(1) while max(target) is `O(n)`.

```python
class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        target_set = set(target)
        result = []
        
        for i in range(1, target[-1] + 1):
            result.append("Push")
            
            if i not in target_set:
                result.append("Pop")
        
        return result
```
---

```python
class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        result = []
        target_index = 0
        
        for i in range(1, target[-1] + 1):
            result.append("Push")
            
            if target_index < len(target) and i == target[target_index]:
                target_index += 1
            else:
                result.append("Pop")
        
        return result
```
