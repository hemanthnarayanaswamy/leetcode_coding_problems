<h2><a href="https://leetcode.com/problems/string-compression">443. String Compression</a></h2><h3>Medium</h3><hr><p>Given an array of characters <code>chars</code>, compress it using the following algorithm:</p>

<p>Begin with an empty string <code>s</code>. For each group of <strong>consecutive repeating characters</strong> in <code>chars</code>:</p>

<ul>
	<li>If the group&#39;s length is <code>1</code>, append the character to <code>s</code>.</li>
	<li>Otherwise, append the character followed by the group&#39;s length.</li>
</ul>

<p>The compressed string <code>s</code> <strong>should not be returned separately</strong>, but instead, be stored <strong>in the input character array <code>chars</code></strong>. Note that group lengths that are <code>10</code> or longer will be split into multiple characters in <code>chars</code>.</p>

<p>After you are done <strong>modifying the input array,</strong> return <em>the new length of the array</em>.</p>

<p>You must write an algorithm that uses only constant extra space.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> chars = [&quot;a&quot;,&quot;a&quot;,&quot;b&quot;,&quot;b&quot;,&quot;c&quot;,&quot;c&quot;,&quot;c&quot;]
<strong>Output:</strong> Return 6, and the first 6 characters of the input array should be: [&quot;a&quot;,&quot;2&quot;,&quot;b&quot;,&quot;2&quot;,&quot;c&quot;,&quot;3&quot;]
<strong>Explanation:</strong> The groups are &quot;aa&quot;, &quot;bb&quot;, and &quot;ccc&quot;. This compresses to &quot;a2b2c3&quot;.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> chars = [&quot;a&quot;]
<strong>Output:</strong> Return 1, and the first character of the input array should be: [&quot;a&quot;]
<strong>Explanation:</strong> The only group is &quot;a&quot;, which remains uncompressed since it&#39;s a single character.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> chars = [&quot;a&quot;,&quot;b&quot;,&quot;b&quot;,&quot;b&quot;,&quot;b&quot;,&quot;b&quot;,&quot;b&quot;,&quot;b&quot;,&quot;b&quot;,&quot;b&quot;,&quot;b&quot;,&quot;b&quot;,&quot;b&quot;]
<strong>Output:</strong> Return 4, and the first 4 characters of the input array should be: [&quot;a&quot;,&quot;b&quot;,&quot;1&quot;,&quot;2&quot;].
<strong>Explanation:</strong> The groups are &quot;a&quot; and &quot;bbbbbbbbbbbb&quot;. This compresses to &quot;ab12&quot;.</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= chars.length &lt;= 2000</code></li>
	<li><code>chars[i]</code> is a lowercase English letter, uppercase English letter, digit, or symbol.</li>
</ul>

# Solution 
```python
class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        if n == 1:
            return 1

        count = 1
        newChars = []

        for i in range(1, n):
            if chars[i] == chars[i-1]:
                count += 1
            else:
                if count > 1:
                    newChars.append(chars[i-1])
                    newChars.extend(list(str(count)))
                    count = 1
                else:
                    newChars.append(chars[i-1])
            
        newChars.append(chars[i])

        if count > 1:
            newChars.extend(list(str(count)))

        chars[:n] = newChars

        return len(chars)
```
* If previous char is not equal to current char, then append that char and the count if greater then 1. 
* After the loop manage the last char if and its count 
* And to pass the test instead of re initialize `char = newChars` use this logic instead `char[:len(chars)] = newChars` this way its not reinitialized. 

# Optimal Solution 
```python
def compress(chars):
    write = 0  # Where to write in the array
    read = 0   # Where we're reading from
    
    while read < len(chars):
        # Step 1: Get current character
        current_char = chars[read]
        count = 0
        
        # Step 2: Count how many times it repeats
        while read < len(chars) and chars[read] == current_char:
            count += 1
            read += 1
        
        # Step 3: Write the character
        chars[write] = current_char
        write += 1
        
        # Step 4: If more than 1, write the count
        if count > 1:
            for digit in str(count):
                chars[write] = digit
                write += 1
    
    return write
```
```ini
Step 1: read=0, write=0
- current_char = 'a'
- Count 'a': read moves 0→1→2, count=2
- Write: chars[0] = 'a', write=1
- count > 1, so write '2': chars[1] = '2', write=2

Step 2: read=2, write=2  
- current_char = 'b'
- Count 'b': read moves 2→3→4, count=2
- Write: chars[2] = 'b', write=3
- count > 1, so write '2': chars[3] = '2', write=4

Step 3: read=4, write=4
- current_char = 'c' 
- Count 'c': read moves 4→5→6→7, count=3
- Write: chars[4] = 'c', write=5
- count > 1, so write '3': chars[5] = '3', write=6

Final: chars = ["a","2","b","2","c","3","c"], return 6
```

1. Problem Only Cares About the Length: The function returns 6, which tells us only the first 6 elements matter.

2. LeetCode Tests Only Check First n Elements: When you return 6, LeetCode only validates chars[0:6].

3. Real-world Usage: The calling code would only use chars[0:returned_length].
