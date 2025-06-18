<h2><a href="https://leetcode.com/problems/intersection-of-multiple-arrays">2331. Intersection of Multiple Arrays</a></h2><h3>Easy</h3><hr>Given a 2D integer array <code>nums</code> where <code>nums[i]</code> is a non-empty array of <strong>distinct</strong> positive integers, return <em>the list of integers that are present in <strong>each array</strong> of</em> <code>nums</code><em> sorted in <strong>ascending order</strong></em>.
<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [[<u><strong>3</strong></u>,1,2,<u><strong>4</strong></u>,5],[1,2,<u><strong>3</strong></u>,<u><strong>4</strong></u>],[<u><strong>3</strong></u>,<u><strong>4</strong></u>,5,6]]
<strong>Output:</strong> [3,4]
<strong>Explanation:</strong> 
The only integers present in each of nums[0] = [<u><strong>3</strong></u>,1,2,<u><strong>4</strong></u>,5], nums[1] = [1,2,<u><strong>3</strong></u>,<u><strong>4</strong></u>], and nums[2] = [<u><strong>3</strong></u>,<u><strong>4</strong></u>,5,6] are 3 and 4, so we return [3,4].</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [[1,2,3],[4,5,6]]
<strong>Output:</strong> []
<strong>Explanation:</strong> 
There does not exist any integer present both in nums[0] and nums[1], so we return an empty list [].
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 1000</code></li>
	<li><code>1 &lt;= sum(nums[i].length) &lt;= 1000</code></li>
	<li><code>1 &lt;= nums[i][j] &lt;= 1000</code></li>
	<li>All the values of <code>nums[i]</code> are <strong>unique</strong>.</li>
</ul>


# Solution 
* Nested for loop to make a counter for all the elements in the matrix. 
* Since all integers of nums[i] are distinct, if an integer is present in each array, its count will be equal to the total number of arrays.

```python
class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        counter = {}
        result = []
        n = len(nums)

        for i in range(n):
            for j in range(len(nums[i])):
                counter[nums[i][j]] = counter.get(nums[i][j], 0) + 1
        
        for num, freq in counter.items():
            if freq == n:
                result.append(num)

        return sorted(result)
```
* Using the array to track via the index 

```python
class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        n_lists = len(nums)
        counts = [0] * 1001
        # Count each distinct element per sub-array
        for arr in nums:
            # arr elements are guaranteed distinct, so no need for set(arr)
            for x in arr:
                counts[x] += 1

        # Now scan 1…1001; if counts[i] == n_lists, it appeared in _every_ list
        res = []
        for val in range(1, 1001):
            if counts[val] == n_lists:
                res.append(val)
        return res
```

# Optimal Solution 
```python
class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        
        intersection_nums = set(nums[0])
        for i in range(1, len(nums)):
            intersection_nums &= set(nums[i])
        return sorted(intersection_nums)
```
