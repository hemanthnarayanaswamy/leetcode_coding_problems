<h2><a href="https://leetcode.com/problems/contains-duplicate-ii">219. Contains Duplicate II</a></h2><h3>Easy</h3><hr><p>Given an integer array <code>nums</code> and an integer <code>k</code>, return <code>true</code> <em>if there are two <strong>distinct indices</strong> </em><code>i</code><em> and </em><code>j</code><em> in the array such that </em><code>nums[i] == nums[j]</code><em> and </em><code>abs(i - j) &lt;= k</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,2,3,1], k = 3
<strong>Output:</strong> true
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,0,1,1], k = 1
<strong>Output:</strong> true
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,2,3,1,2,3], k = 2
<strong>Output:</strong> false
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

## Solution Approach 
* Here the only catch is we need to find the ` j` element which is at `k` distance from `i`.
* abs(i - j) <= k ---> abs(i - k) <=j 

* I came up this solution but it is not able to cover all the edge cases like what is the number is <= k only checking for == k 
```python
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        lenght_nums = len(nums)
        for i in range(lenght_nums):
            j = abs(i - k)
            if j != lenght_nums:
                if j != i and nums[j] == nums[i]:
                    return True
        return False
```

* <B>Brute FORCE approach, Got error as `Time Limit Exceed `
```python
	class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        lenght_nums = len(nums)
        for i in range(lenght_nums):
            for j in range(i+1,lenght_nums):
                    if nums[i] == nums[j]:
                        return True 
        return False
```
## Optimized Approach 
	
* We need to use hash-map to store the visited number and for every number we check if the number exits in the map if yes than we try to calculate the `i-j` to check that condition.
* If true reture else add the recorded number into the map 
	
```python 
	class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        found_nums = {} ## HAsh Map to track the number
        
        for i,num in enumerate(nums):
            if num in found_nums and abs(i-found_nums[num]) <= k:   ## checking conditions #
								return True 
            else:
                found_nums[num] = i
        return False
```
* Using `Sliding window Technique`																																	
``` python 
def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = set()  # To track the elements in the current sliding window

        for i in range(len(nums)):
            # If the element is already in the set, it means a duplicate exists within the range k
            if nums[i] in seen:
                return True

            # Add the current element to the set
            seen.add(nums[i])

            # Maintain the size of the sliding window to at most k
            if len(seen) > k:
                seen.remove(nums[i - k])  # Remove the element that's out of range k

        return False
```
