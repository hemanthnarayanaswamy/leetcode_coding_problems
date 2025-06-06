<h2><a href="https://leetcode.com/problems/sort-array-by-parity-ii">958. Sort Array By Parity II</a></h2><h3>Easy</h3><hr><p>Given an array of integers <code>nums</code>, half of the integers in <code>nums</code> are <strong>odd</strong>, and the other half are <strong>even</strong>.</p>

<p>Sort the array so that whenever <code>nums[i]</code> is odd, <code>i</code> is <strong>odd</strong>, and whenever <code>nums[i]</code> is even, <code>i</code> is <strong>even</strong>.</p>

<p>Return <em>any answer array that satisfies this condition</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [4,2,5,7]
<strong>Output:</strong> [4,5,2,7]
<strong>Explanation:</strong> [4,7,2,5], [2,5,4,7], [2,7,4,5] would also have been accepted.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [2,3]
<strong>Output:</strong> [2,3]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= nums.length &lt;= 2 * 10<sup>4</sup></code></li>
	<li><code>nums.length</code> is even.</li>
	<li>Half of the integers in <code>nums</code> are even.</li>
	<li><code>0 &lt;= nums[i] &lt;= 1000</code></li>
</ul>

<p>&nbsp;</p>
<p><strong>Follow Up:</strong> Could you solve it in-place?</p>

# Approach 
* Thinking of using the two pointer approach to solve the problem
* Normal approach solution is easy, sepeate the odd and even integers sort them and while zipping them in a iteration store the result and return it.
**In-Place Computation**
```python
class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        even, odd = 0, 1

        while even < len(nums)-1 and odd < len(nums):

            evenIdx, oddIdx = nums[even]%2, nums[odd]%2
            
            if evenIdx == 0:
                if oddIdx == 1:
                    even += 2
                    odd += 2
                else:
                    even += 2
            else: 
                if oddIdx == 1:
                    odd += 2
                else:
                    nums[even], nums[odd] = nums[odd], nums[even]
                    even += 2
                    odd += 2

        return nums
```

## Improved Approach
```python
class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        even, odd = 0, 1
        n = len(nums)

        while even < n and odd < n:
            if nums[even] % 2 == 0:
                even += 2
            elif nums[odd] % 2 == 1:
                odd += 2
            else:
                nums[even], nums[odd] = nums[odd], nums[even]
                even += 2
                odd += 2

        return nums
```
--------------------------------------------------------
**Usual computation**
```python
class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        evenInd = 0
        oddInd = 1
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                res[evenInd] = nums[i]
                evenInd += 2
            if nums[i] % 2 == 1:
                res[oddInd] = nums[i]
                oddInd += 2
        return res
```

