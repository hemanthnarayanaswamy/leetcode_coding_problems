<h2><a href="https://leetcode.com/problems/number-of-laser-beams-in-a-bank/?envType=problem-list-v2&envId=nudotrev">2244. Number of Laser Beams in a Bank</a></h2><h3>Medium</h3><hr><p>Anti-theft security devices are activated inside a bank. You are given a <strong>0-indexed</strong> binary string array <code>bank</code> representing the floor plan of the bank, which is an <code>m x n</code> 2D matrix. <code>bank[i]</code> represents the <code>i<sup>th</sup></code> row, consisting of <code>&#39;0&#39;</code>s and <code>&#39;1&#39;</code>s. <code>&#39;0&#39;</code> means the cell is empty, while<code>&#39;1&#39;</code> means the cell has a security device.</p>

<p>There is <strong>one</strong> laser beam between any <strong>two</strong> security devices <strong>if both</strong> conditions are met:</p>

<ul>
	<li>The two devices are located on two <strong>different rows</strong>: <code>r<sub>1</sub></code> and <code>r<sub>2</sub></code>, where <code>r<sub>1</sub> &lt; r<sub>2</sub></code>.</li>
	<li>For <strong>each</strong> row <code>i</code> where <code>r<sub>1</sub> &lt; i &lt; r<sub>2</sub></code>, there are <strong>no security devices</strong> in the <code>i<sup>th</sup></code> row.</li>
</ul>

<p>Laser beams are independent, i.e., one beam does not interfere nor join with another.</p>

<p>Return <em>the total number of laser beams in the bank</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/12/24/laser1.jpg" style="width: 400px; height: 368px;" />
<pre>
<strong>Input:</strong> bank = [&quot;011001&quot;,&quot;000000&quot;,&quot;010100&quot;,&quot;001000&quot;]
<strong>Output:</strong> 8
<strong>Explanation:</strong> Between each of the following device pairs, there is one beam. In total, there are 8 beams:
 * bank[0][1] -- bank[2][1]
 * bank[0][1] -- bank[2][3]
 * bank[0][2] -- bank[2][1]
 * bank[0][2] -- bank[2][3]
 * bank[0][5] -- bank[2][1]
 * bank[0][5] -- bank[2][3]
 * bank[2][1] -- bank[3][2]
 * bank[2][3] -- bank[3][2]
Note that there is no beam between any device on the 0<sup>th</sup> row with any on the 3<sup>rd</sup> row.
This is because the 2<sup>nd</sup> row contains security devices, which breaks the second condition.
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/12/24/laser2.jpg" style="width: 244px; height: 325px;" />
<pre>
<strong>Input:</strong> bank = [&quot;000&quot;,&quot;111&quot;,&quot;000&quot;]
<strong>Output:</strong> 0
<strong>Explanation:</strong> There does not exist two devices located on two different rows.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>m == bank.length</code></li>
	<li><code>n == bank[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 500</code></li>
	<li><code>bank[i][j]</code> is either <code>&#39;0&#39;</code> or <code>&#39;1&#39;</code>.</li>
</ul>

# Approach 
* Each device on the same row has the same number of beams pointing towards the devices on the next row with devices.
* Convert the input to such an array, skip any row with no security device, then find the sum of the product between adjacent elements.
```ini 
Convert to array : {3,0,2,1}.
Ignore the 0's in the array so the array is [3,2,1] : 
Answer is `3*2 + 2*1` as simple.
```

# Solution 
```python
class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        numberDev = []
        lasers = 0

        for r in bank: # Create a Interger Array of number of devices per row ignoring zeros
            d = r.count('1')
            if d:
                numberDev.append(d)
        
        for i in range(len(numberDev)-1):
            lasers += numberDev[i] * numberDev[i+1]
        
        return lasers
```

# Improved Solution 
```python
class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        lasers = 0
        x = bank[0].count('1')

        for i in range(1, len(bank)): 
            y = bank[i].count('1')
            if y:
                lasers += x * bank[i].count('1')
                x = y
        
        return lasers
```
---
```python
class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        ans = prev = 0
        for s in bank:
            c = s.count('1')
            if c:
                ans += prev * c
                prev = c
        return ans
```
