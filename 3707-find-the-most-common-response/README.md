<h2><a href="https://leetcode.com/problems/find-the-most-common-response">3707. Find the Most Common Response</a></h2><h3>Medium</h3><hr><p>You are given a 2D string array <code>responses</code> where each <code>responses[i]</code> is an array of strings representing survey responses from the <code>i<sup>th</sup></code> day.</p>

<p>Return the <strong>most common</strong> response across all days after removing <strong>duplicate</strong> responses within each <code>responses[i]</code>. If there is a tie, return the <em><span data-keyword="lexicographically-smaller-string">lexicographically smallest</span></em> response.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">responses = [[&quot;good&quot;,&quot;ok&quot;,&quot;good&quot;,&quot;ok&quot;],[&quot;ok&quot;,&quot;bad&quot;,&quot;good&quot;,&quot;ok&quot;,&quot;ok&quot;],[&quot;good&quot;],[&quot;bad&quot;]]</span></p>

<p><strong>Output:</strong> <span class="example-io">&quot;good&quot;</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>After removing duplicates within each list, <code>responses = [[&quot;good&quot;, &quot;ok&quot;], [&quot;ok&quot;, &quot;bad&quot;, &quot;good&quot;], [&quot;good&quot;], [&quot;bad&quot;]]</code>.</li>
	<li><code>&quot;good&quot;</code> appears 3 times, <code>&quot;ok&quot;</code> appears 2 times, and <code>&quot;bad&quot;</code> appears 2 times.</li>
	<li>Return <code>&quot;good&quot;</code> because it has the highest frequency.</li>
</ul>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">responses = [[&quot;good&quot;,&quot;ok&quot;,&quot;good&quot;],[&quot;ok&quot;,&quot;bad&quot;],[&quot;bad&quot;,&quot;notsure&quot;],[&quot;great&quot;,&quot;good&quot;]]</span></p>

<p><strong>Output:</strong> <span class="example-io">&quot;bad&quot;</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>After removing duplicates within each list we have <code>responses = [[&quot;good&quot;, &quot;ok&quot;], [&quot;ok&quot;, &quot;bad&quot;], [&quot;bad&quot;, &quot;notsure&quot;], [&quot;great&quot;, &quot;good&quot;]]</code>.</li>
	<li><code>&quot;bad&quot;</code>, <code>&quot;good&quot;</code>, and <code>&quot;ok&quot;</code> each occur 2 times.</li>
	<li>The output is <code>&quot;bad&quot;</code> because it is the lexicographically smallest amongst the words with the highest frequency.</li>
</ul>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= responses.length &lt;= 1000</code></li>
	<li><code>1 &lt;= responses[i].length &lt;= 1000</code></li>
	<li><code>1 &lt;= responses[i][j].length &lt;= 10</code></li>
	<li><code>responses[i][j]</code> consists of only lowercase English letters</li>
</ul>

# Solution 
* First we store the unique responses in a Map and get the maximum occured value.
* next store all the responses that have the maximum value. 
* Now sort the reponses to have them in `lexicographically Order` and return the first index value. 

```python
class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        responsesFreq = {}
        commonRes = []

        for i in range(len(responses)):
            uniqRes = set(responses[i])
            for r in uniqRes:
                responsesFreq[r] = responsesFreq.get(r, 0) + 1

        maxFreq = max(responsesFreq.values())

        for r,v in responsesFreq.items():
            if v == maxFreq:
                commonRes.append(r)

        return sorted(commonRes)[0]
```

# Improved Solution 
* Use the `Counter.update()` method to keep updating the Map for new occurances. 
* Use `min()` instead of sort to find the lexigraphically smallest string. 

```ini 
Find the Lexicographically Smallest String
* Apply the min() function to obtain the lexicographically smallest string.

names = ["Alice", "Bob", "Diana", "Eli"]
smallest_name = min(names)
print(smallest_name)

* Here, min() examines the strings in the list names. "Alice" is returned as it comes first lexicographically among the names.
```

```python
class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        responsesFreq = Counter()
        commonRes = []

        for response in responses:
            responsesFreq.update(set(response))

        maxFreq = max(responsesFreq.values())
            
        return min((r for r,v in responsesFreq.items() if v == maxFreq))
```

# Optimal Solution 
```python
class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        freq_map = {}
        highest_freq = -1
        highest_freq_word = ""

        for l in responses:
            used_words = set()

            for word in l:
                if word in used_words:
                    continue
                if word in freq_map:
                    freq_map[word] += 1
                else:
                    freq_map[word] = 1
                used_words.add(word)

        for key, val in freq_map.items():
            if val > highest_freq:
                highest_freq = val
                highest_freq_word = key

            elif val == highest_freq:
                highest_freq_word = min(key, highest_freq_word)
                
        return highest_freq_word
```
