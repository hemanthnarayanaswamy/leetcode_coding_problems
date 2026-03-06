<h2><a href="https://leetcode.com/problems/1-bit-and-2-bit-characters">717. 1-bit and 2-bit Characters</a></h2><h3>Easy</h3><hr><p>We have two special characters:</p>

<ul>
	<li>The first character can be represented by one bit <code>0</code>.</li>
	<li>The second character can be represented by two bits (<code>10</code> or <code>11</code>).</li>
</ul>

<p>Given a binary array <code>bits</code> that ends with <code>0</code>, return <code>true</code> if the last character must be a one-bit character.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> bits = [1,0,0]
<strong>Output:</strong> true
<strong>Explanation:</strong> The only way to decode it is two-bit character and one-bit character.
So the last character is one-bit character.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> bits = [1,1,1,0]
<strong>Output:</strong> false
<strong>Explanation:</strong> The only way to decode it is two-bit character and two-bit character.
So the last character is not one-bit character.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= bits.length &lt;= 1000</code></li>
	<li><code>bits[i]</code> is either <code>0</code> or <code>1</code>.</li>
</ul>

We use three bit-representations to represent three characters : 0, 10, 11 (the corresponding characters don't matter)
So bits representation 1, 01 are not valid.
**Given an array of bits ending with 0**, 
- find out if it's only valid to translate the last 0 into the 0 bit representation (means it's not valid when the last 0 is translated into the 10 bits representation)

# Brute Force Solution 
* We use stack, and and we `pop()` stack everytime and only append, only when `stack[-1] = = 0` and at the  end we check if the length of stack is `one`

```python
class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        stack = []

        for i in range(len(bits)):
            if stack:
                if stack[-1]:
                    stack.pop()
                else:
                    stack.pop()
                    stack.append(bits[i])
            else:
                stack.append(bits[i])
        
        return len(stack) == 1
```
---
```python
class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        stack = []

        for i in range(len(bits)):
            if stack:
                bit = stack.pop()
                if bit == 0:
                    stack.append(bits[i])
            else:
                stack.append(bits[i])
        
        return len(stack) == 1
```
---
```python
class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        i = 0
        while i < len(bits):
            if bits[i] == 0:
                i += 1
                res = True
            else:
                i += 2
                res = False
        return res
```
