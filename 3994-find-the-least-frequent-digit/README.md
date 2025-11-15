<h2><a href="https://leetcode.com/problems/find-the-least-frequent-digit">3994. Find The Least Frequent Digit</a></h2><h3>Easy</h3><hr><p>Given an integer <code>n</code>, find the digit that occurs <strong>least</strong> frequently in its decimal representation. If multiple digits have the same frequency, choose the <strong>smallest</strong> digit.</p>

<p>Return the chosen digit as an integer.</p>
The <strong>frequency</strong> of a digit <code>x</code> is the number of times it appears in the decimal representation of <code>n</code>.
<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">n = 1553322</span></p>

<p><strong>Output:</strong> 1</p>

<p><strong>Explanation:</strong></p>

<p>The least frequent digit in <code>n</code> is 1, which appears only once. All other digits appear twice.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">n = 723344511</span></p>

<p><strong>Output:</strong> 2</p>

<p><strong>Explanation:</strong></p>

<p>The least frequent digits in <code>n</code> are 7, 2, and 5; each appears only once.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 2<sup>31</sup>​​​​​​​ - 1</code></li>
</ul>

# Solution 
```python
class Solution:
    def getLeastFrequentDigit(self, n: int) -> int:
        n = str(n)
        nFreq = Counter(n)
        minFreq = len(n)

        for f in nFreq.values():
            if f < minFreq:
                minFreq = f

        ans = []
        for num,f in nFreq.items():
            if f == minFreq:
                ans.append(int(num))
        
        return min(ans)
```
* The above solution can be improved to have a single iteration. 

# Optimal Solution 
```python
class Solution:
    def getLeastFrequentDigit(self, n: int) -> int:
        n = str(n)
        nFreq = Counter(n)
        minFreq = len(n) # worst freq can be the whole lenght being the same number
        answer = inf # Assign infinity number

        for num, f in nFreq.items():
            num = int(num)
            if f < minFreq:
                minFreq = f
                answer = num
            elif f == minFreq:
                if num < answer:
                    answer = num
        
        return answer
```
