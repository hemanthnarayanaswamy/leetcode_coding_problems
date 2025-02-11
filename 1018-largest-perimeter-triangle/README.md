<h2><a href="https://leetcode.com/problems/largest-perimeter-triangle">1018. Largest Perimeter Triangle</a></h2><h3>Easy</h3><hr><p>Given an integer array <code>nums</code>, return <em>the largest perimeter of a triangle with a non-zero area, formed from three of these lengths</em>. If it is impossible to form any triangle of a non-zero area, return <code>0</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [2,1,2]
<strong>Output:</strong> 5
<strong>Explanation:</strong> You can form a triangle with three side lengths: 1, 2, and 2.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,2,1,10]
<strong>Output:</strong> 0
<strong>Explanation:</strong> 
You cannot use the side lengths 1, 1, and 2 to form a triangle.
You cannot use the side lengths 1, 1, and 10 to form a triangle.
You cannot use the side lengths 1, 2, and 10 to form a triangle.
As we cannot use any three side lengths to form a triangle of non-zero area, we return 0.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>3 &lt;= nums.length &lt;= 10<sup>4</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>6</sup></code></li>
</ul>

### APPROACH 
1. If the side of a triangle are `a,b,c` then `a+b>c` for the triangle to be formed .
2. Sort the array to get the maximum element of the array at a side ;
3. Traverse the array bacckward to find `nums[i]<nums[i-1]+nums[i-2]` till the index 2 as i-2 will get out of bound ,
4. Store the value of it in ans (default value is 0) and return it .

```python 
class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums_lenght = len(nums)
        if nums_lenght < 3: ## If the given lengths are less than 3 sides return 0
            return 0
    
        nums.sort() ## sorting the array 

        for i in range(nums_lenght-1, -1, -1): ## We are starting from the largest side
            sum_of_sides = nums[i-1] + nums[i-2]
            largest_side = nums[i]
            if i-2 >= 0 and largest_side < sum_of_sides:
                return largest_side + sum_of_sides
        return 0
```

* <b> This is similar to my solution but note how they are using the range to stop at the exact index      `range(len(nums)-1, 1, -1)`</b> 

```python
def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums)-1, 1, -1):
            if nums[i] < nums[i-1] + nums[i-2]:
                return nums[i] + nums[i-1] + nums[i-2]
        return 0
```

### Optimized Solution 

```python
def largestPerimeter(self, nums: List[int]) -> int:
        # inequality triangle a + b > c, a + c > b, and b + c > a.

        # sort list in descending order 
        nums.sort(reverse=True) ## REversing the sorting order to make it easier
        # print(nums)

        for i in range(len(nums) - 2): ## using range normally will help 
        # if meets condition (a+b > c), then return sum
            if nums[i] < nums[i + 1] + nums[i + 2]:
                return nums[i] + nums[i + 1] + nums[i + 2]
        # else return 0;
        return 0
