<h2><a href="https://leetcode.com/problems/diagonal-traverse">498. Diagonal Traverse</a></h2><h3>Medium</h3><hr><p>Given an <code>m x n</code> matrix <code>mat</code>, return <em>an array of all the elements of the array in a diagonal order</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/04/10/diag1-grid.jpg" style="width: 334px; height: 334px;" />
<pre>
<strong>Input:</strong> mat = [[1,2,3],[4,5,6],[7,8,9]]
<strong>Output:</strong> [1,2,4,7,5,3,6,8,9]
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> mat = [[1,2],[3,4]]
<strong>Output:</strong> [1,2,3,4]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>m == mat.length</code></li>
	<li><code>n == mat[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 10<sup>4</sup></code></li>
	<li><code>1 &lt;= m * n &lt;= 10<sup>4</sup></code></li>
	<li><code>-10<sup>5</sup> &lt;= mat[i][j] &lt;= 10<sup>5</sup></code></li>
</ul>

# Solution 
**Elements on the same diagonal have the same sum of indices `(i+j)`.**
```ini
# Matrix indices and their diagonal groups:
# (0,0) → i+j = 0    (0,1) → i+j = 1    (0,2) → i+j = 2
# (1,0) → i+j = 1    (1,1) → i+j = 2    (1,2) → i+j = 3  
# (2,0) → i+j = 2    (2,1) → i+j = 3    (2,2) → i+j = 4

# Diagonal 0: [(0,0)]
# Diagonal 1: [(0,1), (1,0)]  
# Diagonal 2: [(0,2), (1,1), (2,0)]
```

## Direction Pattern:
* Even diagonals (0, 2, 4...): Traverse bottom-up → reverse order
* Odd diagonals (1, 3, 5...): Traverse top-down → normal order

```python
def findDiagonalOrder(mat):
    diagonalMat = defaultdict(list)
    res = []

    for i in range(len(mat)):
        for j in range(len(mat[0])):
            diagonalMat[i+j].append(mat[i][j])
    
    # diagonalMat = dict(sorted(diagonalMat.items(), key=lambda item: item[0]))

    for i, val in diagonalMat.items():
        if i % 2:
            res.extend(val)
        else:
            res.extend(val[::-1])

    return res
```
---
```python
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        diagonalMat = defaultdict(list)
    
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                diagonalMat[i+j].append(mat[i][j])
        
        result = []
        for diagonal_sum in sorted(diagonalMat.keys()):  # Ensure order
            if diagonal_sum % 2:
                result.extend(diagonalMat[diagonal_sum])
            else:
                result.extend(diagonalMat[diagonal_sum][::-1])
        
        return result
```

# Clean Solution 
**KEY FORMULA**: `j = d - i`
For any diagonal `d`, if you know the row index `i`, you can calculate the column index `j` using. 
```ini
j = d - i
# Where d = diagonal number (0, 1, 2, ...)
```
```
# Diagonal Mapping 
# d=0: i+j=0 → (0,0)
# d=1: i+j=1 → (0,1), (1,0)  
# d=2: i+j=2 → (0,2), (1,1), (2,0)
# d=3: i+j=3 → (1,2), (2,1)
# d=4: i+j=4 → (2,2)
```

#### Step 1: Calculate Total Diagonals 
```ini 
m, n = 3, 3  # 3x3 matrix
total_diagonals = m + n - 1 = 5  # Diagonals 0,1,2,3,4
```

#### Step 2: For each Diagonal `d`, Generate Valid Coordinates
```ini 
# d = 0
d = 0
for i in range(3):  # i = 0,1,2
    j = d - i = 0 - i
    # i=0: j=0 → (0,0) ✅ Valid
    # i=1: j=-1 → Invalid (j < 0)
    # i=2: j=-2 → Invalid (j < 0)
# Result: [(0,0)] → [1]

d = 1  
for i in range(3):
    j = d - i = 1 - i
    # i=0: j=1 → (0,1) ✅ Valid  
    # i=1: j=0 → (1,0) ✅ Valid
    # i=2: j=-1 → Invalid (j < 0)
# Result: [(0,1), (1,0)] → [2, 4]

d = 2
for i in range(3):
    j = d - i = 2 - i  
    # i=0: j=2 → (0,2) ✅ Valid
    # i=1: j=1 → (1,1) ✅ Valid
    # i=2: j=0 → (2,0) ✅ Valid
# Result: [(0,2), (1,1), (2,0)] → [3, 5, 7]

# For d=3, m=3, n=3:
for i in range(3):
    j = 3 - i
    # i=0: j=3 → Invalid (j >= n=3)
    # i=1: j=2 → (1,2) ✅ Valid
    # i=2: j=1 → (2,1) ✅ Valid

# Without the check, we'd try to access mat[0][3] → IndexError!
```
#### Step 3: Complete Trace Example 
```ini
INPUT: mat = [[1,2,3],[4,5,6],[7,8,9]]
# d=0: diagonal=[(0,0)] → [1] → reverse → [1]
# d=1: diagonal=[(0,1),(1,0)] → [2,4] → normal → [2,4]  
# d=2: diagonal=[(0,2),(1,1),(2,0)] → [3,5,7] → reverse → [7,5,3]
# d=3: diagonal=[(1,2),(2,1)] → [6,8] → normal → [6,8]
# d=4: diagonal=[(2,2)] → [9] → reverse → [9]

# Final result: [1,2,4,7,5,3,6,8,9]
```

```python
m, n = len(mat), len(mat[0])
    result = []
    
    # Process each diagonal
    for d in range(m + n - 1):
        diagonal = []
        
        # Collect elements in current diagonal
        for i in range(m):
            j = d - i
            if 0 <= j < n:
                diagonal.append(mat[i][j])
        
        # Add in correct direction
        if d % 2 == 0:
            result.extend(diagonal[::-1])
        else:
            result.extend(diagonal)
    
    return result
```
