<h2><a href="https://leetcode.com/problems/string-without-aaa-or-bbb/?envType=problem-list-v2&envId=greedy">1026. String Without AAA or BBB</a></h2><h3>Medium</h3><hr><p>Given two integers <code>a</code> and <code>b</code>, return <strong>any</strong> string <code>s</code> such that:</p>

<ul>
	<li><code>s</code> has length <code>a + b</code> and contains exactly <code>a</code> <code>&#39;a&#39;</code> letters, and exactly <code>b</code> <code>&#39;b&#39;</code> letters,</li>
	<li>The substring <code>&#39;aaa&#39;</code> does not occur in <code>s</code>, and</li>
	<li>The substring <code>&#39;bbb&#39;</code> does not occur in <code>s</code>.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> a = 1, b = 2
<strong>Output:</strong> &quot;abb&quot;
<strong>Explanation:</strong> &quot;abb&quot;, &quot;bab&quot; and &quot;bba&quot; are all correct answers.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> a = 4, b = 1
<strong>Output:</strong> &quot;aabaa&quot;
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= a, b &lt;= 100</code></li>
	<li>It is guaranteed such an <code>s</code> exists for the given <code>a</code> and <code>b</code>.</li>
</ul>


## Solution Approach 
* Run a while loop until the result lenght is same as `a+b` 
* If either of a or b is zero, add the rest and break the loop 
* If `a>b` add 'aab` 
* If `b>a` add 'bba' 
* else `ab`

```python
def stringwith3a3b(a, b):
    result = ''
    total_lenght =  a+b

    while len(result) < total_lenght:
        if a == 0 or b == 0:
            if a == 0:
                print('a is zero')
                result += 'b'*b
                break
            else:
                print('b is zero')
                result += 'a'*a
                break
        elif a > b:
            print('a is greater')
            result += 'aab'
            a -= 2
            b -= 1
        elif b > a:
            print('b is greater')
            result += 'bba'
            b -= 2
            a -= 1
        else:
            result += 'ab'
            a -= 1
            b -= 1
        print(result, a, b)

    return result
```

## Improved Solution
* After doing the check 
* Do a final check to see if anything is zero, if yes add the other rest of the elements and break the loop 

```python
class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        result = ''
        total_lenght = a+b

        while len(result) < total_lenght:
            if a > b:
                result += 'aab'
                a -= 2
                b -= 1
            elif b > a:
                result += 'bba'
                b -= 2
                a -= 1
            else:
                result += 'ab'
                a -= 1
                b -= 1

            if a == 0 or b == 0:
                if a == 0:
                    result += 'b'*b
                    break
                else:
                    result += 'a'*a
                    break

        return result
```
