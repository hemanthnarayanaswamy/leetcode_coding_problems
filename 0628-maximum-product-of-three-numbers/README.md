<h2><a href="https://leetcode.com/problems/maximum-product-of-three-numbers">628. Maximum Product of Three Numbers</a></h2><h3>Easy</h3><hr><p>Given an integer array <code>nums</code>, <em>find three numbers whose product is maximum and return the maximum product</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> nums = [1,2,3]
<strong>Output:</strong> 6
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> nums = [1,2,3,4]
<strong>Output:</strong> 24
</pre><p><strong class="example">Example 3:</strong></p>
<pre><strong>Input:</strong> nums = [-1,-2,-3]
<strong>Output:</strong> -6
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>3 &lt;= nums.length &lt;=&nbsp;10<sup>4</sup></code></li>
	<li><code>-1000 &lt;= nums[i] &lt;= 1000</code></li>
</ul>

# Approach
```
If all the values are positive :  ( 1 2 3 4 5 )
                  return the product of the last 3 values (3*4*5) 
```
```
If all the values are negative :  ( -5 -4 -3 -2 -1 )

-5  -4  -3  -2  -1
            |____|
                      |-- These 2 MAXIMUM NEGATIVE values product make the MINIMUM 
                      POSITIVE VALUE of 2 than any other two negative values e.g. -4 x -3 = 12, 
               -5 x -4 = 20. One more value remains to be multiplied. 2 x -3 = -6, 12 x -1 = -12
           , 20 * -1 = -20.. -6 > -12 > -20.. So 3 MAXIMUM NEGATIVE VALUES gives us the
      MAXIMUM PRODUCT.  

  So we return nums[last index] * nums[last 2nd index] * nums[last 3rd index] 
```
```
If some values are positive and some negative :
        
    -4  -3  -2  -1  1  2  3  4

Just because we have 3 positive values doesn't mean we will return the product 
of the last 3 positive values CAUSE if the first 2 values are negative(-4,-3) 
then these 2 negative values might make MORE LARGER POSITIVE PRODUCT THAN THE 
LAST 2 POSITIVE VALUES!

     -4 * -3 =  +12 AND 12 * 4(MAXIMUM POSITVE VALUE) = 60
     WHERE 4 * 3 * 2 = 24
```
```
So as you can see our answer is either nums[0] * nums[1] * nums[last index] or
nums[last index] * nums[last 2nd index] * nums[last 3rd index] 
means the maximum of these 2 products.  
```

```python
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        numsSort = sorted(nums, reverse=True)
        
        return max(numsSort[-1]*numsSort[-2]*numsSort[0], numsSort[0]*numsSort[1]*numsSort[2])
```

## Improved 
```python
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        prod1 = nums[0] * nums[1] * nums[-1]
        prod2 = nums[-1] * nums[-2] * nums[-3]
        
        return max(prod1, prod2)
```
