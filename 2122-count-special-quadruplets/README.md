<h2><a href="https://leetcode.com/problems/count-special-quadruplets">2122. Count Special Quadruplets</a></h2><h3>Easy</h3><hr><p>Given a <strong>0-indexed</strong> integer array <code>nums</code>, return <em>the number of <strong>distinct</strong> quadruplets</em> <code>(a, b, c, d)</code> <em>such that:</em></p>

<ul>
	<li><code>nums[a] + nums[b] + nums[c] == nums[d]</code>, and</li>
	<li><code>a &lt; b &lt; c &lt; d</code></li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,2,3,6]
<strong>Output:</strong> 1
<strong>Explanation:</strong> The only quadruplet that satisfies the requirement is (0, 1, 2, 3) because 1 + 2 + 3 == 6.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [3,3,6,4,5]
<strong>Output:</strong> 0
<strong>Explanation:</strong> There are no such quadruplets in [3,3,6,4,5].
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,1,1,3,5]
<strong>Output:</strong> 4
<strong>Explanation:</strong> The 4 quadruplets that satisfy the requirement are:
- (0, 1, 2, 3): 1 + 1 + 1 == 3
- (0, 1, 3, 4): 1 + 1 + 3 == 5
- (0, 2, 3, 4): 1 + 1 + 3 == 5
- (1, 2, 3, 4): 1 + 1 + 3 == 5
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>4 &lt;= nums.length &lt;= 50</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 100</code></li>
</ul>

## Solution Approach 
* we are going with the brute force appraoch first 

```python
class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        lenN = len(nums)
        uniq_quad = 0
				
        for a in range(lenN-3):
             for b in range(a+1,lenN):
                   for c in range(b+1,lenN):
                         for d in range(c+1,lenN):
                                  if nums[a] + nums[b] + nums[c] == nums[d]:
                                          uniq_quad +=1

        return uniq_quad
```

## Optimized Solution 
- ``a+b+c = d -----------------------> a+b = d-c`` is the basic we use to optimized the solution
- We first precompute sums of (a, b) in tot2.
- We then check whether any (c, d) pair satisfies nums[d] - nums[c] == nums[a] + nums[b].
- Since we iterate c from left to right, ordering constraints are naturally enforced.
- The solution splits the problem into two parts:
    1. Prefix Sum Calculation for (a, b) pairs (store in tot2 dictionary).
    2. Finding valid (c, d) pairs by checking nums[d] - nums[c] in tot2.
- Initialize Variables 
```python
count = 0  # Stores the final answer.
tot2 = defaultdict(int)  # A hashmap (defaultdict(int)) to store sums of (a, b) pairs
```
- `tot2[x]` keeps track of how many times a `sum x = nums[a] + nums[b]` has appeared.

- Iterate Over c (Processing c from Left to Right)
```
for c in range(2, len(nums)-1):
```

- Store (a, b) Prefix Sums in tot2
```python
b = c - 1
for a in range(b):
    tot2[nums[a] + nums[b]] += 1
```


```python
class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        count = 0
        tot2 = defaultdict(int)

        for c in range(2, len(nums)-1):
            b = c-1
            # a and b part - prefix sum.
            for a in range(b):
                tot2[nums[a]+nums[b]] += 1
            # c and d part - nums[d]-nums[c] == nums[a]+nums[b].
            for d in range(c+1, len(nums)):
                count += tot2[nums[d]-nums[c]]
        
        return count
```

- The difference is that a defaultdict will "default" a value if that key has not been set yet. If you didn't use a defaultdict you'd have to check to see if that key exists, and if it doesn't, set it to what you want.

- Solution without using default dict

```python
class Solution:
    def countQuadruplets(self, nums: list[int]) -> int:
        count = 0
        tot2 = {}  # Using a regular dictionary instead of defaultdict

        for c in range(2, len(nums) - 1):
            b = c - 1

            # Store all (nums[a] + nums[b]) sums in dictionary
            for a in range(b):
                pair_sum = nums[a] + nums[b]
                if pair_sum in tot2:
                    tot2[pair_sum] += 1  # Increment count if already exists
                else:
                    tot2[pair_sum] = 1  # Initialize the sum count

            # Check for valid quadruplets (nums[d] - nums[c] == nums[a] + nums[b])
            for d in range(c + 1, len(nums)):
                target = nums[d] - nums[c]
                if target in tot2:
                    count += tot2[target]  # Add valid quadruplets found

        return count
```
