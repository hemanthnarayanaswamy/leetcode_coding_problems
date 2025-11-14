<h2><a href="https://leetcode.com/problems/minimum-distance-between-three-equal-elements-i">4115. Minimum Distance Between Three Equal Elements I</a></h2><h3>Easy</h3><hr><p>You are given an integer array <code>nums</code>.</p>

<p>A tuple <code>(i, j, k)</code> of 3 <strong>distinct</strong> indices is <strong>good</strong> if <code>nums[i] == nums[j] == nums[k]</code>.</p>

<p>The <strong>distance</strong> of a <strong>good</strong> tuple is <code>abs(i - j) + abs(j - k) + abs(k - i)</code>, where <code>abs(x)</code> denotes the <strong>absolute value</strong> of <code>x</code>.</p>

<p>Return an integer denoting the <strong>minimum</strong> possible <strong>distance</strong> of a <strong>good</strong> tuple. If no <strong>good</strong> tuples exist, return <code>-1</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,2,1,1,3]</span></p>

<p><strong>Output:</strong> <span class="example-io">6</span></p>

<p><strong>Explanation:</strong></p>

<p>The minimum distance is achieved by the good tuple <code>(0, 2, 3)</code>.</p>

<p><code>(0, 2, 3)</code> is a good tuple because <code>nums[0] == nums[2] == nums[3] == 1</code>. Its distance is <code>abs(0 - 2) + abs(2 - 3) + abs(3 - 0) = 2 + 1 + 3 = 6</code>.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,1,2,3,2,1,2]</span></p>

<p><strong>Output:</strong> <span class="example-io">8</span></p>

<p><strong>Explanation:</strong></p>

<p>The minimum distance is achieved by the good tuple <code>(2, 4, 6)</code>.</p>

<p><code>(2, 4, 6)</code> is a good tuple because <code>nums[2] == nums[4] == nums[6] == 2</code>. Its distance is <code>abs(2 - 4) + abs(4 - 6) + abs(6 - 2) = 2 + 2 + 4 = 8</code>.</p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1]</span></p>

<p><strong>Output:</strong> <span class="example-io">-1</span></p>

<p><strong>Explanation:</strong></p>

<p>There are no good tuples. Therefore, the answer is -1.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n == nums.length &lt;= 100</code></li>
	<li><code>1 &lt;= nums[i] &lt;= n</code></li>
</ul>

# Approach
* Your observation is the key to this problem. The distance formula is: `Distance = abs(i - j) + abs(j - k) + abs(k - i)`
* Let's find a good tuple `(i, j, k)` and sort the indices, calling them `a, b, c` such that `a < b < c .abs(i - j) abs(j - k) abs(k - i)`
When we plug them in, the formula becomes: `Distance = abs(a - b) + abs(b - c) + abs(c - a)` Since we know `a < b < c`, **we can remove the absolute value signs:**
```ini
abs(a - b) = b - a
abs(b - c) = c - b
abs(c - a) = c - a
```
* Now, let's add them together: `Distance = (b - a) + (c - b) + (c - a)` -> `Distance = -a + c + c - a` -> `Distance = 2 * (c - a)`
**The distance of any good tuple is just 2 times the difference between its largest and smallest index. The middle index doesn't affect the final distance at all.**

**Our goal is no longer to find the minimum `abs(i - j) + abs(j - k) + abs(k - i)`, but to find the minimum `2 * (max_index - min_index)` for any three indices that point to the same value.**

```python
class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        res = float('inf')
        numsMap = defaultdict(list)

        for i in range(len(nums)):
            numsMap[nums[i]].append(i)
						n = len(numsMap[nums[i]]) 
            if n == 3:
                l = numsMap[nums[i]][0]
                u = numsMap[nums[i]][-1]
                res = min(res, 2*(u - l))
            elif n > 3:
                numsMap[nums[i]].pop(0)
                l = numsMap[nums[i]][0]
                u = numsMap[nums[i]][-1]
                res = min(res, 2*(u - l))
            
        return res if res != float('inf') else -1
```
* We store all the index of the elements in the map, and when the `len()` is equal to 3 we calculate the distance, and if we have more then 3 element we `pop()` the first element index and have the only 3 elements. 

```python
class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        res = float('inf')
        numsMap = defaultdict(list)

        for i in range(len(nums)):
            numsMap[nums[i]].append(i)
            n = len(numsMap[nums[i]]) 
            if n >= 3:
                if n > 3:
                    numsMap[nums[i]].pop(0)

                l = numsMap[nums[i]][0]
                res = min(res, 2*(i - l))
            
        return res if res != float('inf') else -1
```
