<h2><a href="https://leetcode.com/problems/make-array-elements-equal-to-zero">3616. Make Array Elements Equal to Zero</a></h2><h3>Easy</h3><hr><p>You are given an integer array <code>nums</code>.</p>

<p>Start by selecting a starting position <code>curr</code> such that <code>nums[curr] == 0</code>, and choose a movement <strong>direction</strong> of&nbsp;either left or right.</p>

<p>After that, you repeat the following process:</p>

<ul>
	<li>If <code>curr</code> is out of the range <code>[0, n - 1]</code>, this process ends.</li>
	<li>If <code>nums[curr] == 0</code>, move in the current direction by <strong>incrementing</strong> <code>curr</code> if you are moving right, or <strong>decrementing</strong> <code>curr</code> if you are moving left.</li>
	<li>Else if <code>nums[curr] &gt; 0</code>:
	<ul>
		<li>Decrement <code>nums[curr]</code> by 1.</li>
		<li><strong>Reverse</strong>&nbsp;your movement direction (left becomes right and vice versa).</li>
		<li>Take a step in your new direction.</li>
	</ul>
	</li>
</ul>

<p>A selection of the initial position <code>curr</code> and movement direction is considered <strong>valid</strong> if every element in <code>nums</code> becomes 0 by the end of the process.</p>

<p>Return the number of possible <strong>valid</strong> selections.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,0,2,0,3]</span></p>

<p><strong>Output:</strong> <span class="example-io">2</span></p>

<p><strong>Explanation:</strong></p>

<p>The only possible valid selections are the following:</p>

<ul>
	<li>Choose <code>curr = 3</code>, and a movement direction to the left.

	<ul>
		<li><code>[1,0,2,<strong><u>0</u></strong>,3] -&gt; [1,0,<strong><u>2</u></strong>,0,3] -&gt; [1,0,1,<strong><u>0</u></strong>,3] -&gt; [1,0,1,0,<strong><u>3</u></strong>] -&gt; [1,0,1,<strong><u>0</u></strong>,2] -&gt; [1,0,<strong><u>1</u></strong>,0,2] -&gt; [1,0,0,<strong><u>0</u></strong>,2] -&gt; [1,0,0,0,<strong><u>2</u></strong>] -&gt; [1,0,0,<strong><u>0</u></strong>,1] -&gt; [1,0,<strong><u>0</u></strong>,0,1] -&gt; [1,<strong><u>0</u></strong>,0,0,1] -&gt; [<strong><u>1</u></strong>,0,0,0,1] -&gt; [0,<strong><u>0</u></strong>,0,0,1] -&gt; [0,0,<strong><u>0</u></strong>,0,1] -&gt; [0,0,0,<strong><u>0</u></strong>,1] -&gt; [0,0,0,0,<strong><u>1</u></strong>] -&gt; [0,0,0,0,0]</code>.</li>
	</ul>
	</li>
	<li>Choose <code>curr = 3</code>, and a movement direction to the right.
	<ul>
		<li><code>[1,0,2,<strong><u>0</u></strong>,3] -&gt; [1,0,2,0,<strong><u>3</u></strong>] -&gt; [1,0,2,<strong><u>0</u></strong>,2] -&gt; [1,0,<strong><u>2</u></strong>,0,2] -&gt; [1,0,1,<strong><u>0</u></strong>,2] -&gt; [1,0,1,0,<strong><u>2</u></strong>] -&gt; [1,0,1,<strong><u>0</u></strong>,1] -&gt; [1,0,<strong><u>1</u></strong>,0,1] -&gt; [1,0,0,<strong><u>0</u></strong>,1] -&gt; [1,0,0,0,<strong><u>1</u></strong>] -&gt; [1,0,0,<strong><u>0</u></strong>,0] -&gt; [1,0,<strong><u>0</u></strong>,0,0] -&gt; [1,<strong><u>0</u></strong>,0,0,0] -&gt; [<strong><u>1</u></strong>,0,0,0,0] -&gt; [0,0,0,0,0].</code></li>
	</ul>
	</li>
</ul>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [2,3,4,0,4,1,0]</span></p>

<p><strong>Output:</strong> <span class="example-io">0</span></p>

<p><strong>Explanation:</strong></p>

<p>There are no possible valid selections.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 100</code></li>
	<li><code>0 &lt;= nums[i] &lt;= 100</code></li>
	<li>There is at least one element <code>i</code> where <code>nums[i] == 0</code>.</li>
</ul>

# Approach 
Array indexes are locations. At each index is a wall with nums[i] health. When the wall has 0 health, it disappears. The pointer is a ball. It must start where there isn't a wall (nums[i] == 0) and it has a starting direction. Choosing this starting position & direction is the player's only move. When the ball hits a wall, the wall loses 1 health and the ball changes direction. The game ends when the ball exits one side of the array. The game is won if no walls remain when the game ends. How many starting conditions (index and direction) result in winning the game?

![](https://assets.leetcode.com/users/images/918b572a-9773-4747-8c71-9e9f6945372c_1761508886.660334.webp)

1. Now when you place the ball at index i where `arr[i] == 0` For the ball to exit and win the game by making all elements zero, The sum to the right and the sum to the left from that index should be equal and with a diff of `1`
2. If `sum(right) == sum(left)`, Then the ball can go in any direction and we'll still win the game so We, have two possible options. 
3. If `abs(sum(right) - sum(left)) == 1`, Then the ball should start in the direction where sum is more that way at the end all will be zero, So wh have one possible option. 

```
* Compute the Right Prefix and Left Prefix sum index
* For each starting position where arr[i] == 0, check if left == right or left - right == 1, based on that add the count of possible options 1/2. 
* If the sums not match any options from above, Just continue to the end of array checking all possible start positions.
```

**`HINT` --> If you're feeling confused about this problem, try to think about it like this: you need to find the sum of all the numbers to the left of where nums[i]==0 and the sum of all the numbers to the right of that point. If you need more help, look at the detailed explanation in this comment.**

1. when `sum_left == sum_right` => **you can start from that position and go in either direction since it bounces back and forth removing 1 each time you change direction.**
2. when `abs(sum_left - sum_right) == 1` => **you can only start in the direction that has the larger size**

```python
class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        left_prefix = []
        right_prefix = []
        left_sum = 0
        numsSum = sum(nums)
        res = 0

        for i in range(len(nums)):
            l = left_sum + nums[i]
            r = abs(numsSum - left_sum)
            left_prefix.append(l)
            right_prefix.append(r)
            left_sum = l

            if nums[i] == 0:
                if left_prefix[i] == right_prefix[i]:
                    res += 2
                elif abs(left_prefix[i] - right_prefix[i]) == 1:
                    res += 1

        return res
```
---
* We don't need to store the prefix sum's, directly use the values `l`, `r`. 

```python
class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        left_sum = 0
        numsSum = sum(nums)
        res = 0

        for num in nums:
            l = left_sum + num
            r = abs(numsSum - left_sum)
            left_sum = l

            if num == 0:
                diff = abs(l - r)
                if diff == 0:
                    res += 2
                elif diff == 1:
                    res += 1

        return res
```

