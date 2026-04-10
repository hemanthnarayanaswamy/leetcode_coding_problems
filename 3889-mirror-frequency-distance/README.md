<h2><a href="https://leetcode.com/problems/mirror-frequency-distance">4273. Mirror Frequency Distance</a></h2><h3>Medium</h3><hr><p>You are given a string <code>s</code> consisting of lowercase English letters and digits.</p>

<p>For each character, its <strong>mirror character</strong> is defined by reversing the order of its character set:</p>

<ul>
	<li>For letters, the mirror of a character is the letter at the same position from the end of the alphabet.
	<ul>
		<li>For example, the mirror of <code>&#39;a&#39;</code> is <code>&#39;z&#39;</code>, and the mirror of <code>&#39;b&#39;</code> is <code>&#39;y&#39;</code>, and so on.</li>
	</ul>
	</li>
	<li>For digits, the mirror of a character is the digit at the same position from the end of the range <code>&#39;0&#39;</code> to <code>&#39;9&#39;</code>.
	<ul>
		<li>For example, the mirror of <code>&#39;0&#39;</code> is <code>&#39;9&#39;</code>, and the mirror of <code>&#39;1&#39;</code> is <code>&#39;8&#39;</code>, and so on.</li>
	</ul>
	</li>
</ul>

<p>For each <strong>unique</strong> character <code>c</code> in the string:</p>

<ul>
	<li>Let <code>m</code> be its <strong>mirror</strong> character.</li>
	<li>Let <code>freq(x)</code> denote the number of times character <code>x</code> appears in the string.</li>
	<li>Compute the <strong>absolute difference</strong> between their <strong>frequencies</strong>, defined as: <code>|freq(c) - freq(m)|</code></li>
</ul>

<p>The mirror pairs <code>(c, m)</code> and <code>(m, c)</code> are the same and must be counted <strong>only once</strong>.</p>

<p>Return an integer denoting the total sum of these values over all such <strong>distinct mirror pairs</strong>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;ab1z9&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">3</span></p>

<p><strong>Explanation:</strong></p>

<p>For every mirror pair:</p>

<table style="border: 1px solid black;">
	<thead>
		<tr>
			<th style="border: 1px solid black;"><code>c</code></th>
			<th style="border: 1px solid black;"><code>m</code></th>
			<th style="border: 1px solid black;"><code>freq(c)</code></th>
			<th style="border: 1px solid black;"><code>freq(m)</code></th>
			<th style="border: 1px solid black;"><code>|freq(c) - freq(m)|</code></th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td style="border: 1px solid black;">a</td>
			<td style="border: 1px solid black;">z</td>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">0</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">b</td>
			<td style="border: 1px solid black;">y</td>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">0</td>
			<td style="border: 1px solid black;">1</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">8</td>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">0</td>
			<td style="border: 1px solid black;">1</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">9</td>
			<td style="border: 1px solid black;">0</td>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">0</td>
			<td style="border: 1px solid black;">1</td>
		</tr>
	</tbody>
</table>

<p>Thus, the answer is <code>0 + 1 + 1 + 1 = 3</code>.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;4m7n&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">2</span></p>

<p><strong>Explanation:</strong></p>

<table style="border: 1px solid black;">
	<thead>
		<tr>
			<th style="border: 1px solid black;"><code>c</code></th>
			<th style="border: 1px solid black;"><code>m</code></th>
			<th style="border: 1px solid black;"><code>freq(c)</code></th>
			<th style="border: 1px solid black;"><code>freq(m)</code></th>
			<th style="border: 1px solid black;"><code>|freq(c) - freq(m)|</code></th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td style="border: 1px solid black;">4</td>
			<td style="border: 1px solid black;">5</td>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">0</td>
			<td style="border: 1px solid black;">1</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">m</td>
			<td style="border: 1px solid black;">n</td>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">0</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">7</td>
			<td style="border: 1px solid black;">2</td>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">0</td>
			<td style="border: 1px solid black;">1</td>
		</tr>
	</tbody>
</table>

<p>Thus, the answer is <code>1 + 0 + 1 = 2</code>.​​​​​​​</p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;byby&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">0</span></p>

<p><strong>Explanation:</strong></p>

<table style="border: 1px solid black;">
	<thead>
		<tr>
			<th style="border: 1px solid black;"><code>c</code></th>
			<th style="border: 1px solid black;"><code>m</code></th>
			<th style="border: 1px solid black;"><code>freq(c)</code></th>
			<th style="border: 1px solid black;"><code>freq(m)</code></th>
			<th style="border: 1px solid black;"><code>|freq(c) - freq(m)|</code></th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td style="border: 1px solid black;">b</td>
			<td style="border: 1px solid black;">y</td>
			<td style="border: 1px solid black;">2</td>
			<td style="border: 1px solid black;">2</td>
			<td style="border: 1px solid black;">0</td>
		</tr>
	</tbody>
</table>

<p>Thus, the answer is 0.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 5 * 10<sup>5</sup></code></li>
	<li><code>s</code> consists only of lowercase English letters and digits.</li>
</ul>

# Solution 
* Mirroring lower case alphabets `chr(ord('z') - (ord('c') - ord('a')))`

1. We use different mirror computation logic for both letter and number. 
2. To store the mirror frequency we use `tuple` as key in `HashMaps` like `(character, mirror character) or (mirror character, character)` in a `sorted` order, That way only unique is preserved without worry about the duplicates. 


```python
class Solution:
    def mirrorFrequency(self, s: str) -> int:
        freq = Counter(s)
        mirrorFreq = defaultdict(int)

        for c in s:
            if c.isnumeric():
                mir = str(9 - int(c))
                f = abs(freq[mir] - freq[c])
                k = (c, mir) if c > mir else (mir, c)
                mirrorFreq[k] = f
            else:
                mir = chr(ord('z') - (ord(c) - ord('a')))
                f = abs(freq[mir] - freq[c])
                k = (c, mir) if c > mir else (mir, c)
                mirrorFreq[k] = f
        
        return sum(mirrorFreq.values())
```
* Do a running dynamic sum, instead of doing a reiteration at the end. 
---
```python
class Solution:
    def mirrorFrequency(self, s: str) -> int:
        freq = Counter(s)
        mirrorFreq = set()
        total = 0

        for c in freq:
            if c.isnumeric():
                mir = str(9 - int(c))
            else:
                mir = chr(ord('z') - (ord(c) - ord('a')))

            pair = (c, mir) if c > mir else (mir, c) # we generate character and mirror pair in sorted order

            if pair not in mirrorFreq: # If the pair is unique only find the absolute difference
                total += abs(freq[mir] - freq[c])
                mirrorFreq.add(pair) 
        
        return total # We need to return the sum of absolute difference of all unique pairs
```
*  Iterating over `s` causes unnecessary repeated work, So iterate thourh unique keys from `freq`
*  Don't need to store the `tuple pair` , you can store					
