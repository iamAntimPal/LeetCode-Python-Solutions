


<!-- problem:start -->

# [994. Rotting Oranges](https://leetcode.com/problems/rotting-oranges)
---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/0900-0999/0994.Rotting%20Oranges/README_EN.md
tags:
  - Breadth-First Search
  - Array
  - Matrix
---

## Description

You are given an `m x n` grid where each cell can have one of three values:

- `0` representing an empty cell,
- `1` representing a fresh orange, or
- `2` representing a rotten orange.

Every minute, any fresh orange that is **4-directionally adjacent** to a rotten orange becomes rotten.

Return *the minimum number of minutes that must elapse until no cell has a fresh orange*. If this is impossible, return `-1`.

**Example 1:**

![Example](https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0900-0999/0994.Rotting%20Oranges/images/oranges.png)

```
Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4
```

**Example 2:**

```
Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten.
```

**Example 3:**

```
Input: grid = [[0,2]]
Output: 0
Explanation: There are no fresh oranges to begin with.
```

**Constraints:**

- `m == grid.length`
- `n == grid[i].length`
- `1 <= m, n <= 10`
- `grid[i][j]` is `0`, `1`, or `2`.

<!-- problem:end -->

## Solutions

### Solution 1: BFS

We start by iterating over the grid to count the number of fresh oranges and collect all rotten orange positions into a queue. Then we simulate the process of rotting using Breadth-First Search (BFS). At each minute (each level in BFS), rotten oranges spread to adjacent fresh oranges.

If at the end, fresh oranges remain, return `-1`. Otherwise, return the total minutes elapsed.

Time complexity: `O(m * n)`  
Space complexity: `O(m * n)`

<!-- tabs:start -->

### **Python3**

```python
from collections import deque
from itertools import pairwise

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        cnt = 0
        q = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i, j))
                elif grid[i][j] == 1:
                    cnt += 1
        ans = 0
        dirs = (-1, 0, 1, 0, -1)
        while q and cnt:
            ans += 1
            for _ in range(len(q)):
                i, j = q.popleft()
                for a, b in pairwise(dirs):
                    x, y = i + a, j + b
                    if 0 <= x < m and 0 <= y < n and grid[x][y] == 1:
                        grid[x][y] = 2
                        q.append((x, y))
                        cnt -= 1
                        if cnt == 0:
                            return ans
        return -1 if cnt else 0
```

### **Java**

```java
class Solution {
    public int orangesRotting(int[][] grid) {
        int m = grid.length, n = grid[0].length;
        Deque<int[]> q = new ArrayDeque<>();
        int cnt = 0;
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (grid[i][j] == 1) {
                    ++cnt;
                } else if (grid[i][j] == 2) {
                    q.offer(new int[] {i, j});
                }
            }
        }
        final int[] dirs = {-1, 0, 1, 0, -1};
        for (int ans = 1; !q.isEmpty() && cnt > 0; ++ans) {
            for (int k = q.size(); k > 0; --k) {
                var p = q.poll();
                for (int d = 0; d < 4; ++d) {
                    int x = p[0] + dirs[d], y = p[1] + dirs[d + 1];
                    if (x >= 0 && x < m && y >= 0 && y < n && grid[x][y] == 1) {
                        grid[x][y] = 2;
                        q.offer(new int[] {x, y});
                        if (--cnt == 0) {
                            return ans;
                        }
                    }
                }
            }
        }
        return cnt > 0 ? -1 : 0;
    }
}
```

### **C++**

```cpp
class Solution {
public:
    int orangesRotting(vector<vector<int>>& grid) {
        int m = grid.size(), n = grid[0].size();
        queue<pair<int, int>> q;
        int cnt = 0;
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (grid[i][j] == 1) {
                    ++cnt;
                } else if (grid[i][j] == 2) {
                    q.emplace(i, j);
                }
            }
        }
        const int dirs[5] = {-1, 0, 1, 0, -1};
        for (int ans = 1; !q.empty() && cnt > 0; ++ans) {
            for (int k = q.size(); k > 0; --k) {
                auto [i, j] = q.front();
                q.pop();
                for (int d = 0; d < 4; ++d) {
                    int x = i + dirs[d], y = j + dirs[d + 1];
                    if (x >= 0 && x < m && y >= 0 && y < n && grid[x][y] == 1) {
                        grid[x][y] = 2;
                        q.emplace(x, y);
                        if (--cnt == 0) return ans;
                    }
                }
            }
        }
        return cnt > 0 ? -1 : 0;
    }
};
```

### **Go**

```go
func orangesRotting(grid [][]int) int {
    m, n := len(grid), len(grid[0])
    q := [][2]int{}
    cnt := 0
    for i := range grid {
        for j := range grid[0] {
            if grid[i][j] == 2 {
                q = append(q, [2]int{i, j})
            } else if grid[i][j] == 1 {
                cnt++
            }
        }
    }
    dirs := [5]int{-1, 0, 1, 0, -1}
    for ans := 1; len(q) > 0 && cnt > 0; ans++ {
        for k := len(q); k > 0; k-- {
            p := q[0]
            q = q[1:]
            for d := 0; d < 4; d++ {
                x, y := p[0]+dirs[d], p[1]+dirs[d+1]
                if x >= 0 && x < m && y >= 0 && y < n && grid[x][y] == 1 {
                    grid[x][y] = 2
                    q = append(q, [2]int{x, y})
                    cnt--
                    if cnt == 0 {
                        return ans
                    }
                }
            }
        }
    }
    if cnt > 0 {
        return -1
    }
    return 0
}
```

### **TypeScript**

```ts
function orangesRotting(grid: number[][]): number {
    const m = grid.length, n = grid[0].length;
    const q: number[][] = [];
    let cnt = 0;
    for (let i = 0; i < m; ++i) {
        for (let j = 0; j < n; ++j) {
            if (grid[i][j] === 2) q.push([i, j]);
            else if (grid[i][j] === 1) cnt++;
        }
    }
    const dirs = [-1, 0, 1, 0, -1];
    for (let ans = 1; q.length && cnt > 0; ++ans) {
        const t: number[][] = [];
        for (const [i, j] of q) {
            for (let d = 0; d < 4; ++d) {
                const x = i + dirs[d], y = j + dirs[d + 1];
                if (x >= 0 && x < m && y >= 0 && y < n && grid[x][y] === 1) {
                    grid[x][y] = 2;
                    t.push([x, y]);
                    cnt--;
                    if (cnt === 0) return ans;
                }
            }
        }
        q.splice(0, q.length, ...t);
    }
    return cnt > 0 ? -1 : 0;
}
```

### **Rust**

```rust
use std::collections::VecDeque;

impl Solution {
    pub fn oranges_rotting(mut grid: Vec<Vec<i32>>) -> i32 {
        let m = grid.len();
        let n = grid[0].len();
        let mut q = VecDeque::new();
        let mut cnt = 0;

        for i in 0..m {
            for j in 0..n {
                match grid[i][j] {
                    1 => cnt += 1,
                    2 => q.push_back((i, j)),
                    _ => (),
                }
            }
        }

        let dirs = [-1, 0, 1, 0, -1];
        for ans in 1.. {
            if q.is_empty() || cnt == 0 {
                break;
            }
            let size = q.len();
            for _ in 0..size {
                let (i, j) = q.pop_front().unwrap();
                for d in 0..4 {
                    let x = i as isize + dirs[d];
                    let y = j as isize + dirs[d + 1];
                    if x >= 0 && x < m as isize && y >= 0 && y < n as isize {
                        let (x, y) = (x as usize, y as usize);
                        if grid[x][y] == 1 {
                            grid[x][y] = 2;
                            q.push_back((x, y));
                            cnt -= 1;
                            if cnt == 0 {
                                return ans;
                            }
                        }
                    }
                }
            }
        }

        if cnt > 0 { -1 } else { 0 }
    }
}
```

### **JavaScript**

```js
var orangesRotting = function(grid) {
    const m = grid.length, n = grid[0].length;
    let q = [], cnt = 0;
    for (let i = 0; i < m; ++i) {
        for (let j = 0; j < n; ++j) {
            if (grid[i][j] === 2) q.push([i, j]);
            else if (grid[i][j] === 1) cnt++;
        }
    }

    const dirs = [-1, 0, 1, 0, -1];
    for (let ans = 1; q.length && cnt > 0; ++ans) {
        const t = [];
        for (const [i, j] of q) {
            for (let d = 0; d < 4; ++d) {
                const x = i + dirs[d], y = j + dirs[d + 1];
                if (x >= 0 && x < m && y >= 0 && y < n && grid[x][y] === 1) {
                    grid[x][y] = 2;
                    t.push([x, y]);
                    cnt--;
                    if (cnt === 0) return ans;
                }
            }
        }
        q = t;
    }
    return cnt > 0 ? -1 : 0;
};
```

<!-- tabs:end -->
