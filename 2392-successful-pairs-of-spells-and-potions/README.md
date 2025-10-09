<h2><a href="https://leetcode.com/problems/successful-pairs-of-spells-and-potions">2392. Successful Pairs of Spells and Potions</a></h2><h3>Medium</h3><hr><p>You are given two positive integer arrays <code>spells</code> and <code>potions</code>, of length <code>n</code> and <code>m</code> respectively, where <code>spells[i]</code> represents the strength of the <code>i<sup>th</sup></code> spell and <code>potions[j]</code> represents the strength of the <code>j<sup>th</sup></code> potion.</p>

<p>You are also given an integer <code>success</code>. A spell and potion pair is considered <strong>successful</strong> if the <strong>product</strong> of their strengths is <strong>at least</strong> <code>success</code>.</p>

<p>Return <em>an integer array </em><code>pairs</code><em> of length </em><code>n</code><em> where </em><code>pairs[i]</code><em> is the number of <strong>potions</strong> that will form a successful pair with the </em><code>i<sup>th</sup></code><em> spell.</em></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> spells = [5,1,3], potions = [1,2,3,4,5], success = 7
<strong>Output:</strong> [4,0,3]
<strong>Explanation:</strong>
- 0<sup>th</sup> spell: 5 * [1,2,3,4,5] = [5,<u><strong>10</strong></u>,<u><strong>15</strong></u>,<u><strong>20</strong></u>,<u><strong>25</strong></u>]. 4 pairs are successful.
- 1<sup>st</sup> spell: 1 * [1,2,3,4,5] = [1,2,3,4,5]. 0 pairs are successful.
- 2<sup>nd</sup> spell: 3 * [1,2,3,4,5] = [3,6,<u><strong>9</strong></u>,<u><strong>12</strong></u>,<u><strong>15</strong></u>]. 3 pairs are successful.
Thus, [4,0,3] is returned.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> spells = [3,1,2], potions = [8,5,8], success = 16
<strong>Output:</strong> [2,0,2]
<strong>Explanation:</strong>
- 0<sup>th</sup> spell: 3 * [8,5,8] = [<u><strong>24</strong></u>,15,<u><strong>24</strong></u>]. 2 pairs are successful.
- 1<sup>st</sup> spell: 1 * [8,5,8] = [8,5,8]. 0 pairs are successful. 
- 2<sup>nd</sup> spell: 2 * [8,5,8] = [<strong><u>16</u></strong>,10,<u><strong>16</strong></u>]. 2 pairs are successful. 
Thus, [2,0,2] is returned.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == spells.length</code></li>
	<li><code>m == potions.length</code></li>
	<li><code>1 &lt;= n, m &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= spells[i], potions[i] &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= success &lt;= 10<sup>10</sup></code></li>
</ul>

# Brute Force Solution 
```python
class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        result = []
        potions.sort(reverse=True)

        for i in range(len(spells)):
            count = 0
            for j in range(len(potions)):
                if spells[i] * potions[j] >= success:
                    count += 1
                else:
                    break
            result.append(count)

        return result
```
---
```python
class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
            n = len(potions)
            ns = len(spells)
            result = [0] * ns
            potions.sort()
            
            def SearchIdx(spell):
                l = 0
                r = n - 1
                while l < r:
                    m = (l + r) // 2
                    if potions[m] * spell >= success:
                        r = m - 1
                    else:
                        l = m + 1
                
                if r >= 0:
                    if potions[r] * spell >= success:
                        return n - r
                    else:
                        return n - r - 1

                return n
            
            for i in range(ns):
                result[i] = SearchIdx(spells[i])

            return result
```

# Approach
* Sort the potions array to allow efficient binary search.
* For each spell, Use binary search to find the first potion such that `spell[i] * potions[mid] ≥ success.`
* All potions to the right of that index will also satisfy the condition.
* Therefore, the count of `successful pairs = total_potions - found_index`.
* Store these counts in the answer array and return it.

```python
class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        n = len(potions)

        def countFor(spell):
            l, r = 0, n
            while l < r:
                m = (l+r)//2
                if potions[m] * spell >= success:
                    r = m
                else:
                    l = m + 1
            
            return n - l
        
        return [countFor(spell) for spell in spells]
```

# Complexity
### Time Complexity:
* Sorting potions: `O(m log m)`
* Binary search for each spell: `O(n log m)`
* **Total: `O(m log m + n log m)`**

### Space Complexity:
* O(1) (excluding the output array) — since sorting is in-place and we use only a few extra variables.
