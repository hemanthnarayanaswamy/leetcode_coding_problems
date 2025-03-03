<h2><a href="https://leetcode.com/problems/product-of-array-except-self">238. Product of Array Except Self</a></h2><h3>Medium</h3><hr><p>Given an integer array <code>nums</code>, return <em>an array</em> <code>answer</code> <em>such that</em> <code>answer[i]</code> <em>is equal to the product of all the elements of</em> <code>nums</code> <em>except</em> <code>nums[i]</code>.</p>

<p>The product of any prefix or suffix of <code>nums</code> is <strong>guaranteed</strong> to fit in a <strong>32-bit</strong> integer.</p>

<p>You must write an algorithm that runs in&nbsp;<code>O(n)</code>&nbsp;time and without using the division operation.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> nums = [1,2,3,4]
<strong>Output:</strong> [24,12,8,6]
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> nums = [-1,1,0,-3,3]
<strong>Output:</strong> [0,0,9,0,0]
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>-30 &lt;= nums[i] &lt;= 30</code></li>
	<li>The input is generated such that <code>answer[i]</code> is <strong>guaranteed</strong> to fit in a <strong>32-bit</strong> integer.</li>
</ul>

<p>&nbsp;</p>
<p><strong>Follow up:</strong>&nbsp;Can you solve the problem in <code>O(1)</code>&nbsp;extra&nbsp;space complexity? (The output array <strong>does not</strong> count as extra space for space complexity analysis.)</p>


## Solution Approach 
* The Logic is to pre-calculate the prefixProduct and postfixProduct for all the elements 
* Than Calculate the product for prefix and Postfix and append that into the result and that is the Answer we want. 

```
[-1,1,0,-3,3]
preprod = 1, postproduct = 1
1. i=0, a[0] = -1 
    pre = 1 
    post = 0
		result = 0

2. i=1, a[1]= 1
    pre = -1
		post = 0
		result = 0

3. i=2. a[2]=0
    pre = -1
		post = -9
		result = 9
So on 
result = [0,0,9,0,0]
```
1. We'll start a Loop to Compute the Prefix Product and Postfix Product by initialize them to [1]
2. `prefix_product.append(prefix_product[i-1]*nums[i-1]`
3. `postfix_product.append(postfix_product[-1]*nums[i+1])`
4. `result.append(prefix_product[i]*postfix_product[i])`

```python 
## Beats 20%
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        prefix_product = [1]
        postfix_product = [1]


        for i in range(1, len(nums)):
            prefix_product.append(prefix_product[i-1]*nums[i-1])
        
        for i in range(len(nums)-2, -1, -1):
            postfix_product.append(postfix_product[-1]*nums[i+1])
            
        postfix_product = postfix_product[::-1]

        for i in range(len(nums)):
            result.append(prefix_product[i]*postfix_product[i])
        

        return result
```

## Improved Solution
* We are reducing the Space Complexity by reuse the result to store prefix and postfix products 
```python
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1] * n  # Step 1: Initialize result with 1s

        # Step 2: Compute prefix products (Left to Right)
        prefix = 1
        for i in range(n):
            result[i] = prefix
            prefix *= nums[i]  # Update prefix for next iteration

        # Step 3: Compute postfix products (Right to Left)
        postfix = 1
        for i in range(n-1, -1, -1):
            result[i] *= postfix  # Multiply postfix value to result
            postfix *= nums[i]  # Update postfix for next iteration

        return result
 ```
