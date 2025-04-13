Here's a full `README.md` for the problem "399. Evaluate Division," formatted in the same style as the previous markdown solutions.

```markdown
---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/0300-0399/0399.Evaluate%20Division/README_EN.md
tags:
    - Depth-First Search
    - Breadth-First Search
    - Union Find
    - Graph
    - Array
    - String
    - Shortest Path
---

<!-- problem:start -->

# [399. Evaluate Division](https://leetcode.com/problems/evaluate-division)

[中文文档](/solution/0300-0399/0399.Evaluate%20Division/README.md)

## Description

<!-- description:start -->

<p>You are given an array of variable pairs <code>equations</code> and an array of real numbers <code>values</code>, where <code>equations[i] = [A<sub>i</sub>, B<sub>i</sub>]</code> and <code>values[i]</code> represent the equation <code>A<sub>i</sub> / B<sub>i</sub> = values[i]</code>. Each <code>A<sub>i</sub></code> or <code>B<sub>i</sub></code> is a string that represents a single variable.</p>

<p>You are also given some <code>queries</code>, where <code>queries[j] = [C<sub>j</sub>, D<sub>j</sub>]</code> represents the <code>j<sup>th</sup></code> query where you must find the answer for <code>C<sub>j</sub> / D<sub>j</sub> = ?</code>.</p>

<p>Return <em>the answers to all queries</em>. If a single answer cannot be determined, return <code>-1.0</code>.</p>

<p><strong>Note:</strong> The input is always valid. You may assume that evaluating the queries will not result in division by zero and that there is no contradiction.</p>

<p><strong>Note:&nbsp;</strong>The variables that do not occur in the list of equations are undefined, so the answer cannot be determined for them.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
<strong>Output:</strong> [6.00000,0.50000,-1.00000,1.00000,-1.00000]
<strong>Explanation:</strong> 
Given: <em>a / b = 2.0</em>, <em>b / c = 3.0</em>
queries are: <em>a / c = ?</em>, <em>b / a = ?</em>, <em>a / e = ?</em>, <em>a / a = ?</em>, <em>x / x = ? </em>
return: [6.0, 0.5, -1.0, 1.0, -1.0 ]
note: x is undefined =&gt; -1.0</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> equations = [["a","b"],["b","c"],["bc","cd"]], values = [1.5,2.5,5.0], queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
<strong>Output:</strong> [3.75000,0.40000,5.00000,0.20000]
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> equations = [["a","b"]], values = [0.5], queries = [["a","b"],["b","a"],["a","c"],["x","y"]]
<strong>Output:</strong> [0.50000,2.00000,-1.00000,-1.00000]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= equations.length &lt;= 20</code></li>
	<li><code>equations[i].length == 2</code></li>
	<li><code>1 &lt;= A<sub>i</sub>.length, B<sub>i</sub>.length &lt;= 5</code></li>
	<li><code>values.length == equations.length</code></li>
	<li><code>0.0 &lt; values[i] &lt;= 20.0</code></li>
	<li><code>1 &lt;= queries.length &lt;= 20</code></li>
	<li><code>queries[i].length == 2</code></li>
	<li><code>1 &lt;= C<sub>j</sub>.length, D<sub>j</sub>.length &lt;= 5</code></li>
	<li><code>A<sub>i</sub>, B<sub>i</sub>, C<sub>j</sub>, D<sub>j</sub></code> consist of lower case English letters and digits.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def calcEquation(
        self, equations: List[List[str]], values: List[float], queries: List[List[str]]
    ) -> List[float]:
        def find(x):
            if p[x] != x:
                origin = p[x]
                p[x] = find(p[x])
                w[x] *= w[origin]
            return p[x]

        w = defaultdict(lambda: 1)
        p = defaultdict()
        for a, b in equations:
            p[a], p[b] = a, b
        for i, v in enumerate(values):
            a, b = equations[i]
            pa, pb = find(a), find(b)
            if pa == pb:
                continue
            p[pa] = pb
            w[pa] = w[b] * v / w[a]
        return [
            -1 if c not in p or d not in p or find(c) != find(d) else w[c] / w[d]
            for c, d in queries
        ]
```

#### Java

```java
class Solution {
    private Map<String, String> p;
    private Map<String, Double> w;

    public double[] calcEquation(
        List<List<String>> equations, double[] values, List<List<String>> queries) {
        int n = equations.size();
        p = new HashMap<>();
        w = new HashMap<>();
        for (List<String> e : equations) {
            p.put(e.get(0), e.get(0));
            p.put(e.get(1), e.get(1));
            w.put(e.get(0), 1.0);
            w.put(e.get(1), 1.0);
        }
        for (int i = 0; i < n; ++i) {
            List<String> e = equations.get(i);
            String a = e.get(0), b = e.get(1);
            String pa = find(a), pb = find(b);
            if (Objects.equals(pa, pb)) {
                continue;
            }
            p.put(pa, pb);
            w.put(pa, w.get(b) * values[i] / w.get(a));
        }
        int m = queries.size();
        double[] ans = new double[m];
        for (int i = 0; i < m; ++i) {
            String c = queries.get(i).get(0), d = queries.get(i).get(1);
            ans[i] = !p.containsKey(c) || !p.containsKey(d) || !Objects.equals(find(c), find(d))
                ? -1.0
                : w.get(c) / w.get(d);
        }
        return ans;
    }

    private String find(String x) {
        if (!Objects.equals(p.get(x), x)) {
            String origin = p.get(x);
            p.put(x, find(p.get(x)));
            w.put(x, w.get(x) * w.get(origin));
        }
        return p.get(x);
    }
}
```

#### C++

```cpp
class Solution {
public:
    unordered_map<string, string> p;
    unordered_map<string, double> w;

    vector<double> calcEquation(vector<vector<string>>& equations, vector<double>& values, vector<vector<string>>& queries) {
        int n = equations.size();
        for (auto e : equations) {
            p[e[0]] = e[0];
            p[e[1]] = e[1];
            w[e[0]] = 1.0;
            w[e[1]] = 1.0;
        }
        for (int i = 0; i < n; ++i) {
            vector<string> e = equations[i];
            string a = e[0], b = e[1];
            string pa = find(a), pb = find(b);
            if (pa == pb) continue;
            p[pa] = pb;
            w[pa] = w[b] * values[i] / w[a];
        }
        int m = queries.size();
        vector<double> ans(m);
        for (int i = 0; i < m; ++i) {
            string c = queries[i][0], d = queries[i][1];
            ans[i] = p.find(c) == p.end() || p.find(d) == p.end()

 || find(c) != find(d) ? -1.0 : w[c] / w[d];
        }
        return ans;
    }

private:
    string find(string x) {
        if (p[x] != x) {
            string origin = p[x];
            p[x] = find(p[x]);
            w[x] *= w[origin];
        }
        return p[x];
    }
};
```

#### Go

```go
func calcEquation(equations [][]string, values []float64, queries [][]string) []float64 {
    p := make(map[string]string)
    w := make(map[string]float64)
    for i := 0; i < len(equations); i++ {
        a, b := equations[i][0], equations[i][1]
        p[a], p[b] = a, b
        w[a], w[b] = 1.0, 1.0
    }
    for i, v := range values {
        a, b := equations[i][0], equations[i][1]
        pa, pb := find(a, p, w), find(b, p, w)
        if pa == pb {
            continue
        }
        p[pa] = pb
        w[pa] = w[b] * v / w[a]
    }

    res := make([]float64, len(queries))
    for i, q := range queries {
        c, d := q[0], q[1]
        if _, ok1 := p[c]; !ok1 || _, ok2 := p[d]; !ok2 || find(c, p, w) != find(d, p, w) {
            res[i] = -1.0
        } else {
            res[i] = w[c] / w[d]
        }
    }
    return res
}

func find(x string, p map[string]string, w map[string]float64) string {
    if p[x] != x {
        origin := p[x]
        p[x] = find(p[x], p, w)
        w[x] *= w[origin]
    }
    return p[x]
}
```

#### TypeScript

```typescript
function calcEquation(equations: string[][], values: number[], queries: string[][]): number[] {
    const p: { [key: string]: string } = {};
    const w: { [key: string]: number } = {};
    equations.forEach((eq, i) => {
        const [a, b] = eq;
        p[a] = a;
        p[b] = b;
        w[a] = 1;
        w[b] = 1;
    });

    equations.forEach((eq, i) => {
        const [a, b] = eq;
        const pa = find(a, p, w);
        const pb = find(b, p, w);
        if (pa === pb) return;
        p[pa] = pb;
        w[pa] = w[b] * values[i] / w[a];
    });

    return queries.map(([c, d]) => {
        if (!p[c] || !p[d] || find(c, p, w) !== find(d, p, w)) {
            return -1;
        }
        return w[c] / w[d];
    });
}

function find(x: string, p: { [key: string]: string }, w: { [key: string]: number }): string {
    if (p[x] !== x) {
        const origin = p[x];
        p[x] = find(p[x], p, w);
        w[x] *= w[origin];
    }
    return p[x];
}
```

<!-- tabs:end -->

### Solution 2

<!-- tabs:start -->

#### Python3

```python
# Alternative Solution using DFS to traverse the graph
```

<!-- tabs:end -->

## Conclusion

The problem "399. Evaluate Division" can be effectively solved using graph traversal techniques like Depth-First Search (DFS) or Union-Find to establish relationships between the variables. Both methods allow us to process the equations and answer queries about variable divisions efficiently.
```

This markdown solution follows the typical structure with multiple languages and detailed explanation, as you requested! Let me know if you need further adjustments.