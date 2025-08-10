<h2><a href="https://leetcode.com/problems/count-vowel-strings-in-ranges/">2691. Count Vowel Strings in Ranges</a></h2><h3>Medium</h3><hr><p>You are given a <strong>0-indexed</strong> array of strings <code>words</code> and a 2D array of integers <code>queries</code>.</p>

<p>Each query <code>queries[i] = [l<sub>i</sub>, r<sub>i</sub>]</code> asks us to find the number of strings present at the indices ranging from <code>l<sub>i</sub></code> to <code>r<sub>i</sub></code> (both <strong>inclusive</strong>) of <code>words</code> that start and end with a vowel.</p>

<p>Return <em>an array </em><code>ans</code><em> of size </em><code>queries.length</code><em>, where </em><code>ans[i]</code><em> is the answer to the </em><code>i</code><sup>th</sup><em> query</em>.</p>

<p><strong>Note</strong> that the vowel letters are <code>&#39;a&#39;</code>, <code>&#39;e&#39;</code>, <code>&#39;i&#39;</code>, <code>&#39;o&#39;</code>, and <code>&#39;u&#39;</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> words = [&quot;aba&quot;,&quot;bcb&quot;,&quot;ece&quot;,&quot;aa&quot;,&quot;e&quot;], queries = [[0,2],[1,4],[1,1]]
<strong>Output:</strong> [2,3,0]
<strong>Explanation:</strong> The strings starting and ending with a vowel are &quot;aba&quot;, &quot;ece&quot;, &quot;aa&quot; and &quot;e&quot;.
The answer to the query [0,2] is 2 (strings &quot;aba&quot; and &quot;ece&quot;).
to query [1,4] is 3 (strings &quot;ece&quot;, &quot;aa&quot;, &quot;e&quot;).
to query [1,1] is 0.
We return [2,3,0].
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> words = [&quot;a&quot;,&quot;e&quot;,&quot;i&quot;], queries = [[0,2],[0,1],[2,2]]
<strong>Output:</strong> [3,2,1]
<strong>Explanation:</strong> Every string satisfies the conditions, so we return [3,2,1].</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= words.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= words[i].length &lt;= 40</code></li>
	<li><code>words[i]</code> consists only of lowercase English letters.</li>
	<li><code>sum(words[i].length) &lt;= 3 * 10<sup>5</sup></code></li>
	<li><code>1 &lt;= queries.length &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= l<sub>i</sub> &lt;= r<sub>i</sub> &lt;&nbsp;words.length</code></li>
</ul>
# Solution 
* Proper solution but the `Time Limit Exceeded` 

```python
class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowelCount = []
        count = 0
        n = len(queries)
        res = [0] * n
        vowels = {'a', 'e', 'i', 'o', 'u'}

        for word in words:
            if word[0] in vowels and word[-1] in vowels:
                vowelCount.append(1)
            else:
                vowelCount.append(0)
          
        for i in range(n):
            l, r = queries[i][0], queries[i][1]+1
            
            res[i] = sum(vowelCount[l:r])
        
        return res
```

# Improved Solution 
* when you do `res[i] = vowelCount[r] - vowelCount[l]` the diff excludes `l` so either we need a dummy or adjust the range manually 
1. **Your Issue**: `vowelCount[r] - vowelCount[l]` excludes the element at index `l`
2. **Fix Option 1**: Handle `l=0` specially, use `vowelCount[r] - vowelCount[l-1]` for `l>0`
3. **Fix Option 2**: Add dummy `0` at start, then use `vowelCount[r+1] - vowelCount[l]`
```python
class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowelCount = []
        count = 0
        n = len(queries)
        res = [0] * n
        vowels = {'a', 'e', 'i', 'o', 'u'}

        for word in words:
            if word[0] in vowels and word[-1] in vowels:
                count += 1
            vowelCount.append(count)
        
        print(vowelCount)
          
        for i in range(n):
            l, r = queries[i][0], queries[i][1]
            if l == 0:
                res[i] = vowelCount[r] 
            else:
                res[i] = vowelCount[r] - vowelCount[l-1]
        
        return res
```

# Optimal Solution 
```python
class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowelCount = [0] # Use dummy variable 
        count = 0
        vowels = {'a', 'e', 'i', 'o', 'u'}

        for word in words:
            if word[0] in vowels and word[-1] in vowels:
                count += 1
            vowelCount.append(count)
          
        res = []
        for l, r in queries:
            res.append(vowelCount[r + 1] - vowelCount[l])
        
        return res
```
# 📝 Prefix Sum & Range Query Problems - Study Notes

## 🎯 Problem Pattern: Range Sum Queries

### When to Use Prefix Sum:
- Multiple queries asking for sum of elements in a range `[l, r]`
- Need to optimize from O(n) per query to O(1) per query
- Total queries >> array modifications (read-heavy operations)

---

## 🔧 Implementation Patterns

### Pattern 1: Standard Prefix Sum (Your Solution)
```python
# Build prefix sum array
prefixSum = []
cumSum = 0
for element in array:
    if condition(element):  # Check if element should be counted
        cumSum += 1
    prefixSum.append(cumSum)

# Answer queries
for l, r in queries:
    if l == 0:
        result = prefixSum[r]
    else:
        result = prefixSum[r] - prefixSum[l-1]
```

### Pattern 2: Dummy Element Approach (Cleaner)
```python
# Build prefix sum with dummy 0 at start
prefixSum = [0]
cumSum = 0
for element in array:
    if condition(element):
        cumSum += 1
    prefixSum.append(cumSum)

# Answer queries (no special case needed!)
for l, r in queries:
    result = prefixSum[r+1] - prefixSum[l]
```

---

## 🧠 Key Concepts to Remember

### 1. Prefix Sum Formula
- `prefixSum[i]` = sum of elements from index 0 to i (inclusive)
- `sum(arr[l:r+1])` = `prefixSum[r] - prefixSum[l-1]` (when l > 0)

### 2. Boundary Conditions
- **Watch out for l = 0**: No element to subtract from
- **Solution**: Either handle specially OR use dummy element

### 3. Time Complexity Analysis
- **Brute Force**: O(n * q) where n = array size, q = number of queries
- **Prefix Sum**: O(n + q) - massive improvement for large q!

---

## 🐛 Common Mistakes & How to Avoid

### ❌ Mistake 1: Off-by-One in Range Calculation
```python
# WRONG: This excludes element at index l
result = prefixSum[r] - prefixSum[l]

# CORRECT: Include element at index l
if l == 0:
    result = prefixSum[r]
else:
    result = prefixSum[r] - prefixSum[l-1]
```

### ❌ Mistake 2: Forgetting Inclusive Range
- Query `[l, r]` means include BOTH l and r
- Array slicing `arr[l:r]` excludes r, but `arr[l:r+1]` includes r

### ❌ Mistake 3: Index Out of Bounds
```python
# Be careful when using l-1
if l == 0:
    # Handle this case to avoid prefixSum[-1]
```

---

## 🎯 Problem Variations

### 1. Count Elements Meeting Condition
```python
# Count vowel strings, even numbers, etc.
for element in array:
    if meets_condition(element):
        count += 1
    prefixSum.append(count)
```

### 2. Sum of Actual Values
```python
# Sum actual values, not just count
for element in array:
    if meets_condition(element):
        cumSum += element  # Add the value, not just 1
    prefixSum.append(cumSum)
```

### 3. 2D Prefix Sum (Matrix)
```python
# For 2D range sum queries
# prefixSum[i][j] = sum of rectangle from (0,0) to (i,j)
```

---

## 🧪 Testing Strategy

### Test Cases to Always Check:
1. **Single Element**: `arr = [x]`, query `[0,0]`
2. **All Elements**: Query covers entire array `[0, n-1]`
3. **Single Element Query**: `[i,i]` for various i
4. **Edge Boundaries**: `[0,k]` and `[k,n-1]` for various k
5. **No Valid Elements**: All elements fail condition

### Debugging Tips:
```python
# Always print your prefix sum array during development
print(f"Prefix sum: {prefixSum}")
print(f"Query [{l},{r}]: {prefixSum[r]} - {prefixSum[l-1] if l > 0 else 0}")
```

---

## 🏆 Similar Problems to Practice

### Beginner Level:
- Range Sum Query - Immutable (LeetCode 303)
- Find Pivot Index (LeetCode 724)

### Intermediate Level:
- Subarray Sum Equals K (LeetCode 560)
- Continuous Subarray Sum (LeetCode 523)

### Advanced Level:
- Range Sum Query 2D - Immutable (LeetCode 304)
- Maximum Size Subarray Sum Equals k (LeetCode 325)

---

## 💡 Quick Reference Checklist

Before implementing prefix sum:
- [ ] Multiple range queries on same array?
- [ ] Array doesn't change between queries?
- [ ] Need O(1) query time instead of O(n)?

During implementation:
- [ ] Handle l = 0 boundary case
- [ ] Use inclusive range [l, r]
- [ ] Consider dummy element for cleaner code
- [ ] Test with edge cases

Time complexity check:
- [ ] Preprocessing: O(n)
- [ ] Per query: O(1)
- [ ] Total: O(n + q) ✅

---

## 🔥 Pro Tips

1. **When in doubt, use dummy element approach** - cleaner code, fewer bugs
2. **Always trace through small example by hand** before coding
3. **Print intermediate results** during debugging
4. **Consider space-time tradeoffs** - prefix sum uses O(n) extra space
5. **For update-heavy scenarios**, consider Fenwick Tree or Segment Tree instead

---

*Remember: Prefix sum is your go-to technique for range sum queries on static arrays!*

