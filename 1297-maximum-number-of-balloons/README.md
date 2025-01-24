<h2><a href="https://leetcode.com/problems/maximum-number-of-balloons">1297. Maximum Number of Balloons</a></h2><h3>Easy</h3><hr><p>Given a string <code>text</code>, you want to use the characters of <code>text</code> to form as many instances of the word <strong>&quot;balloon&quot;</strong> as possible.</p>

<p>You can use each character in <code>text</code> <strong>at most once</strong>. Return the maximum number of instances that can be formed.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<p><strong><img alt="" src="https://assets.leetcode.com/uploads/2019/09/05/1536_ex1_upd.JPG" style="width: 132px; height: 35px;" /></strong></p>

<pre>
<strong>Input:</strong> text = &quot;nlaebolko&quot;
<strong>Output:</strong> 1
</pre>

<p><strong class="example">Example 2:</strong></p>

<p><strong><img alt="" src="https://assets.leetcode.com/uploads/2019/09/05/1536_ex2_upd.JPG" style="width: 267px; height: 35px;" /></strong></p>

<pre>
<strong>Input:</strong> text = &quot;loonbalxballpoon&quot;
<strong>Output:</strong> 2
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> text = &quot;leetcode&quot;
<strong>Output:</strong> 0
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= text.length &lt;= 10<sup>4</sup></code></li>
	<li><code>text</code> consists of lower case English letters only.</li>
</ul>

<p>&nbsp;</p>
<p><strong>Note:</strong> This question is the same as <a href="https://leetcode.com/problems/rearrange-characters-to-make-target-string/description/" target="_blank"> 2287: Rearrange Characters to Make Target String.</a></p>

### Solution 
1. First make the reference "ballon" hashmap word {'b':1, 'a':1, 'l':2, 'o':2, 'n': 1}
2. Create a Hashmap for the text parameter excluding the other characters 
3. now for each element in computed hashmap divide by the same element in reference 
4. Now return the min for that "The minimum value is the maximum number of times “balloon” can be formed from the text."

##### MY SOLUTION 
```python
def maxballons(text):
    balloon_ref = {'b':1, 'a':1, 'l':2, 'o':2, 'n': 1}
    text_ballon = {}
    for letter in text:
        if letter in balloon_ref:
            text_ballon[letter] = text_ballon.get(letter, 0) + 1
    for letter in balloon_ref:
        if letter not in text_ballon:
            return 0
        text_ballon[letter] = text_ballon[letter] // balloon_ref[letter]
    return min(text_ballon.values())
```

#### Change Solution
```python
def maxballons(text):
    balloon_ref = {'b':1, 'a':1, 'l':2, 'o':2, 'n': 1}
    text_ballon = {}
    for letter in text:
        if letter in balloon_ref:
            text_ballon[letter] = text_ballon.get(letter, 0) + 1
    return min(text_ballon.get(letter, 0) // balloon_ref[letter] for letter in balloon_ref)
```
