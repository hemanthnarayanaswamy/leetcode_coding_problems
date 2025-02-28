<h2><a href="https://leetcode.com/problems/minimum-penalty-for-a-shop">2576. Minimum Penalty for a Shop</a></h2><h3>Medium</h3><hr><p>You are given the customer visit log of a shop represented by a <strong>0-indexed</strong> string <code>customers</code> consisting only of characters <code>&#39;N&#39;</code> and <code>&#39;Y&#39;</code>:</p>

<ul>
	<li>if the <code>i<sup>th</sup></code> character is <code>&#39;Y&#39;</code>, it means that customers come at the <code>i<sup>th</sup></code> hour</li>
	<li>whereas <code>&#39;N&#39;</code> indicates that no customers come at the <code>i<sup>th</sup></code> hour.</li>
</ul>

<p>If the shop closes at the <code>j<sup>th</sup></code> hour (<code>0 &lt;= j &lt;= n</code>), the <strong>penalty</strong> is calculated as follows:</p>

<ul>
	<li>For every hour when the shop is open and no customers come, the penalty increases by <code>1</code>.</li>
	<li>For every hour when the shop is closed and customers come, the penalty increases by <code>1</code>.</li>
</ul>

<p>Return<em> the <strong>earliest</strong> hour at which the shop must be closed to incur a <strong>minimum</strong> penalty.</em></p>

<p><strong>Note</strong> that if a shop closes at the <code>j<sup>th</sup></code> hour, it means the shop is closed at the hour <code>j</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> customers = &quot;YYNY&quot;
<strong>Output:</strong> 2
<strong>Explanation:</strong> 
- Closing the shop at the 0<sup>th</sup> hour incurs in 1+1+0+1 = 3 penalty.
- Closing the shop at the 1<sup>st</sup> hour incurs in 0+1+0+1 = 2 penalty.
- Closing the shop at the 2<sup>nd</sup> hour incurs in 0+0+0+1 = 1 penalty.
- Closing the shop at the 3<sup>rd</sup> hour incurs in 0+0+1+1 = 2 penalty.
- Closing the shop at the 4<sup>th</sup> hour incurs in 0+0+1+0 = 1 penalty.
Closing the shop at 2<sup>nd</sup> or 4<sup>th</sup> hour gives a minimum penalty. Since 2 is earlier, the optimal closing time is 2.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> customers = &quot;NNNNN&quot;
<strong>Output:</strong> 0
<strong>Explanation:</strong> It is best to close the shop at the 0<sup>th</sup> hour as no customers arrive.</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> customers = &quot;YYYY&quot;
<strong>Output:</strong> 4
<strong>Explanation:</strong> It is best to close the shop at the 4<sup>th</sup> hour as customers arrive at each hour.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= customers.length &lt;= 10<sup>5</sup></code></li>
	<li><code>customers</code> consists only of characters <code>&#39;Y&#39;</code> and <code>&#39;N&#39;</code>.</li>
</ul>

## Problem Statement 
* 'Y' (Yes, Customers Arrived):- If the shop is closed during this hour, penalty increases by 1.
* 'N' (No Customers Arrived):- If the shop is open during this hour, penalty increases by 1.
* The shop can be closed at any hour j (0 ≤ j ≤ n), meaning:
--> If j = 0, the shop is never open.
--> If j = n, the shop remains open for all hours.
* Return the earliest hour when the shop needs to be closed to incure the minimum cost. 

## Explanation of Code
1. Start with Initial Penalty (j = 0), The penalty starts as the number of 'Y' in customers, since all customers are affected if we close at j=0.
Iterate Over Possible Closing Times (j = 0 to n)
2. If the current penalty is the minimum found so far, update best_time.
3. Adjust the penalty dynamically:
 -->If customers[j] == 'Y' (closing when customers arrive) → Penalty decreases (-1).
 --> If customers[j] == 'N' (staying open without customers) → Penalty increases (+1).
Return the best_time where penalty is minimum.

```python
class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n = len(customers)
        
        min_penalty = float('inf')  # Store the minimum penalty found
        best_time = 0  # Store the best closing time
        penalty = customers.count('Y')  # Initial penalty if the shop closes at j = 0

        if "Y" not in customers:
            return 0
        if "N" not in customers:
            return n

        for j in range(n + 1):  # Check all possible closing times (0 to n) shop can close at n
            if penalty < min_penalty:
                min_penalty = penalty
                best_time = j  # Store the earliest minimum penalty closing hour
            
            if j < n:
                # If shop is open at 'N' (no customers), increase penalty
                # If shop is closed at 'Y' (customers inside), decrease penalty
                penalty += -1 if customers[j] == 'Y' else 1  
            
        return best_time
```


* Start with an initial penalty = count of 'Y' in customers
* This assumes the shop is closed immediately (j = 0)., Every 'Y' counts as penalty because we closed before any customers arrived.
* Iterate through all possible closing times (j = 0 to n)
* Keep track of the minimum penalty and the best closing hour. Adjust penalty dynamically while iterating:
--> If customers[j] == 'N', the shop was open with no customers, so penalty increases (+1).
--> If customers[j] == 'Y', the shop was open and we treat the customer, so penalty decreases (-1).
Store the closing time j that gives the lowest penalty.

```
1. WE assume the shop is closed and calculate the penality for closed
2. Now we try to close late one by one, during that time if it is N than +1 because its open that time and -1 if Y because initially through it closed but we are treating the customer
```
