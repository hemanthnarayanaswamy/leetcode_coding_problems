<h2><a href="https://leetcode.com/problems/x-of-a-kind-in-a-deck-of-cards">950. X of a Kind in a Deck of Cards</a></h2><h3>Easy</h3><hr><p>You are given an integer array <code>deck</code> where <code>deck[i]</code> represents the number written on the <code>i<sup>th</sup></code> card.</p>

<p>Partition the cards into <strong>one or more groups</strong> such that:</p>

<ul>
	<li>Each group has <strong>exactly</strong> <code>x</code> cards where <code>x &gt; 1</code>, and</li>
	<li>All the cards in one group have the same integer written on them.</li>
</ul>

<p>Return <code>true</code><em> if such partition is possible, or </em><code>false</code><em> otherwise</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> deck = [1,2,3,4,4,3,2,1]
<strong>Output:</strong> true
<strong>Explanation</strong>: Possible partition [1,1],[2,2],[3,3],[4,4].
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> deck = [1,1,1,2,2,2,3,3]
<strong>Output:</strong> false
<strong>Explanation</strong>: No possible partition.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= deck.length &lt;= 10<sup>4</sup></code></li>
	<li><code>0 &lt;= deck[i] &lt; 10<sup>4</sup></code></li>
</ul>

# Solution 
* We need to find the greatest Common divisor for all the values in the hashMap of the Deck and that should be greater then 1.
* say there are C_i cards of number i. These must be broken down into piles of X cards each, ie. C_i % X == 0 for all i.
` Thus, X must divide the greatest common divisor of C_i. If this greatest common divisor g is greater than 1, then X = g will satisfy. Otherwise, it won't.

```python
import math 

class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        if len(deck) == 1:
            return False
        
        cardCounts = [v for v in Counter(deck).values()]

        Xgcd = math.gcd(*cardCounts)

        return Xgcd != 1
```
---
* To use the `math.gcd`, it doesn't automatically compute gcd automatically for the list 

```ini
**Reduce** is a function in "functools" module which is used to perform a particular function to all of the elements in the list. Here reduce() computes the GCD of the complete list A by computing GCD of first two elements, then the GCD of 3rd element with previously computed GCD of first two elements and so on
```

```python
class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        rec = defaultdict(int)
        for x in deck:
            rec[x]+=1
        if(reduce(math.gcd, rec.values())==1): # reduce(math.gcd, rec.values())
            return False
        
        return True
```

## Compute the GCD code 
```python
from functools import reduce
from math import gcd

def gcd_of_list(numbers):
  """Calculates the greatest common divisor of a list of numbers."""
  return reduce(gcd, numbers)

# Example usage
numbers = [24, 36, 60, 102]
result = gcd_of_list(numbers)
print(f"The GCD of {numbers} is {result}")
```
