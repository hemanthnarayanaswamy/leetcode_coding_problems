<h2><a href="https://leetcode.com/problems/reduction-operations-to-make-the-array-elements-equal">2016. Reduction Operations to Make the Array Elements Equal</a></h2><h3>Medium</h3><hr><p>Given an integer array <code>nums</code>, your goal is to make all elements in <code>nums</code> equal. To complete one operation, follow these steps:</p>

<ol>
	<li>Find the <strong>largest</strong> value in <code>nums</code>. Let its index be <code>i</code> (<strong>0-indexed</strong>) and its value be <code>largest</code>. If there are multiple elements with the largest value, pick the smallest <code>i</code>.</li>
	<li>Find the <strong>next largest</strong> value in <code>nums</code> <strong>strictly smaller</strong> than <code>largest</code>. Let its value be <code>nextLargest</code>.</li>
	<li>Reduce <code>nums[i]</code> to <code>nextLargest</code>.</li>
</ol>

<p>Return <em>the number of operations to make all elements in </em><code>nums</code><em> equal</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [5,1,3]
<strong>Output:</strong> 3
<strong>Explanation:</strong>&nbsp;It takes 3 operations to make all elements in nums equal:
1. largest = 5 at index 0. nextLargest = 3. Reduce nums[0] to 3. nums = [<u>3</u>,1,3].
2. largest = 3 at index 0. nextLargest = 1. Reduce nums[0] to 1. nums = [<u>1</u>,1,3].
3. largest = 3 at index 2. nextLargest = 1. Reduce nums[2] to 1. nums = [1,1,<u>1</u>].
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,1,1]
<strong>Output:</strong> 0
<strong>Explanation:</strong>&nbsp;All elements in nums are already equal.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,1,2,2,3]
<strong>Output:</strong> 4
<strong>Explanation:</strong>&nbsp;It takes 4 operations to make all elements in nums equal:
1. largest = 3 at index 4. nextLargest = 2. Reduce nums[4] to 2. nums = [1,1,2,2,<u>2</u>].
2. largest = 2 at index 2. nextLargest = 1. Reduce nums[2] to 1. nums = [1,1,<u>1</u>,2,2].
3. largest = 2 at index 3. nextLargest = 1. Reduce nums[3] to 1. nums = [1,1,1,<u>1</u>,2].
4. largest = 2 at index 4. nextLargest = 1. Reduce nums[4] to 1. nums = [1,1,1,1,<u>1</u>].
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 5 * 10<sup>4</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 5 * 10<sup>4</sup></code></li>
</ul>


# Approach
```
                                   nums = [1,1,2,2,3,3]
sorting the nums in reverse order  nums = [3,3,2,2,1,1]

                3  3  2  2  1  1
           i =  0  1  2  3  4  5  (indexes)
                |__|
    
    We have two 3, so we need 2 step to convert '3 3' to '2 2'. 

               '2  2' 2  2  1  1
           i =  0  1  2  3  4  5            Total 2 step right now.
                |________|
 
    We have four 2, so we need 4 step to convert '2 2 2 2' to '1 1 1 1'.
   
               '1  1  1  1' 1  1
           i =  0  1  2  3  4  5            Total 2 + 4 = 6 step right now.
                |______________|
                 All are equal!

So we need total 6 step here to make all of them equal.

When we calculated how many value there is for 3? when there was a different value after 3

starting from i = 1, if nums[i] != nums[i-1] then we calculate total steps, total_steps = 0
   
             3  3  2  2  1  1
        i =  0  1  2  3  4  5 
                   |____ Here nums[2] != nums[1], so total_steps += the frequency of 3 = 0 + 2 = 2
    If you look closely, frequency of 3 and i are both 2, so no need to count frequency. Just add i

Now :       2  2  2  2  1  1  
       i =  0  1  2  3  4  5
                        |____ Here nums[4] != nums[3], so total_steps += i '=' 2 + 4 = 6.
    See? just add i which is working as frequency here. 
```

# Solution
```python
class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        operations = 0
        nums = sorted(nums, reverse=True)
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                continue
            else:
                operations += i+1
        
        return operations
```

# Optimized Solution 
```python 
class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        n = len(nums)
        nums = sorted(nums, reverse=True)
        opperations = 0

        for i in range(1, n):
            if nums[i] != nums[i - 1]:
                opperations += i
        return opperations
```
