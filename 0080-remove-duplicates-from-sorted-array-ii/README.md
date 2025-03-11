<h2><a href="https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii">80. Remove Duplicates from Sorted Array II</a></h2><h3>Medium</h3><hr><p>Given an integer array <code>nums</code> sorted in <strong>non-decreasing order</strong>, remove some duplicates <a href="https://en.wikipedia.org/wiki/In-place_algorithm" target="_blank"><strong>in-place</strong></a> such that each unique element appears <strong>at most twice</strong>. The <strong>relative order</strong> of the elements should be kept the <strong>same</strong>.</p>

<p>Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the <strong>first part</strong> of the array <code>nums</code>. More formally, if there are <code>k</code> elements after removing the duplicates, then the first <code>k</code> elements of <code>nums</code>&nbsp;should hold the final result. It does not matter what you leave beyond the first&nbsp;<code>k</code>&nbsp;elements.</p>

<p>Return <code>k</code><em> after placing the final result in the first </em><code>k</code><em> slots of </em><code>nums</code>.</p>

<p>Do <strong>not</strong> allocate extra space for another array. You must do this by <strong>modifying the input array <a href="https://en.wikipedia.org/wiki/In-place_algorithm" target="_blank">in-place</a></strong> with O(1) extra memory.</p>

<p><strong>Custom Judge:</strong></p>

<p>The judge will test your solution with the following code:</p>

<pre>
int[] nums = [...]; // Input array
int[] expectedNums = [...]; // The expected answer with correct length

int k = removeDuplicates(nums); // Calls your implementation

assert k == expectedNums.length;
for (int i = 0; i &lt; k; i++) {
    assert nums[i] == expectedNums[i];
}
</pre>

<p>If all assertions pass, then your solution will be <strong>accepted</strong>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,1,1,2,2,3]
<strong>Output:</strong> 5, nums = [1,1,2,2,3,_]
<strong>Explanation:</strong> Your function should return k = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [0,0,1,1,1,1,2,3,3]
<strong>Output:</strong> 7, nums = [0,0,1,1,2,3,3,_,_]
<strong>Explanation:</strong> Your function should return k = 7, with the first seven elements of nums being 0, 0, 1, 1, 2, 3 and 3 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 3 * 10<sup>4</sup></code></li>
	<li><code>-10<sup>4</sup> &lt;= nums[i] &lt;= 10<sup>4</sup></code></li>
	<li><code>nums</code> is sorted in <strong>non-decreasing</strong> order.</li>
</ul>

## Solution Approach 
* This Problem is similar to how we have handle this problem 
https://leetcode.com/problems/remove-duplicates-from-sorted-array/
* we use a pointer techique to solve it one is `slow pointer` that will track the position where we write the next valid element.
* `fast pointer` will scan through the arry to find valid elements.
```python
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:   ## If nums has 2 or fewer elements, all are already valid
            return n
    
        slow = 2     ## Since the first two index are always valid 

        for fast in range(2, n):
            if nums[fast] != nums[slow - 2]:
                nums[slow] = nums[fast]    ## Overwrite the element at 'slow' index
                slow += 1
        return slow
```

## Improved approach
* we start with two pointers and use a count variable to track the count of the occurance .
* if the `nums[i] != nums[j]` then `nums[i + 1] = nums[j]`
* If they are not equal check the count, If it is `<2` then  `nums[i + 1] = nums[j]`
```python
def removeDuplicates(nums):
    if len(nums) < 2:
        return len(nums)
    i, j = 0, 1
    count = 1  # A number is always valid 

    for j in range(1, len(nums)):
        if nums[i] != nums[j]:  ## If number are not equal move the slow pointer and asign the value 
            nums[i + 1] = nums[j]
            i += 1
            count = 1
        elif count < 2:           ## If they are equal than chekc the count value 
            nums[i + 1] = nums[j]
            i += 1
            count += 1
    return i + 1
```
