<h2><a href="https://leetcode.com/problems/count-pairs-whose-sum-is-less-than-target">2917. Count Pairs Whose Sum is Less than Target</a></h2><h3>Easy</h3><hr>Given a <strong>0-indexed</strong> integer array <code>nums</code> of length <code>n</code> and an integer <code>target</code>, return <em>the number of pairs</em> <code>(i, j)</code> <em>where</em> <code>0 &lt;= i &lt; j &lt; n</code> <em>and</em> <code>nums[i] + nums[j] &lt; target</code>.
<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [-1,1,2,3,1], target = 2
<strong>Output:</strong> 3
<strong>Explanation:</strong> There are 3 pairs of indices that satisfy the conditions in the statement:
- (0, 1) since 0 &lt; 1 and nums[0] + nums[1] = 0 &lt; target
- (0, 2) since 0 &lt; 2 and nums[0] + nums[2] = 1 &lt; target 
- (0, 4) since 0 &lt; 4 and nums[0] + nums[4] = 0 &lt; target
Note that (0, 3) is not counted since nums[0] + nums[3] is not strictly less than the target.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [-6,2,5,-2,-7,-1,3], target = -2
<strong>Output:</strong> 10
<strong>Explanation:</strong> There are 10 pairs of indices that satisfy the conditions in the statement:
- (0, 1) since 0 &lt; 1 and nums[0] + nums[1] = -4 &lt; target
- (0, 3) since 0 &lt; 3 and nums[0] + nums[3] = -8 &lt; target
- (0, 4) since 0 &lt; 4 and nums[0] + nums[4] = -13 &lt; target
- (0, 5) since 0 &lt; 5 and nums[0] + nums[5] = -7 &lt; target
- (0, 6) since 0 &lt; 6 and nums[0] + nums[6] = -3 &lt; target
- (1, 4) since 1 &lt; 4 and nums[1] + nums[4] = -5 &lt; target
- (3, 4) since 3 &lt; 4 and nums[3] + nums[4] = -9 &lt; target
- (3, 5) since 3 &lt; 5 and nums[3] + nums[5] = -3 &lt; target
- (4, 5) since 4 &lt; 5 and nums[4] + nums[5] = -8 &lt; target
- (4, 6) since 4 &lt; 6 and nums[4] + nums[6] = -4 &lt; target
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length == n &lt;= 50</code></li>
	<li><code>-50 &lt;= nums[i], target &lt;= 50</code></li>
</ul>


# Brute Force Solution 
**If you find a pair (a, b) and flip it (b, a) one of them's index is still lesser than other. it doesnt matter if you sort or not. it only matters that you count it once. the condition 0<=i<j<n is trying to say count one pair only once.** 
```python
class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        count = 0
        n = len(nums)

        for i in range(n -1):
            for j in range(i+1, n):
                if nums[i] + nums[j] < target:
                    count += 1
                    
        return count
```

* The problem asks for the count of pairs `(i, j)` where `nums[i] + nums[j] < target`. It doesn't ask us to return the actual indices - just the count.

### Sorting doesn't change the number of valid pairs because:

* We're looking for pairs of values that sum to less than target
* The combination of values remains the same regardless of their positions
* We only care about the count, not the actual index pairs

***If the problem asked to return the actual index pairs, then we couldn't sort:***

### Why Two Pointers Works:
* Key Insight: After sorting, if `nums[left] + nums[right] < target`, then:
```ini
nums[left] + nums[left+1] < target
nums[left] + nums[left+2] < target
...
nums[left] + nums[right] < target
```
* All pairs with left as the first element and any index from left+1 to right will be valid.

```python
nums = [1, 3, 2, 4], target = 5
After sorting: [1, 2, 3, 4]

left=0, right=3: nums[0]+nums[3] = 1+4 = 5 >= 5 → right--
left=0, right=2: nums[0]+nums[2] = 1+3 = 4 < 5 → count += 2-0 = 2, left++
left=1, right=2: nums[1]+nums[2] = 2+3 = 5 >= 5 → right--
left=1, right=1: left == right, stop

Total count = 2 (pairs: (1,2), (1,3))
```

```ini
# If current pair sum < target, then all pairs 
 (left, left+1), (left, left+2), ..., (left, right) are valid
 
 count += right - left 
```
---
```python
class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        if len(nums) < 2:
            return 0
            
        nums.sort()
        left, right = 0, len(nums) - 1
        count = 0
        
        while left < right:
            if nums[left] + nums[right] < target:
                count += right - left
                left += 1
            else:
                right -= 1
        
        return count
```
