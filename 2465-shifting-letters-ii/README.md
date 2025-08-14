<h2><a href="https://leetcode.com/problems/shifting-letters-ii">2465. Shifting Letters II</a></h2><h3>Medium</h3><hr><p>You are given a string <code>s</code> of lowercase English letters and a 2D integer array <code>shifts</code> where <code>shifts[i] = [start<sub>i</sub>, end<sub>i</sub>, direction<sub>i</sub>]</code>. For every <code>i</code>, <strong>shift</strong> the characters in <code>s</code> from the index <code>start<sub>i</sub></code> to the index <code>end<sub>i</sub></code> (<strong>inclusive</strong>) forward if <code>direction<sub>i</sub> = 1</code>, or shift the characters backward if <code>direction<sub>i</sub> = 0</code>.</p>

<p>Shifting a character <strong>forward</strong> means replacing it with the <strong>next</strong> letter in the alphabet (wrapping around so that <code>&#39;z&#39;</code> becomes <code>&#39;a&#39;</code>). Similarly, shifting a character <strong>backward</strong> means replacing it with the <strong>previous</strong> letter in the alphabet (wrapping around so that <code>&#39;a&#39;</code> becomes <code>&#39;z&#39;</code>).</p>

<p>Return <em>the final string after all such shifts to </em><code>s</code><em> are applied</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;abc&quot;, shifts = [[0,1,0],[1,2,1],[0,2,1]]
<strong>Output:</strong> &quot;ace&quot;
<strong>Explanation:</strong> Firstly, shift the characters from index 0 to index 1 backward. Now s = &quot;zac&quot;.
Secondly, shift the characters from index 1 to index 2 forward. Now s = &quot;zbd&quot;.
Finally, shift the characters from index 0 to index 2 forward. Now s = &quot;ace&quot;.</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;dztz&quot;, shifts = [[0,0,0],[1,1,1]]
<strong>Output:</strong> &quot;catz&quot;
<strong>Explanation:</strong> Firstly, shift the characters from index 0 to index 0 backward. Now s = &quot;cztz&quot;.
Finally, shift the characters from index 1 to index 1 forward. Now s = &quot;catz&quot;.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length, shifts.length &lt;= 5 * 10<sup>4</sup></code></li>
	<li><code>shifts[i].length == 3</code></li>
	<li><code>0 &lt;= start<sub>i</sub> &lt;= end<sub>i</sub> &lt; s.length</code></li>
	<li><code>0 &lt;= direction<sub>i</sub> &lt;= 1</code></li>
	<li><code>s</code> consists of lowercase English letters.</li>
</ul>

# Solution 
* I came up with the solution, but it exceeds the time Limit (TLE). 

```python
class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        char2val = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25}
        val2char = {-1: 'z', 0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h', 8: 'i', 9: 'j', 10: 'k', 11: 'l', 12: 'm', 13: 'n', 14: 'o', 15: 'p', 16: 'q', 17: 'r', 18: 's', 19: 't', 20: 'u', 21: 'v', 22: 'w', 23: 'x', 24: 'y', 25: 'z'}
        s = list(s)

        for start, end, direction in shifts:
            for i in range(start, end+1):
                if direction:
                    tmp = (char2val[s[i]] + 1) % 26
                    s[i] = val2char[tmp]
                else:
                    tmp = (char2val[s[i]] - 1)
                    s[i] = val2char[tmp]

        return ''.join(s)
```

* A direct implementation would involve iterating over each range [start, end] for every shift operation and updating the characters in that range individually.
* Since applying each shift involves iterating over a substring of s, and this approach has a quadratic time complexity which is inefficient for the problem's constraints.

# Optimal Solution 
* Instead of applying each shift directly, we can optimize by focusing on the net effect of all shifts on each character. This means that rather than updating the string multiple times for each operation, we calculate how many total shifts each character undergoes. Once the total shifts numberOfShifts for each character have been calculated, we can use the following formula to create the final string in one pass:

```ini
newChar=’a’+(oldChar−’a’+numberOfShifts) mod 26.

* oldChar−’a’: Converts the character to a 0-based index in the range [0, 25] (e.g., 'a' = 0, 'b' = 1, ..., 'z' = 25).
* numberOfShifts: Applies the total shifts to the character.
* mod 26: Ensures the result wraps around the alphabet if necessary (e.g., shifting 'z' forward yields 'a').
* ’a’+... : Converts the 0-based index back to a character.
```

```python
class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        diff = [0] * (n + 1)  # Difference array
        
        # Step 1: Process all shifts in O(m) time
        for start, end, direction in shifts:
            shift_val = 1 if direction == 1 else -1
            diff[start] += shift_val
            diff[end + 1] -= shift_val
        
        # Step 2: Convert to actual shift values in O(n) time
        actual_shifts = [0] * n
        actual_shifts[0] = diff[0]
        for i in range(1, n):
            actual_shifts[i] = actual_shifts[i-1] + diff[i]
        
        # Step 3: Apply shifts to characters in O(n) time
        result = []
        for i in range(n):
            shifted_val = (ord(s[i]) - ord('a') + actual_shifts[i]) % 26
            result.append(chr(shifted_val + ord('a')))
        
        return ''.join(result)
```

1.  Difference Array Technique Explained 
* Instead of updating each element in a range individually, mark the start and end of changes, then apply all changes at once.

```ini
Build Difference Array 

# For each shift [start, end, direction]:
diff[start] += shift_value     # "Start adding shift_value from here"
diff[end + 1] -= shift_value   # "Stop adding shift_value after end"
```
2. Convert to Actual Values (Prefix Sum)
```ini 
# actual_shifts[i] = sum of all diff[0] to diff[i]
for i in range(1, n):
    actual_shifts[i] = actual_shifts[i-1] + diff[i]
```

```ini 
# Forward shift: 'z' + 1 = 'a' (wrapping)
shifted_val = (ord(char) - ord('a') + shift) % 26
new_char = chr(shifted_val + ord('a'))

# Backward shift: 'a' - 1 = 'z' (wrapping)  
shifted_val = (ord(char) - ord('a') + shift) % 26  # shift can be negative
new_char = chr(shifted_val + ord('a'))
```

### **2. Why Extra Element in Diff Array**
```python
diff = [0] * (n + 1)  # n+1 size!

# When end = n-1 (last position), we do:
diff[end + 1] -= shift_val  # This would be diff[n]
# Without extra element, this would cause index error!
```

### **3. Handling Negative Shifts**
```python
# Python's modulo handles negative numbers correctly:
(-1) % 26 = 25  # Perfect for 'a' - 1 = 'z'
(-27) % 26 = 25 # Works for large backward shifts too
```

---

## **🚫 Common Mistakes**

### **1. Forgetting Extra Element in Diff Array**
```python
diff = [0] * n  # ❌ Wrong size
diff = [0] * (n + 1)  # ✅ Correct size
```

### **2. Incorrect Range Update**
```python
# ❌ Wrong:
diff[start] += shift_val
diff[end] -= shift_val  # Should be end+1

# ✅ Correct:
diff[start] += shift_val  
diff[end + 1] -= shift_val
```

### **3. Character Wrapping Issues**
```python
# ❌ Manual wrapping (error-prone):
if new_val > 25: new_val -= 26
if new_val < 0: new_val += 26

# ✅ Use modulo (handles all cases):
new_val = (old_val + shift) % 26
```

---

## **🎓 Key Takeaways**

### **1. Range Update Pattern**
When you need to apply the same operation to multiple ranges, consider difference arrays for O(1) range updates.

### **2. Batch Processing**
Instead of applying operations immediately, batch them and apply once for better performance.

### **3. Template for Similar Problems**
````python
def rangeUpdate(arr, operations):
    n = len(arr)
    diff = [0] * (n + 1)
    
    # Process all operations
    for start, end, value in operations:
        diff[start] += value
        diff[end + 1] -= value
    
    # Convert to actual values
    for i in range(1, n):
        diff[i] += diff[i-1]
    
    # Apply to original array
    for i in range(n):
        arr[i] += diff[i]
    
    return arr
```
