<h2><a href="https://leetcode.com/problems/remove-k-digits">402. Remove K Digits</a></h2><h3>Medium</h3><hr><p>Given string num representing a non-negative integer <code>num</code>, and an integer <code>k</code>, return <em>the smallest possible integer after removing</em> <code>k</code> <em>digits from</em> <code>num</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> num = &quot;1432219&quot;, k = 3
<strong>Output:</strong> &quot;1219&quot;
<strong>Explanation:</strong> Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> num = &quot;10200&quot;, k = 1
<strong>Output:</strong> &quot;200&quot;
<strong>Explanation:</strong> Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> num = &quot;10&quot;, k = 2
<strong>Output:</strong> &quot;0&quot;
<strong>Explanation:</strong> Remove all the digits from the number and it is left with nothing which is 0.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= k &lt;= num.length &lt;= 10<sup>5</sup></code></li>
	<li><code>num</code> consists of only digits.</li>
	<li><code>num</code> does not have any leading zeros except for the zero itself.</li>
</ul>

# Solution 
# Remove K Digits - Complete Learning Notes

"""
PROBLEM: Remove k digits from number string to make smallest possible number

EXAMPLES:
"1432219", k=3 → "1219" (remove 4,3,2)
"10200", k=1 → "200" (remove 1)  
"10", k=2 → "0" (remove both digits)
"54321", k=2 → "321" (remove 5,4)

KEY INSIGHTS:
1. Use GREEDY approach: remove larger digits when possible
2. If digit[i] > digit[i+1], removing digit[i] makes number smaller
3. Use STACK to allow "looking back" after removals
4. Handle remaining k removals by removing from end
5. Handle leading zeros and empty results
"""

# OPTIMAL SOLUTION:
```python
def removeKdigits(num, k):
    n = len(num)
    
    if k >= n:
        return '0'
    
    stack = []
    i = 0
    
    # Phase 1: Greedy removal using stack
    while i < n and k > 0:
        # Remove digits from stack if current digit is smaller
        while stack and k > 0 and stack[-1] > num[i]:
            stack.pop()
            k -= 1
        stack.append(num[i])
        i += 1
    
    # Add remaining digits
    while i < n:
        stack.append(num[i])
        i += 1
    
    # Phase 2: Remove remaining k digits from end
    while k > 0:
        stack.pop()
        k -= 1
    
    # Phase 3: Handle leading zeros and empty result
    result = ''.join(stack).lstrip('0')
    return result if result else '0'
```
"""
YOUR LEARNING JOURNEY & MISTAKES:

MISTAKE 1 - Single Pass Without Stack:
❌ Initial approach: Mark digits with '*' and continue forward
Problem: After removing a digit, you need to reconsider previous digits
Example: "1432" → remove 4, now need to compare 1 vs 3

LESSON: Use stack for "looking back" capability

MISTAKE 2 - Index Management Issues:
❌ Problem: After marking digit for removal, indices get misaligned
❌ Your fix attempt: Complex index tracking with marked positions

LESSON: Stack eliminates index management complexity

MISTAKE 3 - Integer Conversion Error:
❌ Code: return str(int(''.join(res)))
❌ Error: "Exceeds the limit (4300 digits) for integer string conversion"

LESSON: Use string manipulation (.lstrip('0')) instead of int conversion

MISTAKE 4 - Incomplete K Handling:
❌ Problem: What if k > 0 after processing all digits?
❌ Missing: Remove remaining digits from end

LESSON: Two-phase algorithm - greedy removal + cleanup

YOUR FINAL BREAKTHROUGH:
✅ Used stack for lookback capability
✅ Two-phase removal (greedy + end removal)  
✅ String manipulation for leading zeros
✅ Proper edge case handling
"""

# ALGORITHM BREAKDOWN:

"""
PHASE 1 - Greedy Stack Removal:
while i < n and k > 0:
    while stack and k > 0 and stack[-1] > num[i]:
        stack.pop()  # Remove larger digit
        k -= 1
    stack.append(num[i])
    i += 1

Why this works:
- If current digit < top of stack, removing stack top makes number smaller
- Stack allows us to "look back" and remove previously added digits
- Continue until no more beneficial removals or k exhausted

PHASE 2 - Handle Remaining Digits:
- Add any unprocessed digits: stack.extend(num[i:])  
- Remove remaining k digits from end: stack = stack[:-k]

PHASE 3 - Format Result:
- Remove leading zeros: result.lstrip('0')
- Handle empty result: return result if result else '0'
"""

# TRACE EXAMPLE: "1432219", k=3

"""
i=0, num[0]='1': stack=[], add '1' → stack=['1']
i=1, num[1]='4': '1'<'4', add '4' → stack=['1','4'] 
i=2, num[2]='3': '4'>'3', remove '4', k=2 → stack=['1'], add '3' → stack=['1','3']
i=3, num[3]='2': '3'>'2', remove '3', k=1 → stack=['1'], add '2' → stack=['1','2']  
i=4, num[4]='2': '2'='2', add '2' → stack=['1','2','2']
i=5, num[5]='1': '2'>'1', remove '2', k=0 → stack=['1','2'], add '1' → stack=['1','2','1']
i=6, num[6]='9': k=0, add '9' → stack=['1','2','1','9']

Result: '1219'
"""

# COMMON PITFALLS & SOLUTIONS:

"""
PITFALL 1: Infinite Loop
❌ while stack and stack[-1] > num[i]: (missing k > 0 check)
✅ while stack and k > 0 and stack[-1] > num[i]:

PITFALL 2: Index Out of Bounds  
❌ Forgetting to check if k > 0 before popping
✅ Always check k > 0 in while condition

PITFALL 3: Large Number Conversion
❌ str(int(result)) fails on huge numbers
✅ result.lstrip('0') for leading zero removal

PITFALL 4: Empty Result
❌ Returning empty string when all digits removed
✅ return result if result else '0'

PITFALL 5: Remaining K Not Zero
❌ Not handling case where greedy phase doesn't use all k
✅ Remove remaining k digits from end: stack = stack[:-k]
"""

# TEMPLATE FOR SIMILAR PROBLEMS:
"""
def removeKItems(arr, k, compare_func):
    if k >= len(arr):
        return default_result()
    
    stack = []
    
    # Phase 1: Greedy removal
    for item in arr:
        while stack and k > 0 and compare_func(stack[-1], item):
            stack.pop()
            k -= 1
        stack.append(item)
    
    # Phase 2: Remove remaining k items
    stack = stack[:-k] if k > 0 else stack
    
    # Phase 3: Format result
    return format_result(stack)

TIME: O(n) - each element pushed/popped at most once
SPACE: O(n) - stack storage
"""

# KEY TAKEAWAYS:
"""
1. STACK PATTERN: When you need to "look back" and reconsider previous decisions
2. GREEDY + CLEANUP: Two-phase algorithms for constraint satisfaction
3. STRING MANIPULATION: Avoid int conversion for very large numbers
4. EDGE CASE HANDLING: Empty results, remaining operations, leading zeros
5. DEBUGGING APPROACH: Trace through examples step by step
"""

# Optimal Solution 
```python
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if len(num)==k:
            return '0'
        stack = []
        for i in num:
            while stack and k>0 and stack[-1]>i:
                stack.pop()
                k-=1
            stack.append(i)
        if k>0:
            stack = stack[:-k]
        res = ''.join(stack).lstrip('0')
        return res if res else '0'
```        
				
