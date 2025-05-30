

<!-- problem:start -->

# [1926. Nearest Exit from Entrance in Maze](https://leetcode.com/problems/nearest-exit-from-entrance-in-maze)
---
- **comments**: true
- **difficulty**: Medium

- **rating**: 1638
- **source**: Biweekly Contest 56 Q2
- **tags**:
    - Breadth-First Search
    - Array
    - Matrix
---
## Description

<!-- description:start -->

<p>You are given an <code>m x n</code> matrix <code>maze</code> (<strong>0-indexed</strong>) with empty cells (represented as <code>&#39;.&#39;</code>) and walls (represented as <code>&#39;+&#39;</code>). You are also given the <code>entrance</code> of the maze, where <code>entrance = [entrance<sub>row</sub>, entrance<sub>col</sub>]</code> denotes the row and column of the cell you are initially standing at.</p>

<p>In one step, you can move one cell <strong>up</strong>, <strong>down</strong>, <strong>left</strong>, or <strong>right</strong>. You cannot step into a cell with a wall, and you cannot step outside the maze. Your goal is to find the <strong>nearest exit</strong> from the <code>entrance</code>. An <strong>exit</strong> is defined as an <strong>empty cell</strong> that is at the <strong>border</strong> of the <code>maze</code>. The <code>entrance</code> <strong>does not count</strong> as an exit.</p>

<p>Return <em>the <strong>number of steps</strong> in the shortest path from the </em><code>entrance</code><em> to the nearest exit, or </em><code>-1</code><em> if no such path exists</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/1900-1999/1926.Nearest%20Exit%20from%20Entrance%20in%20Maze/images/nearest1-grid.jpg" style="width: 333px; height: 253px;" />
<pre>
<strong>Input:</strong> maze = [["+","+",".","+"],[".","",".",".","+"],["+","+","+","."]], entrance = [1,2]
<strong>Output:</strong> 1
<strong>Explanation:</strong>
There are 3 exits in this maze at [1,0], [0,2], and [2,3].
Initially, you are at the entrance cell [1,2].
- You can reach [1,0] by moving 2 steps left.
- You can reach [0,2] by moving 1 step up.
It is impossible to reach [2,3] from the entrance.
Thus, the nearest exit is [0,2], which is 1 step away.
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/1900-1999/1926.Nearest%20Exit%20from%20Entrance%20in%20Maze/images/nearesr2-grid.jpg" style="width: 253px; height: 253px;" />
<pre>
<strong>Input:</strong> maze = [["+","+","+"],[".","",".","."],["+","+","+"]], entrance = [1,0]
<strong>Output:</strong> 2
<strong>Explanation:</strong>
There is 1 exit in this maze at [1,2].
[1,0] does not count as an exit since it is the entrance cell.
Initially, you are at the entrance cell [1,0].
- You can reach [1,2] by moving 2 steps right.
Thus, the nearest exit is [1,2], which is 2 steps away.
</pre>

<p><strong class="example">Example 3:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/1900-1999/1926.Nearest%20Exit%20from%20Entrance%20in%20Maze/images/nearest3-grid.jpg" style="width: 173px; height: 93px;" />
<pre>
<strong>Input:</strong> maze = [[".","+"]], entrance = [0,0]
<strong>Output:</strong> -1
<strong>Explanation:</strong>
There are no exits in this maze.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>maze.length == m</code></li>
	<li><code>maze[i].length == n</code></li>
	<li><code>1 &lt;= m, n &lt;= 100</code></li>
	<li><code>maze[i][j]</code> is either <code>&#39;.</code> or <code>&#39;+&#39;</code>.</li>
	<li><code>entrance.length == 2</code></li>
	<li><code>0 &lt;= entrance<sub>row</sub> &lt; m</code></li>
	<li><code>0 &lt;= entrance<sub>col</sub> &lt; n</code></li>
	<li><code>entrance</code> will always be an empty cell.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: BFS

We can start from the entrance and perform a breadth-first search (BFS). Each time we reach a new empty cell, we mark it as visited and add it to the queue until we find an empty cell on the boundary, then return the number of steps.

Specifically, we define a queue `q`, initially adding `entrance` to the queue. We define a variable `ans` to record the number of steps, initially set to `1`. Then we start the BFS. In each round, we take out all elements from the queue and traverse them. For each element, we try to move in four directions. If the new position is an empty cell, we add it to the queue and mark it as visited. If the new position is an empty cell on the boundary, we return `ans`. If the queue is empty, we return `-1`. After this round of search, we increment `ans` by one and continue to the next round of search.

If we finish the traversal without finding an empty cell on the boundary, we return `-1`.

The time complexity is `O(m × n)`, and the space complexity is `O(m × n)`. Here, `m` and `n` are the number of rows and columns in the maze, respectively.

<!-- tabs:start -->

#### Python3

```python
from collections import deque
class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m, n = len(maze), len(maze[0])
        i, j = entrance
        q = deque([(i, j)])
        maze[i][j] = "+"
        ans = 0
        while q:
            ans += 1
            for _ in range(len(q)):
                i, j = q.popleft()
                for a, b in [[0, -1], [0, 1], [-1, 0], [1, 0]]:
                    x, y = i + a, j + b
                    if 0 <= x < m and 0 <= y < n and maze[x][y] == ".":
                        if x == 0 or x == m - 1 or y == 0 or y == n - 1:
                            return ans
                        q.append((x, y))
                        maze[x][y] = "+"
        return -1
```

#### Java

```java
class Solution {
    public int nearestExit(char[][] maze, int[] entrance) {
        int m = maze.length, n = maze[0].length;
        final int[] dirs = {-1, 0, 1, 0, -1};
        Deque<int[]> q = new ArrayDeque<>();
        q.offer(entrance);
        maze[entrance[0]][entrance[1]] = '+';
        for (int ans = 1; !q.isEmpty(); ++ans) {
            for (int k = q.size(); k > 0; --k) {
                var p = q.poll();
                for (int d = 0; d < 4; ++d) {
                    int x = p[0] + dirs[d], y = p[1] + dirs[d + 1];
                    if (x >= 0 && x < m && y >= 0 && y < n && maze[x][y] == '.') {
                        if (x == 0 || x == m - 1 || y == 0 || y == n - 1) {
                            return ans;
                        }
                        maze[x][y] = '+';
                        q.offer(new int[] {x, y});
                    }
                }
            }
        }
        return -1;
    }
}
```

#### C++

```cpp
#include <queue>
#include <vector>
using namespace std;

class Solution {
public:
    int nearestExit(vector<vector<char>>& maze, vector<int>& entrance) {
        int m = maze.size(), n = maze[0].size();
        int dirs[5] = {-1, 0, 1, 0, -1};
        queue<pair<int, int>> q;


        q.push({entrance[0], entrance[1]});
        maze[entrance[0]][entrance[1]] = '+';
        for (int ans = 1; !q.empty(); ++ans) {
            for (int sz = q.size(); sz > 0; --sz) {
                auto [x, y] = q.front();
                q.pop();
                for (int d = 0; d < 4; ++d) {
                    int nx = x + dirs[d], ny = y + dirs[d + 1];
                    if (nx >= 0 && nx < m && ny >= 0 && ny < n && maze[nx][ny] == '.') {
                        if (nx == 0 || nx == m - 1 || ny == 0 || ny == n - 1) {
                            return ans;
                        }
                        maze[nx][ny] = '+';
                        q.push({nx, ny});
                    }
                }
            }
        }
        return -1;
    }
};
```

#### Go

```go
import "container/list"

func nearestExit(maze [][]byte, entrance []int) int {
    dirs := []int{-1, 0, 1, 0, -1}
    m, n := len(maze), len(maze[0])
    queue := list.New()
    queue.PushBack(entrance)
    maze[entrance[0]][entrance[1]] = '+'
    for steps := 1; queue.Len() > 0; steps++ {
        for sz := queue.Len(); sz > 0; sz-- {
            p := queue.Remove(queue.Front()).([2]int)
            for d := 0; d < 4; d++ {
                x, y := p[0]+dirs[d], p[1]+dirs[d+1]
                if x >= 0 && x < m && y >= 0 && y < n && maze[x][y] == '.' {
                    if x == 0 || x == m-1 || y == 0 || y == n-1 {
                        return steps
                    }
                    maze[x][y] = '+'
                    queue.PushBack([2]int{x, y})
                }
            }
        }
    }
    return -1
}
```

#### TypeScript

```typescript
function nearestExit(maze: string[][], entrance: number[]): number {
    const dirs = [-1, 0, 1, 0, -1];
    const m = maze.length, n = maze[0].length;
    const queue: number[][] = [entrance];
    maze[entrance[0]][entrance[1]] = '+';
    for (let ans = 1; queue.length > 0; ++ans) {
        for (let sz = queue.length; sz > 0; --sz) {
            const [x, y] = queue.shift()!;
            for (let d = 0; d < 4; ++d) {
                const nx = x + dirs[d], ny = y + dirs[d + 1];
                if (nx >= 0 && nx < m && ny >= 0 && ny < n && maze[nx][ny] === '.') {
                    if (nx === 0 || nx === m - 1 || ny === 0 || ny === n - 1) {
                        return ans;
                    }
                    maze[nx][ny] = '+';
                    queue.push([nx, ny]);
                }
            }
        }
    }
    return -1;
}
```

<!-- solution:end -->

## Related Topics
- Breadth-First Search
- Array
- Matrix

## Similar Problems
- [542. 01 Matrix](https://leetcode.com/problems/01-matrix/)
- [1091. Shortest Path in Binary Matrix](https://leetcode.com/problems/shortest-path-in-binary-matrix/)
- [1094. Car Pooling](https://leetcode.com/problems/car-pooling/)

<!-- problem:end -->
