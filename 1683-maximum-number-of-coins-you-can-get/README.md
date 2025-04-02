<h2><a href="https://leetcode.com/problems/maximum-number-of-coins-you-can-get">1683. Maximum Number of Coins You Can Get</a></h2><h3>Medium</h3><hr><p>There are <code>3n</code> piles of coins of varying size, you and your friends will take piles of coins as follows:</p>

<ul>
	<li>In each step, you will choose <strong>any </strong><code>3</code> piles of coins (not necessarily consecutive).</li>
	<li>Of your choice, Alice will pick the pile with the maximum number of coins.</li>
	<li>You will pick the next pile with the maximum number of coins.</li>
	<li>Your friend Bob will pick the last pile.</li>
	<li>Repeat until there are no more piles of coins.</li>
</ul>

<p>Given an array of integers <code>piles</code> where <code>piles[i]</code> is the number of coins in the <code>i<sup>th</sup></code> pile.</p>

<p>Return the maximum number of coins that you can have.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> piles = [2,4,1,2,7,8]
<strong>Output:</strong> 9
<strong>Explanation: </strong>Choose the triplet (2, 7, 8), Alice Pick the pile with 8 coins, you the pile with <strong>7</strong> coins and Bob the last one.
Choose the triplet (1, 2, 4), Alice Pick the pile with 4 coins, you the pile with <strong>2</strong> coins and Bob the last one.
The maximum number of coins which you can have are: 7 + 2 = 9.
On the other hand if we choose this arrangement (1, <strong>2</strong>, 8), (2, <strong>4</strong>, 7) you only get 2 + 4 = 6 coins which is not optimal.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> piles = [2,4,5]
<strong>Output:</strong> 4
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> piles = [9,8,7,6,5,1,2,3,4]
<strong>Output:</strong> 18
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>3 &lt;= piles.length &lt;= 10<sup>5</sup></code></li>
	<li><code>piles.length % 3 == 0</code></li>
	<li><code>1 &lt;= piles[i] &lt;= 10<sup>4</sup></code></li>
</ul>

## Solution Approach 
* You are always picking the second max from the set of three always 
* Your files will pick the 3rd by default 
* You job is to choose the set of 3 piles with 2 are max and 1 min.
* I that logic your are picking n times ` n= len(piles) //3 ` the  second max number , which is are index `i = 1, 3, 5, 7, 9 .........`
```python 
class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True)

        my_coins = 0
        n = len(piles) // 3

        for i in range(1,3*n, 2):
            my_coins += piles[i]
            n -= 1
            if n == 0:
                break 
        
        return my_coins
```

## Improved Solution

```python
class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        coinCount = 0
        n = len(piles)
        
        for _ in range(n//3):
            n -=2
            coinCount += piles[n]

        return coinCount
```
