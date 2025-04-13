# 2352. Equal Row and Column Pairs

**Difficulty:** Medium  
**Source:** [Weekly Contest 303 - Q2](https://leetcode.com/contest/weekly-contest-303)  
**Tags:** Array, Hash Table, Matrix, Simulation  
**Rating:** 1286  

---

## Problem

Given a **0-indexed** `n x n` integer matrix `grid`, return the number of pairs `(ri, cj)` such that row `ri` and column `cj` are equal.

A row and column pair is considered equal if they contain the same elements in the same order (i.e., an equal array).

---

## Examples

### Example 1:

**Input:**

```
grid = [[3,2,1],
        [1,7,6],
        [2,7,7]]
```

**Output:** `1`  
**Explanation:** There is 1 equal row and column pair:
- (Row 2, Column 1): [2,7,7]

---

### Example 2:

**Input:**

```
grid = [[3,1,2,2],
        [1,4,4,5],
        [2,4,2,2],
        [2,4,2,2]]
```

**Output:** `3`  
**Explanation:** There are 3 equal row and column pairs:
- (Row 0, Column 0): [3,1,2,2]  
- (Row 2, Column 2): [2,4,2,2]  
- (Row 3, Column 2): [2,4,2,2]

---

## Constraints

- `n == grid.length == grid[i].length`
- `1 <= n <= 200`
- `1 <= grid[i][j] <= 10⁵`

---

## Explanation

We need to count the number of times a row in the grid exactly matches a column. One efficient way to approach this is:

1. Store all row vectors in a hash map with their frequencies.
2. For each column vector, check if it exists in the row hash map and count how many times.

This reduces redundant comparisons and avoids brute force $O(n^3)$ complexity.

---

## Solutions

### Python3

```python
from collections import Counter

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        row_map = Counter(tuple(row) for row in grid)
        count = 0
        for col in zip(*grid):
            count += row_map[tuple(col)]
        return count
```

---

### Java

```java
class Solution {
    public int equalPairs(int[][] grid) {
        int n = grid.length;
        Map<String, Integer> rowMap = new HashMap<>();
        for (int[] row : grid) {
            String key = Arrays.toString(row);
            rowMap.put(key, rowMap.getOrDefault(key, 0) + 1);
        }

        int count = 0;
        for (int j = 0; j < n; j++) {
            int[] col = new int[n];
            for (int i = 0; i < n; i++) {
                col[i] = grid[i][j];
            }
            String key = Arrays.toString(col);
            count += rowMap.getOrDefault(key, 0);
        }

        return count;
    }
}
```

---

### C++

```cpp
class Solution {
public:
    int equalPairs(vector<vector<int>>& grid) {
        int n = grid.size();
        map<vector<int>, int> rowMap;
        for (auto& row : grid) {
            rowMap[row]++;
        }

        int count = 0;
        for (int j = 0; j < n; ++j) {
            vector<int> col;
            for (int i = 0; i < n; ++i) {
                col.push_back(grid[i][j]);
            }
            count += rowMap[col];
        }

        return count;
    }
};
```

---

### Go

```go
func equalPairs(grid [][]int) int {
    n := len(grid)
    rowMap := map[string]int{}
    for _, row := range grid {
        key := fmt.Sprint(row)
        rowMap[key]++
    }

    count := 0
    for j := 0; j < n; j++ {
        col := []int{}
        for i := 0; i < n; i++ {
            col = append(col, grid[i][j])
        }
        key := fmt.Sprint(col)
        count += rowMap[key]
    }
    return count
}
```

---

### TypeScript

```ts
function equalPairs(grid: number[][]): number {
    const n = grid.length;
    const rowMap = new Map<string, number>();
    
    for (const row of grid) {
        const key = row.join(',');
        rowMap.set(key, (rowMap.get(key) ?? 0) + 1);
    }

    let count = 0;
    for (let j = 0; j < n; ++j) {
        const col: number[] = [];
        for (let i = 0; i < n; ++i) {
            col.push(grid[i][j]);
        }
        const key = col.join(',');
        count += rowMap.get(key) ?? 0;
    }

    return count;
}
```

