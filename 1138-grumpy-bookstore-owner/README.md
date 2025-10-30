<h2><a href="https://leetcode.com/problems/grumpy-bookstore-owner">1138. Grumpy Bookstore Owner</a></h2><h3>Medium</h3><hr><p>There is a bookstore owner that has a store open for <code>n</code> minutes. You are given an integer array <code>customers</code> of length <code>n</code> where <code>customers[i]</code> is the number of the customers that enter the store at the start of the <code>i<sup>th</sup></code> minute and all those customers leave after the end of that minute.</p>

<p>During certain minutes, the bookstore owner is grumpy. You are given a binary array grumpy where <code>grumpy[i]</code> is <code>1</code> if the bookstore owner is grumpy during the <code>i<sup>th</sup></code> minute, and is <code>0</code> otherwise.</p>

<p>When the bookstore owner is grumpy, the customers entering during that minute are not <strong>satisfied</strong>. Otherwise, they are satisfied.</p>

<p>The bookstore owner knows a secret technique to remain <strong>not grumpy</strong> for <code>minutes</code> consecutive minutes, but this technique can only be used <strong>once</strong>.</p>

<p>Return the <strong>maximum</strong> number of customers that can be <em>satisfied</em> throughout the day.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">customers = [1,0,1,2,1,1,7,5], grumpy = [0,1,0,1,0,1,0,1], minutes = 3</span></p>

<p><strong>Output:</strong> <span class="example-io">16</span></p>

<p><strong>Explanation:</strong></p>

<p>The bookstore owner keeps themselves not grumpy for the last 3 minutes.</p>

<p>The maximum number of customers that can be satisfied = 1 + 1 + 1 + 1 + 7 + 5 = 16.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">customers = [1], grumpy = [0], minutes = 1</span></p>

<p><strong>Output:</strong> <span class="example-io">1</span></p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == customers.length == grumpy.length</code></li>
	<li><code>1 &lt;= minutes &lt;= n &lt;= 2 * 10<sup>4</sup></code></li>
	<li><code>0 &lt;= customers[i] &lt;= 1000</code></li>
	<li><code>grumpy[i]</code> is either <code>0</code> or <code>1</code>.</li>
</ul>

# Approach 
* We need to find the maximum number of customers that can be satisfied. 
* **Number of Customers Satified = sum of customers at which owner is not Grumpy i.e `grumpy[i]=0`**.
* Now to make the above count maximum, We need to use `minutes` effectively. i.e But placing minutes consecutive at the place where the above sum becomes max. 

1. Compute Initial Satified customers. and other varible to track the maximum Satified Customers. 
2. Now for the `window Size = minutes`, compute a tmp satified customers, which is intial satified customers plus any new ones in the window where the owner was grumpy before. 
3. If this tmp is greater than the max satified customer, replace it and move to next window. 

# Brute Force Solution 
```python
class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        initialSatified = sum(c for c,g in zip(customers, grumpy) if not g)
        maxSatified = initialSatified
        
        for i in range(len(customers)-minutes+1):
            tmp = initialSatified
            for j in range(i, i + minutes):
                if grumpy[j]:
                    tmp += customers[j]
            
            if tmp > maxSatified:
                maxSatified = tmp
        
        return maxSatified
```
# Optimal Solution 
* Seperate the processes `Base = customers when owner not grumpy`. `Gain = extra customers you could satisfy by turning off grumpiness`.
* Create a `Potential Gain Array`, `gain[i] = customers[i] if grumpy[i] == 1, else 0`
```python
class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        gain = []
        initialSatified = 0
    
        for c,g in zip(customers, grumpy):
            if not g:
                initialSatified += c
                gain.append(0)
            else:
                gain.append(c)
        
        if minutes == 0:
            return initialSatified
        
        newSatified = sum(gain[:minutes]) +  initialSatified      
        maxSatified = newSatified
    
        for i in range(1, len(gain)-minutes+1):
            newSatified += gain[i+minutes-1] - gain[i-1]
            
            if newSatified > maxSatified:
                maxSatified = newSatified
        
        return maxSatified
```
---
```python
class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        n = len(customers)
        base = 0          # customers already satisfied when not grumpy
        win = 0           # current window gain
        best = 0          # best gain over any window of length minutes
        left = 0

        for right in range(n):
            if grumpy[right] == 0:
                base += customers[right]
            else:
                win += customers[right]

            if right - left + 1 > minutes:
                if grumpy[left] == 1:
                    win -= customers[left]
                left += 1

            if win > best:
                best = win

        return base + best
```
