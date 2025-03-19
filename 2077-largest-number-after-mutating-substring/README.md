<h2><a href="https://leetcode.com/problems/largest-number-after-mutating-substring">2077. Largest Number After Mutating Substring</a></h2><h3>Medium</h3><hr><p>You are given a string <code>num</code>, which represents a large integer. You are also given a <strong>0-indexed</strong> integer array <code>change</code> of length <code>10</code> that maps each digit <code>0-9</code> to another digit. More formally, digit <code>d</code> maps to digit <code>change[d]</code>.</p>

<p>You may <strong>choose</strong> to <b>mutate a single substring</b> of <code>num</code>. To mutate a substring, replace each digit <code>num[i]</code> with the digit it maps to in <code>change</code> (i.e. replace <code>num[i]</code> with <code>change[num[i]]</code>).</p>

<p>Return <em>a string representing the <strong>largest</strong> possible integer after <strong>mutating</strong> (or choosing not to) a <strong>single substring</strong> of </em><code>num</code>.</p>

<p>A <strong>substring</strong> is a contiguous sequence of characters within the string.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> num = &quot;<u>1</u>32&quot;, change = [9,8,5,0,3,6,4,2,6,8]
<strong>Output:</strong> &quot;<u>8</u>32&quot;
<strong>Explanation:</strong> Replace the substring &quot;1&quot;:
- 1 maps to change[1] = 8.
Thus, &quot;<u>1</u>32&quot; becomes &quot;<u>8</u>32&quot;.
&quot;832&quot; is the largest number that can be created, so return it.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> num = &quot;<u>021</u>&quot;, change = [9,4,3,5,7,2,1,9,0,6]
<strong>Output:</strong> &quot;<u>934</u>&quot;
<strong>Explanation:</strong> Replace the substring &quot;021&quot;:
- 0 maps to change[0] = 9.
- 2 maps to change[2] = 3.
- 1 maps to change[1] = 4.
Thus, &quot;<u>021</u>&quot; becomes &quot;<u>934</u>&quot;.
&quot;934&quot; is the largest number that can be created, so return it.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> num = &quot;5&quot;, change = [1,4,7,5,3,2,5,6,9,4]
<strong>Output:</strong> &quot;5&quot;
<strong>Explanation:</strong> &quot;5&quot; is already the largest number that can be created, so return it.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= num.length &lt;= 10<sup>5</sup></code></li>
	<li><code>num</code> consists of only digits <code>0-9</code>.</li>
	<li><code>change.length == 10</code></li>
	<li><code>0 &lt;= change[d] &lt;= 9</code></li>
</ul>

## Solution Approach 
* First we converted the List into a Hashmap for better Lookup and access complexity. 
* Then we use a flag and start index to start changeing from that index and store the result in other variable once i reaches the end we breaked and return the result. 

```python
class Solution:
    def maximumNumber(self, num: str, change: List[int]) -> str:
        change_map = {i:num for i, num in enumerate(change)}
        result = [] 
        i = 0
        while i < len(num):
            if int(num[i]) < change_map[int(num[i])]:
                result.append(str(change_map[int(num[i])]))
                i += 1
                while i < len(num):
                    if int(num[i]) > change_map[int(num[i])]:
                        result.append(num[i:len(num)])
                        i = len(num)
                        break
                    else:
                        result.append(str(change_map[int(num[i])]))
                        i += 1
            else:
                result.append(num[i])
                i += 1                

        return ''.join(result)
```				
* It is a big solution can be optimized more to reduce the time and space. 
* Remove the result variable and reuse the num string as list 

## Improved Solution 
```python
class Solution:
    def maximumNumber(self, num: str, change: List[int]) -> str:
        #change_map = {i:num for i, num in enumerate(change)}
        num = [s for s in num] 
        i = 0 
        while i < len(num):
            if int(num[i]) < change[int(num[i])]:
                while i < len(num):
                    if int(num[i]) > change[int(num[i])]:
                        return ''.join(num)
                    else:
                        num[i] = str(change[int(num[i])])
                        i += 1
            i += 1               

        return ''.join(num)
```
* Can be further Improved in terms of using the while loop. 
* and int and str conversions 
* Remove while loop and manage the breaking of thw while loops properly 

```python
class Solution:
    def maximumNumber(self, num: str, change: List[int]) -> str:
        num = list(num)  
        mutation_started = False  # Flag to track mutation start

        for i in range(len(num)):
            digit = int(num[i])

            if change[digit] > digit:  # Start mutation if change[digit] > digit
                num[i] = str(change[digit])
                mutation_started = True
            elif change[digit] < digit and mutation_started:  
                # Stop as soon as we see a decreasing transformation
                break


        return ''.join(num)  # Convert list back to string
```

