<h2><a href="https://leetcode.com/problems/find-the-prefix-common-array-of-two-arrays">2766. Find the Prefix Common Array of Two Arrays</a></h2><h3>Medium</h3><hr><p>You are given two <strong>0-indexed </strong>integer<strong> </strong>permutations <code>A</code> and <code>B</code> of length <code>n</code>.</p>

<p>A <strong>prefix common array</strong> of <code>A</code> and <code>B</code> is an array <code>C</code> such that <code>C[i]</code> is equal to the count of numbers that are present at or before the index <code>i</code> in both <code>A</code> and <code>B</code>.</p>

<p>Return <em>the <strong>prefix common array</strong> of </em><code>A</code><em> and </em><code>B</code>.</p>

<p>A sequence of <code>n</code> integers is called a&nbsp;<strong>permutation</strong> if it contains all integers from <code>1</code> to <code>n</code> exactly once.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> A = [1,3,2,4], B = [3,1,2,4]
<strong>Output:</strong> [0,2,3,4]
<strong>Explanation:</strong> At i = 0: no number is common, so C[0] = 0.
At i = 1: 1 and 3 are common in A and B, so C[1] = 2.
At i = 2: 1, 2, and 3 are common in A and B, so C[2] = 3.
At i = 3: 1, 2, 3, and 4 are common in A and B, so C[3] = 4.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> A = [2,3,1], B = [3,1,2]
<strong>Output:</strong> [0,1,3]
<strong>Explanation:</strong> At i = 0: no number is common, so C[0] = 0.
At i = 1: only 3 is common in A and B, so C[1] = 1.
At i = 2: 1, 2, and 3 are common in A and B, so C[2] = 3.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= A.length == B.length == n &lt;= 50</code></li>
	<li><code>1 &lt;= A[i], B[i] &lt;= n</code></li>
	<li><code>It is guaranteed that A and B are both a permutation of n integers.</code></li>
</ul>

# Solution 
* It like a brute force solution you find the intersection between the `setA() & setB()` by adding elements till `A[i] & B[i]` and find the common elements at each index.

```python
class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        setA = set()
        setB = set()
        prefix = 0

        c = []

        for a, b in zip(A, B):
            setA.add(a)
            setB.add(b)

            prefix = len(setA & setB)
            
            c.append(prefix)
        
        return c
```
---
```python
class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        freq = defaultdict(int)
        prefix = 0
        C = []

        for a, b in zip(A, B):
            freq[a] += 1
            freq[b] += 1

            if a != b:
                if freq[a] == 2 and freq[b] == 2:
                    prefix += 2
                elif freq[a] == 2 or freq[b] == 2:
                    prefix += 1
            else:
                if freq[a] == 2:
                    prefix += 1
            
            C.append(prefix)

        return C
```
---
```python
class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        result = [0] * n
        count = [0] * (n + 1)
        common = 0
        
        for i in range(n):
            count[A[i]] += 1
            if count[A[i]] == 2:
                common += 1
            count[B[i]] += 1
            if count[B[i]] == 2:
                common += 1
            result[i] = common
        return result
```
