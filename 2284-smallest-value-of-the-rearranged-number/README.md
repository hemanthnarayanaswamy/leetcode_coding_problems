<h2><a href="https://leetcode.com/problems/smallest-value-of-the-rearranged-number">2284. Smallest Value of the Rearranged Number</a></h2><h3>Medium</h3><hr><p>You are given an integer <code>num.</code> <strong>Rearrange</strong> the digits of <code>num</code> such that its value is <strong>minimized</strong> and it does not contain <strong>any</strong> leading zeros.</p>

<p>Return <em>the rearranged number with minimal value</em>.</p>

<p>Note that the sign of the number does not change after rearranging the digits.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> num = 310
<strong>Output:</strong> 103
<strong>Explanation:</strong> The possible arrangements for the digits of 310 are 013, 031, 103, 130, 301, 310. 
The arrangement with the smallest value that does not contain any leading zeros is 103.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> num = -7605
<strong>Output:</strong> -7650
<strong>Explanation:</strong> Some possible arrangements for the digits of -7605 are -7650, -6705, -5076, -0567.
The arrangement with the smallest value that does not contain any leading zeros is -7650.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>-10<sup>15</sup> &lt;= num &lt;= 10<sup>15</sup></code></li>
</ul>

# Solution

- Have two scenarios :
1. What if the number is negative..?
2. What if the number is positive..?

## Approach
```
num is zero:
Do nothing and return zero.
```
```
num is negative:
Remove the sign.
Sort the digits in descending order.
Combine the sorted digits.
Reassign the original sign (i.e) -ve and return the value.
```

num is positive:
Count number of zeroes in the num
Sort the digits in asc order.
The first leading zero is swapped with the first non zero digit.
Combining the digits.
Return the value.

```
else:
    num = str(num) // convert to string
    count = num.count('0') // counting zeros
    num = sorted(num) // sorting digits in asc order
    num = num[count:count+1] + ['0']*count + num[count+1:] // swapping
    num = int(''.join(num)) // combining
    return num // final answer
		
For example, num = 809123546.
Step-1: num = str(num) => num = "809123546"
Step-2: count = num.count("0")
Step-3: num = sorted(num) => num = ['0','1','2','3','4','5','6','8','9']
Step-4: num = ['1','0','2','3','4','5','6','8','9'] // swapped
Step-5: num = 102345689 // Final answer
```

### SWAPPING LOGIC 
* To swap we get the number of zeros present in the number list which is sorted in ascending order, when its sorted in ascending order all the zeros are at the beginning 
* so basically what we need to do is to remove the zeros and find the first occurance of non-zero digit in soeted list which can be done by `num[count:count+1] `
* then add number of zeros present 
* and merge the rest of the list 

Complexity
Time complexity: O(Nlogn)
Space complexity: O(N)

```python
class Solution:
    def smallestNumber(self, num: int) -> int:
        if num == 0:
            return 0
        
        if num < 0:
            num = -num 
            num = sorted(str(num), reverse=True)
            num = int(''.join(num))
            return -num
        else:
            num = sorted(str(num))
            count = num.count('0')
            if count > 0:
                num = num[count: count+1] + ['0']*count + num[count+1:]
            num = int(''.join(num))

            return num
```
