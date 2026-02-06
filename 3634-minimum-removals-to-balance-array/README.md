<h2><a href="https://leetcode.com/problems/minimum-removals-to-balance-array">3958. Minimum Removals to Balance Array</a></h2><h3>Medium</h3><hr><p>You are given an integer array <code>nums</code> and an integer <code>k</code>.</p>

<p>An array is considered <strong>balanced</strong> if the value of its <strong>maximum</strong> element is <strong>at most</strong> <code>k</code> times the <strong>minimum</strong> element.</p>

<p>You may remove <strong>any</strong> number of elements from <code>nums</code>​​​​​​​ without making it <strong>empty</strong>.</p>

<p>Return the <strong>minimum</strong> number of elements to remove so that the remaining array is balanced.</p>

<p><strong>Note:</strong> An array of size 1 is considered balanced as its maximum and minimum are equal, and the condition always holds true.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [2,1,5], k = 2</span></p>

<p><strong>Output:</strong> <span class="example-io">1</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>Remove <code>nums[2] = 5</code> to get <code>nums = [2, 1]</code>.</li>
	<li>Now <code>max = 2</code>, <code>min = 1</code> and <code>max &lt;= min * k</code> as <code>2 &lt;= 1 * 2</code>. Thus, the answer is 1.</li>
</ul>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,6,2,9], k = 3</span></p>

<p><strong>Output:</strong> <span class="example-io">2</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>Remove <code>nums[0] = 1</code> and <code>nums[3] = 9</code> to get <code>nums = [6, 2]</code>.</li>
	<li>Now <code>max = 6</code>, <code>min = 2</code> and <code>max &lt;= min * k</code> as <code>6 &lt;= 2 * 3</code>. Thus, the answer is 2.</li>
</ul>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [4,6], k = 2</span></p>

<p><strong>Output:</strong> <span class="example-io">0</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>Since <code>nums</code> is already balanced as <code>6 &lt;= 4 * 2</code>, no elements need to be removed.</li>
</ul>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
	<li><code>1 &lt;= k &lt;= 10<sup>5</sup></code></li>
</ul>

# Solution 
1. sort array
**Rewriting the question- `find the maximum length subarray such the the following condition is valid`**
* `minimum * k >= maximum element`
* now use sliding window - find maxlength by expanding window and shrinking always from left.
* If you think to shrink from right then the loop must terminate in next step as all elements should be removed from right.

```python
class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        moves = float('inf')

        l, r = 0, 1

        while r < n:
            if nums[r] > k * nums[l]:
                moves = min(moves, n - (r - l))
                l += 1
            else:
                r += 1
        
        moves = min(moves, n - (r - l))
        
        return 0 if moves == float('inf') else moves
```
---
```python
class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        l = 0
        
        for r in range(len(nums)):
            if nums[r] > nums[l] * k:
                l += 1
        return l
```
* It finds the largest valid window where: 'max < min * k` and counts how many elements must be removed to achieve that.
But instead of returning: `len(nums) - size_of_largest_valid_window` --> `l`, which is the number of elements that were “pushed out” from the left.

```ini
Sorted: 
Window checks:
• 	r=0 → window = [1] → valid
• 	r=1 → window = [1,3] → 3 ≤ 1*3 → valid
• 	r=2 → window = [1,3,9] → 9 > 1*3 → invalid → l=1
Now window = [3,9] → valid
• 	r=3 → window = [3,9,10] → 10 > 3*3 → invalid → l=2
Now window = [9,10] → valid
Final  → remove 2 elements.
```
