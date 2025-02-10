<h2><a href="https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses">1371. Minimum Remove to Make Valid Parentheses</a></h2><h3>Medium</h3><hr><p>Given a string <font face="monospace">s</font> of <code>&#39;(&#39;</code> , <code>&#39;)&#39;</code> and lowercase English characters.</p>

<p>Your task is to remove the minimum number of parentheses ( <code>&#39;(&#39;</code> or <code>&#39;)&#39;</code>, in any positions ) so that the resulting <em>parentheses string</em> is valid and return <strong>any</strong> valid string.</p>

<p>Formally, a <em>parentheses string</em> is valid if and only if:</p>

<ul>
	<li>It is the empty string, contains only lowercase characters, or</li>
	<li>It can be written as <code>AB</code> (<code>A</code> concatenated with <code>B</code>), where <code>A</code> and <code>B</code> are valid strings, or</li>
	<li>It can be written as <code>(A)</code>, where <code>A</code> is a valid string.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;lee(t(c)o)de)&quot;
<strong>Output:</strong> &quot;lee(t(c)o)de&quot;
<strong>Explanation:</strong> &quot;lee(t(co)de)&quot; , &quot;lee(t(c)ode)&quot; would also be accepted.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;a)b(c)d&quot;
<strong>Output:</strong> &quot;ab(c)d&quot;
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;))((&quot;
<strong>Output:</strong> &quot;&quot;
<strong>Explanation:</strong> An empty string is also valid.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>5</sup></code></li>
	<li><code>s[i]</code> is either&nbsp;<code>&#39;(&#39;</code> , <code>&#39;)&#39;</code>, or lowercase English letter.</li>
</ul>

#### Background 

* A prefix is the start of a string while the suffix is the end of a string. For instance, the prefixes of the string "abcd" are ["a","ab","abc"] . The suffixes are ["bcd", "cd", "d"] . You should not overlap the prefix and suffix. 

#### Parentheses Properties:
* For parentheses to be balanced, count of Opens must be equal to count of Closes. eg: for ( ( ( ) ) ), count = 3 and 3
* Each Close must form a pair with previously encountered Open. eg: for ) ) ) ( ( (, though count = 3 and 3, each Close doesn't have a previous Open to be paired with.


#### Approach 1: <b> Without using Stack </b>
1. Iterate through the string from left to right. Track the count of open parentheses encountered. If an excess closing parenthesis is encountered (i.e., a closing parenthesis with no matching opening parenthesis), mark it with '*'. Keep track of the count of open parentheses encountered.
2. Iterate through the string from right to left. If there are excess opening parentheses remaining (i.e., opening parentheses with no matching closing parenthesis), mark them with '*'.
3. Filter out the marked characters ('*') from the character array, leaving only the valid parentheses.

```python 
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        # Initialize variables
        openParenthesesCount = 0
        arr = list(s)

        # First pass: mark excess closing parentheses with '*'
        for i in range(len(arr)):
            if arr[i] == '(':
                openParenthesesCount += 1
            elif arr[i] == ')':
                if openParenthesesCount == 0:
                    arr[i] = '*' # Mark excess closing parentheses
                else:
                    openParenthesesCount -= 1

        # Second pass: mark excess opening parentheses from the end
        for i in range(len(arr) - 1, -1, -1):
            if openParenthesesCount > 0 and arr[i] == '(':
                arr[i] = '*' # Mark excess opening parentheses
                openParenthesesCount -= 1
        
        # Filter out marked characters and construct the result string
        result = ''.join(c for c in arr if c != '*')

        return result
```

 ### Approach 2: <b> Using Stacks </b>
1. Convert String in List
2. stack to keep track of ')'
3. First Iteration marking the closing ')' as empty strings
4. second iteration marking any leftover opening '(' as empty strings
5. Join the list

```python 
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        sList = list(s) # Convert String in List
        stack = [] # To keep tack of all opening 'c'
				
        for i,char in enumerate(s): ## Tracking Excess ')'
            if char == "(":
                stack.append(i)
            elif char == ")":
                if stack:
                    stack.pop()
                else:
                    sList[i] = ""   ## Replace ')' with a empty string 
    ## ['l', 'e', 'e', '(', 't', '(', 'c', ')', 'o', ')', 'd', 'e', '']

        for i in stack:   ## Now whatever is left in stack are the excess ')'
            sList[i] = "" ## mark them as empty strings 
        
        return "".join(sList) ## Join the List 
```
