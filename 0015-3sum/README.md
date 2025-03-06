<h2><a href="https://leetcode.com/problems/3sum">15. 3Sum</a></h2><h3>Medium</h3><hr><p>Given an integer array nums, return all the triplets <code>[nums[i], nums[j], nums[k]]</code> such that <code>i != j</code>, <code>i != k</code>, and <code>j != k</code>, and <code>nums[i] + nums[j] + nums[k] == 0</code>.</p>

<p>Notice that the solution set must not contain duplicate triplets.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [-1,0,1,2,-1,-4]
<strong>Output:</strong> [[-1,-1,2],[-1,0,1]]
<strong>Explanation:</strong> 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [0,1,1]
<strong>Output:</strong> []
<strong>Explanation:</strong> The only possible triplet does not sum up to 0.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums = [0,0,0]
<strong>Output:</strong> [[0,0,0]]
<strong>Explanation:</strong> The only possible triplet sums up to 0.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>3 &lt;= nums.length &lt;= 3000</code></li>
	<li><code>-10<sup>5</sup> &lt;= nums[i] &lt;= 10<sup>5</sup></code></li>
</ul>

## Solution Approach 
* Here is the Brute Force Approach, which iterates three times and checks for the given condition.
```python
def threesum(nums):
result = []
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            for k in range(j+1, len(nums)):
                if nums[i] + nums[j] + nums[k] == 0:
                    result.append([nums[i], nums[j], nums[k]])
    return result
```

## Solution using the TWO-POINTER 
* First we'll sort the array that way least values elements are in the front and highest value elements are at the back 
* Now we'll do a iteration on the sorted array, and then use the two pointer approach to check if the sum of the two pointer elements is equal to `-num[i]`
```
num[i]+num[j]+num[k] = 0
num]j] + num[k] = -num[i]
``` 

* First, we sort the input array. This makes it easier to avoid duplicates and apply the two-pointer technique.
* Iterate through the array and fix one element at a time. For each fixed element, use two pointers to find pairs that sum to the negative of the fixed element.
* Skip duplicate elements to ensure all triplets in the result are unique.

```python
def threesum(nums):
    result = set()
    nums.sort()

    for i in range(len(nums)-2):
        if nums[i] > 0:                     ## Checking for any impossible sums
            break
        if i > 0 and nums[i] == nums[i-1]:  ## Skip duplicate values for i
            continue
        left, right = i + 1, len(nums) - 1
        while left < right:
            total = nums[left] + nums[right] + nums[i]
            if total == 0:
                result.add((nums[i], nums[left], nums[right]))
                left += 1
                right -= 1
            elif total < 0: # If total is less than 0, we need to increase the sum so left pointer needs to move for higher number
                left += 1
            else:
                right -= 1
    return list(result)
```
