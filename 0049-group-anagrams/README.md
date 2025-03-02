<h2><a href="https://leetcode.com/problems/group-anagrams">49. Group Anagrams</a></h2><h3>Medium</h3><hr><p>Given an array of strings <code>strs</code>, group the <span data-keyword="anagram">anagrams</span> together. You can return the answer in <strong>any order</strong>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">strs = [&quot;eat&quot;,&quot;tea&quot;,&quot;tan&quot;,&quot;ate&quot;,&quot;nat&quot;,&quot;bat&quot;]</span></p>

<p><strong>Output:</strong> <span class="example-io">[[&quot;bat&quot;],[&quot;nat&quot;,&quot;tan&quot;],[&quot;ate&quot;,&quot;eat&quot;,&quot;tea&quot;]]</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>There is no string in strs that can be rearranged to form <code>&quot;bat&quot;</code>.</li>
	<li>The strings <code>&quot;nat&quot;</code> and <code>&quot;tan&quot;</code> are anagrams as they can be rearranged to form each other.</li>
	<li>The strings <code>&quot;ate&quot;</code>, <code>&quot;eat&quot;</code>, and <code>&quot;tea&quot;</code> are anagrams as they can be rearranged to form each other.</li>
</ul>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">strs = [&quot;&quot;]</span></p>

<p><strong>Output:</strong> <span class="example-io">[[&quot;&quot;]]</span></p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">strs = [&quot;a&quot;]</span></p>

<p><strong>Output:</strong> <span class="example-io">[[&quot;a&quot;]]</span></p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= strs.length &lt;= 10<sup>4</sup></code></li>
	<li><code>0 &lt;= strs[i].length &lt;= 100</code></li>
	<li><code>strs[i]</code> consists of lowercase English letters.</li>
</ul>

## solution Approach 
* Take the string and sort the string 
* Check if the sorted string is in the dict 
* If yes add the normal string the ditc result if not assign it a new value 
```python
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}                          ## Store the result 
        for string in strs:
            temp = []  
            for c in string:                 ## Unnecessary Loop 
                temp.append(c)
            temp.sort()
            sorted_str = ''.join(temp)
            if sorted_str in result:
                result[sorted_str] += [string]
            else:
                result[sorted_str] = [string]
                
        return list(result.values())
```

### Improved Solution 
```python
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}
        for string in strs:
            sorted_str = ''.join(sorted(string))
            if sorted_str in result:    ## Remove the if conditon 
                result[sorted_str] += [string]
            else:
                result[sorted_str] = [string]
                
        return list(result.values())
```
* Removed the If condition 
```python
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}
        for string in strs:
            sorted_str = ''.join(sorted(string))
            result[sorted_str] = result.get(sorted_str, []) + [string]
                
        return list(result.values())
```

## Optimal Solution 


