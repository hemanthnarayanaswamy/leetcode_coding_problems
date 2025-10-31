<h2><a href="https://leetcode.com/problems/complex-number-multiplication">537. Complex Number Multiplication</a></h2><h3>Medium</h3><hr><p>A <a href="https://en.wikipedia.org/wiki/Complex_number" target="_blank">complex number</a> can be represented as a string on the form <code>&quot;<strong>real</strong>+<strong>imaginary</strong>i&quot;</code> where:</p>

<ul>
	<li><code>real</code> is the real part and is an integer in the range <code>[-100, 100]</code>.</li>
	<li><code>imaginary</code> is the imaginary part and is an integer in the range <code>[-100, 100]</code>.</li>
	<li><code>i<sup>2</sup> == -1</code>.</li>
</ul>

<p>Given two complex numbers <code>num1</code> and <code>num2</code> as strings, return <em>a string of the complex number that represents their multiplications</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> num1 = &quot;1+1i&quot;, num2 = &quot;1+1i&quot;
<strong>Output:</strong> &quot;0+2i&quot;
<strong>Explanation:</strong> (1 + i) * (1 + i) = 1 + i2 + 2 * i = 2i, and you need convert it to the form of 0+2i.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> num1 = &quot;1+-1i&quot;, num2 = &quot;1+-1i&quot;
<strong>Output:</strong> &quot;0+-2i&quot;
<strong>Explanation:</strong> (1 - i) * (1 - i) = 1 + i2 - 2 * i = -2i, and you need convert it to the form of 0+-2i.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>num1</code> and <code>num2</code> are valid complex numbers.</li>
</ul>

# Approach 
* The product of two complex numbers is computed as follows:
![](https://wikimedia.org/api/rest_v1/media/math/render/svg/4f6f9b21903da13a2ad8a091b391b8ef0d279e0b)

![](https://wikimedia.org/api/rest_v1/media/math/render/svg/65be647ba3d494fb73c129d8412ea4ba36872c9c)

NOTE: **"1+-1i" means 1 + (-1)i** `a = 1, b = -1`

```python
class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        a = b = c = d = 0
    
        i = num1.index('+')
        j = num2.index('+')
        
        a = int(num1[:i])
        b = int(num1[i+1:-1]) # Ignore the i
        c = int(num2[:j])
        d = int(num2[j+1:-1])

        return str(a*c - b*d) + '+' + str(a*d + b*c) + 'i'
```
---
```python
class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        r1,i1 = map(int, num1[:-1].split('+'))
        r2,i2 = map(int, num2[:-1].split('+'))
        
        return str(r1*r2 - i1*i2) + "+" + str(r1*i2 + r2*i1) + 'i' 
```
