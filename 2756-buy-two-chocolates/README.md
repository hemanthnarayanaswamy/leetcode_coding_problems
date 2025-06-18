<h2><a href="https://leetcode.com/problems/buy-two-chocolates">2756. Buy Two Chocolates</a></h2><h3>Easy</h3><hr><p>You are given an integer array <code>prices</code> representing the prices of various chocolates in a store. You are also given a single integer <code>money</code>, which represents your initial amount of money.</p>

<p>You must buy <strong>exactly</strong> two chocolates in such a way that you still have some <strong>non-negative</strong> leftover money. You would like to minimize the sum of the prices of the two chocolates you buy.</p>

<p>Return <em>the amount of money you will have leftover after buying the two chocolates</em>. If there is no way for you to buy two chocolates without ending up in debt, return <code>money</code>. Note that the leftover must be non-negative.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> prices = [1,2,2], money = 3
<strong>Output:</strong> 0
<strong>Explanation:</strong> Purchase the chocolates priced at 1 and 2 units respectively. You will have 3 - 3 = 0 units of money afterwards. Thus, we return 0.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> prices = [3,2,3], money = 3
<strong>Output:</strong> 3
<strong>Explanation:</strong> You cannot buy 2 chocolates without going in debt, so we return 3.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= prices.length &lt;= 50</code></li>
	<li><code>1 &lt;= prices[i] &lt;= 100</code></li>
	<li><code>1 &lt;= money &lt;= 100</code></li>
</ul>

# Solution 
* The best way is to sort the array and compute the sum of first two low price chocolates and check if the combined price exceed the money we have and return the results based on that 

```python
# Solution without using the Sorting 
class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        first = second = float('inf')
        for p in prices:
            if p < first:
                second, first = first, p
            elif p < second:
                second = p

        cost = first + second
        return money - cost if cost <= money else money
```

# Improved Solution 
```python
# Solution with sorting 
class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()
        
        choPrice = prices[0] + prices[1]
        
        return money if choPrice > money else money - choPrice
```

# Optimal Solution 
```python
class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        first = second = float('inf')
        for i in range(len(prices)):
            if prices[i] < first:
                second, first = first, prices[i] 
            elif prices[i]  < second:
                second = prices[i] 

        if money >= first + second:
            return money - first - second
        else:
            return money
```
