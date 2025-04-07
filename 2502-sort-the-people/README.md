<h2><a href="https://leetcode.com/problems/sort-the-people">2502. Sort the People</a></h2><h3>Easy</h3><hr><p>You are given an array of strings <code>names</code>, and an array <code>heights</code> that consists of <strong>distinct</strong> positive integers. Both arrays are of length <code>n</code>.</p>

<p>For each index <code>i</code>, <code>names[i]</code> and <code>heights[i]</code> denote the name and height of the <code>i<sup>th</sup></code> person.</p>

<p>Return <code>names</code><em> sorted in <strong>descending</strong> order by the people&#39;s heights</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> names = [&quot;Mary&quot;,&quot;John&quot;,&quot;Emma&quot;], heights = [180,165,170]
<strong>Output:</strong> [&quot;Mary&quot;,&quot;Emma&quot;,&quot;John&quot;]
<strong>Explanation:</strong> Mary is the tallest, followed by Emma and John.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> names = [&quot;Alice&quot;,&quot;Bob&quot;,&quot;Bob&quot;], heights = [155,185,150]
<strong>Output:</strong> [&quot;Bob&quot;,&quot;Alice&quot;,&quot;Bob&quot;]
<strong>Explanation:</strong> The first Bob is the tallest, followed by Alice and the second Bob.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == names.length == heights.length</code></li>
	<li><code>1 &lt;= n &lt;= 10<sup>3</sup></code></li>
	<li><code>1 &lt;= names[i].length &lt;= 20</code></li>
	<li><code>1 &lt;= heights[i] &lt;= 10<sup>5</sup></code></li>
	<li><code>names[i]</code> consists of lower and upper case English letters.</li>
	<li>All the values of <code>heights</code> are distinct.</li>
</ul>

# Solution
* Map `height: names` as heights are distinct not names 
```python
class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        names_height = dict()
        for name,height in zip(names, heights):
            names_height[height] = name
        
        return [name for _,name  in sorted(names_height.items(), key=lambda item: item[0], reverse=True)]
```

```python
class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        names_height = {height: name for name, height in zip(names, heights)}
        return [name for _,name  in sorted(names_height.items(), key=lambda item: item[0], reverse=True)]
```

## Easy Solution
```python
class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        number_of_people = len(names)

        # Create a dictionary to store height-name pairs
        height_to_name_map = dict(zip(heights, names))

        sorted_heights = sorted(heights, reverse=True)

        # Create a list of sorted names based on descending heights
        sorted_names = [height_to_name_map[height] for height in sorted_heights]

        return sorted_names
```
