<h2><a href="https://leetcode.com/problems/minimum-moves-to-equal-array-elements">453. Minimum Moves to Equal Array Elements</a></h2><h3>Medium</h3><hr><p>Given an integer array <code>nums</code> of size <code>n</code>, return <em>the minimum number of moves required to make all array elements equal</em>.</p>

<p>In one move, you can increment <code>n - 1</code> elements of the array by <code>1</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,2,3]
<strong>Output:</strong> 3
<strong>Explanation:</strong> Only three moves are needed (remember each move increments two elements):
[1,2,3]  =&gt;  [2,3,3]  =&gt;  [3,4,3]  =&gt;  [4,4,4]
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,1,1]
<strong>Output:</strong> 0
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == nums.length</code></li>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>-10<sup>9</sup> &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
	<li>The answer is guaranteed to fit in a <strong>32-bit</strong> integer.</li>
</ul>


# Approach 

* The problem description tells you that you should count how much moves (or sums) to make all values equal, always excluding one. So, we can think reversely by saying we could count how much moves (or subtracts) to make all values equal, only considering one.

**incrementing (n - 1) elements == decrementing 1 element**
**num steps to increase all to same element == num steps to decrease to min element**

So, instead of:

```
[1,2,3] -> [2,3,3] -> [3,3,4] -> [4,4,4] = 3 moves

We do:

[1,2,3] -> [1,2,2] -> [1,1,2] -> [1,1,1] = 3 moves
``
The logic is the same:

Decrease 1 over Sum every but one.

```
Nice, with that being clear it gets easier. We need to find out how much subtracts should happen, and it always will be related to the minimum number. So, in our case, if it's 1 (one), then we need to find out how much different to subtract. So:

3 - 1 = 2
2 - 1 = 1
1 - 1 = 0
Now we sum the difference: 2 + 1 + 0 = 3, so we got here! 3 moves!!
```

1. find the minimum number in the array 
2. for each element in the array calculate the number of moves needed to reduce the num to the minimum number 
3. return that value 

```python
class Solution:
    def minMoves(self, nums: List[int]) -> int:
        minValue = min(nums)
        moves = 0

        for num in nums:
            moves += num - minValue
        
        return moves
```

# Improved Solution
```python
class Solution:
    def minMoves(self, nums: List[int]) -> int:
        # incrementing (n - 1) elements == decrementing 1 element
        # num steps to increase all to same element == num steps to decrease to min element
        return sum(nums) - len(nums) * min(nums)
```
