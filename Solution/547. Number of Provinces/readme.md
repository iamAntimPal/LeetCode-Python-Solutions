# 547. Number of Provinces
- **difficulty**: Medium
- **related**: []
- **tags**: 
  - **Depth**-First Search
  - **Breadth**-First Search
  - **Union Find**
  - **Graph**
---

## Description

There are `n` cities. Some of them are connected, while some are not. If city `a` is connected directly with city `b`, and city `b` is connected directly with city `c`, then city `a` is connected indirectly with city `c`.

A **province** is a group of directly or indirectly connected cities and no other cities outside of the group.

You are given an `n x n` matrix `isConnected` where `isConnected[i][j] = 1` if the `i-th` city and the `j-th` city are directly connected, and `isConnected[i][j] = 0` otherwise.

Return *the total number of **provinces***.

## Examples

**Example 1:**

```
Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
Output: 2
```

**Example 2:**

```
Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
Output: 3
```

## Constraints

- `1 <= n <= 200`
- `n == isConnected.length`
- `n == isConnected[i].length`
- `isConnected[i][j]` is `1` or `0`.
- `isConnected[i][i] == 1`
- `isConnected[i][j] == isConnected[j][i]`

## Solutions

### Solution 1: DFS

We maintain a visited array and perform DFS from each unvisited node, marking all reachable nodes as visited. Each DFS traversal corresponds to a new province.

**Time Complexity:** O(n²)  
**Space Complexity:** O(n)

#### Python

```python
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(i: int):
            vis[i] = True
            for j, x in enumerate(isConnected[i]):
                if not vis[j] and x:
                    dfs(j)

        n = len(isConnected)
        vis = [False] * n
        ans = 0
        for i in range(n):
            if not vis[i]:
                dfs(i)
                ans += 1
        return ans
```

#### Java

```java
class Solution {
    private int[][] g;
    private boolean[] vis;

    public int findCircleNum(int[][] isConnected) {
        g = isConnected;
        int n = g.length;
        vis = new boolean[n];
        int ans = 0;
        for (int i = 0; i < n; ++i) {
            if (!vis[i]) {
                dfs(i);
                ++ans;
            }
        }
        return ans;
    }

    private void dfs(int i) {
        vis[i] = true;
        for (int j = 0; j < g.length; ++j) {
            if (!vis[j] && g[i][j] == 1) {
                dfs(j);
            }
        }
    }
}
```

#### C++

```cpp
class Solution {
public:
    int findCircleNum(vector<vector<int>>& isConnected) {
        int n = isConnected.size();
        int ans = 0;
        vector<bool> vis(n, false);
        function<void(int)> dfs = [&](int i) {
            vis[i] = true;
            for (int j = 0; j < n; ++j) {
                if (!vis[j] && isConnected[i][j]) {
                    dfs(j);
                }
            }
        };
        for (int i = 0; i < n; ++i) {
            if (!vis[i]) {
                dfs(i);
                ++ans;
            }
        }
        return ans;
    }
};
```

#### Go

```go
func findCircleNum(isConnected [][]int) int {
	n := len(isConnected)
	vis := make([]bool, n)
	var dfs func(int)
	dfs = func(i int) {
		vis[i] = true
		for j, x := range isConnected[i] {
			if !vis[j] && x == 1 {
				dfs(j)
			}
		}
	}
	ans := 0
	for i := range vis {
		if !vis[i] {
			ans++
			dfs(i)
		}
	}
	return ans
}
```

#### TypeScript

```ts
function findCircleNum(isConnected: number[][]): number {
    const n = isConnected.length;
    const vis = Array(n).fill(false);
    const dfs = (i: number) => {
        vis[i] = true;
        for (let j = 0; j < n; ++j) {
            if (!vis[j] && isConnected[i][j]) {
                dfs(j);
            }
        }
    };
    let ans = 0;
    for (let i = 0; i < n; ++i) {
        if (!vis[i]) {
            dfs(i);
            ++ans;
        }
    }
    return ans;
}
```

#### Rust

```rust
impl Solution {
    fn dfs(is_connected: &Vec<Vec<i32>>, vis: &mut Vec<bool>, i: usize) {
        vis[i] = true;
        for j in 0..is_connected.len() {
            if !vis[j] && is_connected[i][j] == 1 {
                Self::dfs(is_connected, vis, j);
            }
        }
    }

    pub fn find_circle_num(is_connected: Vec<Vec<i32>>) -> i32 {
        let n = is_connected.len();
        let mut vis = vec![false; n];
        let mut res = 0;
        for i in 0..n {
            if !vis[i] {
                res += 1;
                Self::dfs(&is_connected, &mut vis, i);
            }
        }
        res
    }
}
```

---

### Solution 2: Union-Find

Use Union-Find to group connected cities. Initially each city is its own parent. Merge cities with direct connections and count the number of distinct roots.

**Time Complexity:** O(n² * α(n))  
**Space Complexity:** O(n)

#### Python

```python
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def find(x):
            if p[x] != x:
                p[x] = find(p[x])
            return p[x]

        n = len(isConnected)
        p = list(range(n))
        ans = n
        for i in range(n):
            for j in range(i + 1, n):
                if isConnected[i][j]:
                    pa, pb = find(i), find(j)
                    if pa != pb:
                        p[pa] = pb
                        ans -= 1
        return ans
```

#### Java

```java
class Solution {
    private int[] p;

    public int findCircleNum(int[][] isConnected) {
        int n = isConnected.length;
        p = new int[n];
        for (int i = 0; i < n; ++i) {
            p[i] = i;
        }
        int ans = n;
        for (int i = 0; i < n; ++i) {
            for (int j = i + 1; j < n; ++j) {
                if (isConnected[i][j] == 1) {
                    int pa = find(i), pb = find(j);
                    if (pa != pb) {
                        p[pa] = pb;
                        --ans;
                    }
                }
            }
        }
        return ans;
    }

    private int find(int x) {
        if (p[x] != x) {
            p[x] = find(p[x]);
        }
        return p[x];
    }
}
```

#### C++

```cpp
class Solution {
public:
    int findCircleNum(vector<vector<int>>& isConnected) {
        int n = isConnected.size();
        vector<int> p(n);
        iota(p.begin(), p.end(), 0);
        function<int(int)> find = [&](int x) {
            return p[x] == x ? x : p[x] = find(p[x]);
        };
        int ans = n;
        for (int i = 0; i < n; ++i) {
            for (int j = i + 1; j < n; ++j) {
                if (isConnected[i][j]) {
                    int pa = find(i), pb = find(j);
                    if (pa != pb) {
                        p[pa] = pb;
                        --ans;
                    }
                }
            }
        }
        return ans;
    }
};
```

#### Go

```go
func findCircleNum(isConnected [][]int) int {
	n := len(isConnected)
	p := make([]int, n)
	for i := range p {
		p[i] = i
	}
	var find func(int) int
	find = func(x int) int {
		if p[x] != x {
			p[x] = find(p[x])
		}
		return p[x]
	}
	ans := n
	for i := 0; i < n; i++ {
		for j := i + 1; j < n; j++ {
			if isConnected[i][j] == 1 {
				pa, pb := find(i), find(j)
				if pa != pb {
					p[pa] = pb
					ans--
				}
			}
		}
	}
	return ans
}
```

#### TypeScript

```ts
function findCircleNum(isConnected: number[][]): number {
    const n = isConnected.length;
    const p: number[] = Array.from({ length: n }, (_, i) => i);
    const find = (x: number): number => {
        if (p[x] !== x) {
            p[x] = find(p[x]);
        }
        return p[x];
    };
    let ans = n;
    for (let i = 0; i < n; ++i) {
        for (let j = i + 1; j < n; ++j) {
            if (isConnected[i][j]) {
                const pa = find(i), pb = find(j);
                if (pa !== pb) {
                    p[pa] = pb;
                    --ans;
                }
            }
        }
    }
    return ans;
}
```

---
