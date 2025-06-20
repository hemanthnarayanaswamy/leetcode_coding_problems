<h2><a href="https://leetcode.com/problems/calculate-amount-paid-in-taxes/?envType=problem-list-v2&envId=n9iuhemc">1382. Calculate Amount Paid in Taxes</a></h2><h3>Easy</h3><hr><p>You are given a <strong>0-indexed</strong> 2D integer array <code>brackets</code> where <code>brackets[i] = [upper<sub>i</sub>, percent<sub>i</sub>]</code> means that the <code>i<sup>th</sup></code> tax bracket has an upper bound of <code>upper<sub>i</sub></code> and is taxed at a rate of <code>percent<sub>i</sub></code>. The brackets are <strong>sorted</strong> by upper bound (i.e. <code>upper<sub>i-1</sub> &lt; upper<sub>i</sub></code> for <code>0 &lt; i &lt; brackets.length</code>).</p>

<p>Tax is calculated as follows:</p>

<ul>
	<li>The first <code>upper<sub>0</sub></code> dollars earned are taxed at a rate of <code>percent<sub>0</sub></code>.</li>
	<li>The next <code>upper<sub>1</sub> - upper<sub>0</sub></code> dollars earned are taxed at a rate of <code>percent<sub>1</sub></code>.</li>
	<li>The next <code>upper<sub>2</sub> - upper<sub>1</sub></code> dollars earned are taxed at a rate of <code>percent<sub>2</sub></code>.</li>
	<li>And so on.</li>
</ul>

<p>You are given an integer <code>income</code> representing the amount of money you earned. Return <em>the amount of money that you have to pay in taxes.</em> Answers within <code>10<sup>-5</sup></code> of the actual answer will be accepted.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> brackets = [[3,50],[7,10],[12,25]], income = 10
<strong>Output:</strong> 2.65000
<strong>Explanation:</strong>
Based on your income, you have 3 dollars in the 1<sup>st</sup> tax bracket, 4 dollars in the 2<sup>nd</sup> tax bracket, and 3 dollars in the 3<sup>rd</sup> tax bracket.
The tax rate for the three tax brackets is 50%, 10%, and 25%, respectively.
In total, you pay $3 * 50% + $4 * 10% + $3 * 25% = $2.65 in taxes.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> brackets = [[1,0],[4,25],[5,50]], income = 2
<strong>Output:</strong> 0.25000
<strong>Explanation:</strong>
Based on your income, you have 1 dollar in the 1<sup>st</sup> tax bracket and 1 dollar in the 2<sup>nd</sup> tax bracket.
The tax rate for the two tax brackets is 0% and 25%, respectively.
In total, you pay $1 * 0% + $1 * 25% = $0.25 in taxes.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> brackets = [[2,50]], income = 0
<strong>Output:</strong> 0.00000
<strong>Explanation:</strong>
You have no income to tax, so you have to pay a total of $0 in taxes.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= brackets.length &lt;= 100</code></li>
	<li><code>1 &lt;= upper<sub>i</sub> &lt;= 1000</code></li>
	<li><code>0 &lt;= percent<sub>i</sub> &lt;= 100</code></li>
	<li><code>0 &lt;= income &lt;= 1000</code></li>
	<li><code>upper<sub>i</sub></code> is sorted in ascending order.</li>
	<li>All the values of <code>upper<sub>i</sub></code> are <strong>unique</strong>.</li>
	<li>The upper bound of the last tax bracket is greater than or equal to <code>income</code>.</li>
</ul>

# Approach 
1. You are calculating tax on brackets.

2. At any point taxable income = min(income, income in the bracket) - tax income accumulated so far.

3. Calculate tax on taxable income (taxable income * percentage / 100) and add it to tax variable.

4. Add current taxable income to tax income accumulated.

5. Repeat process through all the brackets.

6. At all point make sure the income is more then the previous upper to continue calculating the taxes. 

# Solution 
```python
class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        tax  = 0.0
        prev = 0

        for upper, pct in brackets:
            if income <= prev:
                break

            # how much of your income falls in this bracket
            taxable = min(income, upper) - prev
            tax    += taxable * (pct / 100)
            prev    = upper

        return tax
```

# Optimal Solution
```python
class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        if not income: 
            return 0
        total = 0
        upper_prev = 0
        for upper, rate in brackets: 
            charge = min(upper - upper_prev, income)
            total += charge * rate / 100 
            income -= charge
            if not income: 
                break
            upper_prev = upper
        return total
```
