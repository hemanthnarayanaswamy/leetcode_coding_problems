<h2><a href="https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number">1482. How Many Numbers Are Smaller Than the Current Number</a></h2><h3>Easy</h3><hr><p>Given the array <code>nums</code>, for each <code>nums[i]</code> find out how many numbers in the array are smaller than it. That is, for each <code>nums[i]</code> you have to count the number of valid <code>j&#39;s</code>&nbsp;such that&nbsp;<code>j != i</code> <strong>and</strong> <code>nums[j] &lt; nums[i]</code>.</p>

<p>Return the answer in an array.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [8,1,2,2,3]
<strong>Output:</strong> [4,0,1,1,3]
<strong>Explanation:</strong> 
For nums[0]=8 there exist four smaller numbers than it (1, 2, 2 and 3). 
For nums[1]=1 does not exist any smaller number than it.
For nums[2]=2 there exist one smaller number than it (1). 
For nums[3]=2 there exist one smaller number than it (1). 
For nums[4]=3 there exist three smaller numbers than it (1, 2 and 2).
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [6,5,4,8]
<strong>Output:</strong> [2,1,0,3]
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums = [7,7,7,7]
<strong>Output:</strong> [0,0,0,0]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= nums.length &lt;= 500</code></li>
	<li><code>0 &lt;= nums[i] &lt;= 100</code></li>
</ul>

# Solution
* Keep a sorted array to track the index which gives how many numbers are greater then the currrent number.
* Iterate through the original array and find its index in the sorted array to append into the result.

```python
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        nums_sorted = sorted(nums)
        result = [0]*len(nums)

        for i in range(len(nums)): 
            result[i] = nums_sorted.index(nums[i])

        return result
```

## Optinal Solution
* In the above code we have O(n*2) complexity as we are computing the index which is like a nested loop.
* To remove that we use a hashMap to store the sorted result in it with its index.

```python
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        nums_sorted = sorted(nums)
        tempMap = {}
        
        n = len(nums)

        for i,num in enumerate(nums_sorted): 
            if num not in tempMap:
                tempMap[num] = i 
    

        result = [0]*len(nums)

        for i in range(n):
            result[i] = tempMap[nums[i]]
        
        return result
```
