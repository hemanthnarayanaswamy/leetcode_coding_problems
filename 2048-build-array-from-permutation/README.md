<h2><a href="https://leetcode.com/problems/build-array-from-permutation">2048. Build Array from Permutation</a></h2><h3>Easy</h3><hr><p>Given a <strong>zero-based permutation</strong> <code>nums</code> (<strong>0-indexed</strong>), build an array <code>ans</code> of the <strong>same length</strong> where <code>ans[i] = nums[nums[i]]</code> for each <code>0 &lt;= i &lt; nums.length</code> and return it.</p>

<p>A <strong>zero-based permutation</strong> <code>nums</code> is an array of <strong>distinct</strong> integers from <code>0</code> to <code>nums.length - 1</code> (<strong>inclusive</strong>).</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [0,2,1,5,3,4]
<strong>Output:</strong> [0,1,2,4,5,3]<strong>
Explanation:</strong> The array ans is built as follows: 
ans = [nums[nums[0]], nums[nums[1]], nums[nums[2]], nums[nums[3]], nums[nums[4]], nums[nums[5]]]
    = [nums[0], nums[2], nums[1], nums[5], nums[3], nums[4]]
    = [0,1,2,4,5,3]</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [5,0,1,2,3,4]
<strong>Output:</strong> [4,5,0,1,2,3]
<strong>Explanation:</strong> The array ans is built as follows:
ans = [nums[nums[0]], nums[nums[1]], nums[nums[2]], nums[nums[3]], nums[nums[4]], nums[nums[5]]]
    = [nums[5], nums[0], nums[1], nums[2], nums[3], nums[4]]
    = [4,5,0,1,2,3]</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 1000</code></li>
	<li><code>0 &lt;= nums[i] &lt; nums.length</code></li>
	<li>The elements in <code>nums</code> are <strong>distinct</strong>.</li>
</ul>

<p>&nbsp;</p>
<p><strong>Follow-up:</strong> Can you solve it without using an extra space (i.e., <code>O(1)</code> memory)?</p>

## Solution with Normal Approach 
```python
class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ans = [0]*len(nums)

        for i in range(len(nums)):
            ans[i] = nums[nums[i]]
        
        return ans 
```

## Optimal solution with `O(1)` Space Complexity 
* The intuition behind doing the problem in constant space is that we must process the original array: in-place, in a way that allows us to move the correct value (nums[nums[i]) to it's correct place (i), while also keeping the original value, (nums[i]), in-place, in some way so that we can use it when needed later.
* To accomplish this task, we're going to use the fact that if we have a number of the form a = qb + r, where b and r are not multiples of q and r < q, then we can extract b and r with the following:
```
b = a // q (where // is integer division)
```
* we know that qb when divided by q will give us b, however we still would need to get rid of the `r // q`. From our requirements though, `r < q`, so `r // q` will always be 0, thus `b = (qb//q) + (r//q) = b + 0 = b`
* `r = a % q` - we know that qb is a multiple of q, thus is divided by it cleanly and we know that r < q, so r is not a multiple of q, therefore the remainder when dividing a = qb + r by q is just r

* At every i, nums[nums[i]] is going to be our b and the original value, nums[i] is our r.
* Now we just need a q that satisfies the r < q, for all the possible r values (all nums[i]). Luckily, we have such a q already, as our array values are indices into the same array. q = len(nums) is always guaranteed to be greater than all nums[i] because each index is always within the bounds of the array, from 0 to len(nums) - 1.

```python
def buildArray(nums: List[int]) -> List[int]:
  q = len(nums)
  
  # turn the array into a=qb+r
  for i in range(len(nums)):
	r = nums[i]
	
	# retrieve correct value from potentially already processed element
	# i.e. get r from something maybe already in the form a = qb + r
	# if it isnt already processed (doesnt have qb yet), that's ok b/c
	# r < q, so r % q will return the same value
	b = nums[nums[i]] % q
	
    # put it all together
	nums[i] = q*b + r
	
# extract just the final b values
  for i in range(len(nums)):
    nums[i] = nums[i] // q
  
  return nums
```
