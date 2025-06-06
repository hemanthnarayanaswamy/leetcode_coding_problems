<h2><a href="https://leetcode.com/problems/count-items-matching-a-rule">1899. Count Items Matching a Rule</a></h2><h3>Easy</h3><hr><p>You are given an array <code>items</code>, where each <code>items[i] = [type<sub>i</sub>, color<sub>i</sub>, name<sub>i</sub>]</code> describes the type, color, and name of the <code>i<sup>th</sup></code> item. You are also given a rule represented by two strings, <code>ruleKey</code> and <code>ruleValue</code>.</p>

<p>The <code>i<sup>th</sup></code> item is said to match the rule if <strong>one</strong> of the following is true:</p>

<ul>
	<li><code>ruleKey == &quot;type&quot;</code> and <code>ruleValue == type<sub>i</sub></code>.</li>
	<li><code>ruleKey == &quot;color&quot;</code> and <code>ruleValue == color<sub>i</sub></code>.</li>
	<li><code>ruleKey == &quot;name&quot;</code> and <code>ruleValue == name<sub>i</sub></code>.</li>
</ul>

<p>Return <em>the number of items that match the given rule</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> items = [[&quot;phone&quot;,&quot;blue&quot;,&quot;pixel&quot;],[&quot;computer&quot;,&quot;silver&quot;,&quot;lenovo&quot;],[&quot;phone&quot;,&quot;gold&quot;,&quot;iphone&quot;]], ruleKey = &quot;color&quot;, ruleValue = &quot;silver&quot;
<strong>Output:</strong> 1
<strong>Explanation:</strong> There is only one item matching the given rule, which is [&quot;computer&quot;,&quot;silver&quot;,&quot;lenovo&quot;].
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> items = [[&quot;phone&quot;,&quot;blue&quot;,&quot;pixel&quot;],[&quot;computer&quot;,&quot;silver&quot;,&quot;phone&quot;],[&quot;phone&quot;,&quot;gold&quot;,&quot;iphone&quot;]], ruleKey = &quot;type&quot;, ruleValue = &quot;phone&quot;
<strong>Output:</strong> 2
<strong>Explanation:</strong> There are only two items matching the given rule, which are [&quot;phone&quot;,&quot;blue&quot;,&quot;pixel&quot;] and [&quot;phone&quot;,&quot;gold&quot;,&quot;iphone&quot;]. Note that the item [&quot;computer&quot;,&quot;silver&quot;,&quot;phone&quot;] does not match.</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= items.length &lt;= 10<sup>4</sup></code></li>
	<li><code>1 &lt;= type<sub>i</sub>.length, color<sub>i</sub>.length, name<sub>i</sub>.length, ruleValue.length &lt;= 10</code></li>
	<li><code>ruleKey</code> is equal to either <code>&quot;type&quot;</code>, <code>&quot;color&quot;</code>, or <code>&quot;name&quot;</code>.</li>
	<li>All strings consist only of lowercase letters.</li>
</ul>


# solution 
```python
class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        rule_map = {"type": 0, "color": 1, "name": 2}
        itemCounter = 0
        idx = rule_map[ruleKey]

        for item in items:
            if item[idx] == ruleValue:
                itemCounter += 1
        
        return itemCounter
```
```python
class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        i = 0 if ruleKey[0] == 't' else (1 if ruleKey[0] == 'c' else 2)
        return sum(v[i] == ruleValue for v in items)
```
