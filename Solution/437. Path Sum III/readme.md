
# 437. Path Sum III
---
## Description

Given the `root` of a binary tree and an integer `targetSum`, return *the number of paths where the sum of the values along the path equals* `targetSum`.

The path does not need to start or end at the root or a leaf, but it must go downwards (i.e., traveling only from parent nodes to child nodes).

### Example 1:

![example1](https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0400-0499/0437.Path%20Sum%20III/images/pathsum3-1-tree.jpg)

```
Input: root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
Output: 3
Explanation: The paths that sum to 8 are shown.
```

### Example 2:

```
Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
Output: 3
```

### Constraints:

- The number of nodes in the tree is in the range `[0, 1000]`.
- `-10⁹ <= Node.val <= 10⁹`
- `-1000 <= targetSum <= 1000`

---

## Solutions

### Solution: Prefix Sum + DFS

We traverse the tree using depth-first search while maintaining a prefix sum and storing its frequency in a hash map. If at any point the difference between the current prefix sum and `targetSum` exists in the map, it means there is a path that sums up to the target.

Time complexity: `O(n)`  
Space complexity: `O(n)`  
Where `n` is the number of nodes in the binary tree.

---

### Python3

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import Counter

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def dfs(node, s):
            if not node:
                return 0
            s += node.val
            ans = cnt[s - targetSum]
            cnt[s] += 1
            ans += dfs(node.left, s)
            ans += dfs(node.right, s)
            cnt[s] -= 1
            return ans

        cnt = Counter({0: 1})
        return dfs(root, 0)
```

### Java

```java
class Solution {
    private Map<Long, Integer> cnt = new HashMap<>();
    private int targetSum;

    public int pathSum(TreeNode root, int targetSum) {
        cnt.put(0L, 1);
        this.targetSum = targetSum;
        return dfs(root, 0);
    }

    private int dfs(TreeNode node, long s) {
        if (node == null) return 0;
        s += node.val;
        int ans = cnt.getOrDefault(s - targetSum, 0);
        cnt.put(s, cnt.getOrDefault(s, 0) + 1);
        ans += dfs(node.left, s) + dfs(node.right, s);
        cnt.put(s, cnt.get(s) - 1);
        return ans;
    }
}
```

### C++

```cpp
class Solution {
public:
    int pathSum(TreeNode* root, int targetSum) {
        unordered_map<long long, int> cnt;
        cnt[0] = 1;
        return dfs(root, 0, targetSum, cnt);
    }

    int dfs(TreeNode* node, long long s, int targetSum, unordered_map<long long, int>& cnt) {
        if (!node) return 0;
        s += node->val;
        int ans = cnt[s - targetSum];
        cnt[s]++;
        ans += dfs(node->left, s, targetSum, cnt);
        ans += dfs(node->right, s, targetSum, cnt);
        cnt[s]--;
        return ans;
    }
};
```

### JavaScript

```js
var pathSum = function (root, targetSum) {
    const cnt = new Map();
    const dfs = (node, s) => {
        if (!node) return 0;
        s += node.val;
        let ans = cnt.get(s - targetSum) || 0;
        cnt.set(s, (cnt.get(s) || 0) + 1);
        ans += dfs(node.left, s) + dfs(node.right, s);
        cnt.set(s, cnt.get(s) - 1);
        return ans;
    };
    cnt.set(0, 1);
    return dfs(root, 0);
};
```

### TypeScript

```ts
function pathSum(root: TreeNode | null, targetSum: number): number {
    const cnt: Map<number, number> = new Map();
    const dfs = (node: TreeNode | null, s: number): number => {
        if (!node) return 0;
        s += node.val;
        let ans = cnt.get(s - targetSum) ?? 0;
        cnt.set(s, (cnt.get(s) ?? 0) + 1);
        ans += dfs(node.left, s) + dfs(node.right, s);
        cnt.set(s, (cnt.get(s) ?? 0) - 1);
        return ans;
    };
    cnt.set(0, 1);
    return dfs(root, 0);
}
```

### Go

```go
func pathSum(root *TreeNode, targetSum int) int {
	cnt := map[int]int{0: 1}
	var dfs func(*TreeNode, int) int
	dfs = func(node *TreeNode, s int) int {
		if node == nil {
			return 0
		}
		s += node.Val
		ans := cnt[s-targetSum]
		cnt[s]++
		ans += dfs(node.Left, s) + dfs(node.Right, s)
		cnt[s]--
		return ans
	}
	return dfs(root, 0)
}
```

### C#

```cs
public class Solution {
    public int PathSum(TreeNode root, int targetSum) {
        Dictionary<long, int> cnt = new Dictionary<long, int>();

        int Dfs(TreeNode node, long s) {
            if (node == null) return 0;
            s += node.val;
            int ans = cnt.GetValueOrDefault(s - targetSum, 0);
            cnt[s] = cnt.GetValueOrDefault(s, 0) + 1;
            ans += Dfs(node.left, s);
            ans += Dfs(node.right, s);
            cnt[s]--;
            return ans;
        }

        cnt[0] = 1;
        return Dfs(root, 0);
    }
}
```

### Rust

```rust
use std::rc::Rc;
use std::cell::RefCell;
use std::collections::HashMap;

impl Solution {
    pub fn path_sum(root: Option<Rc<RefCell<TreeNode>>>, target_sum: i32) -> i32 {
        let mut cnt = HashMap::new();
        cnt.insert(0, 1);

        fn dfs(node: Option<Rc<RefCell<TreeNode>>>, s: i64, target: i64, cnt: &mut HashMap<i64, i32>) -> i32 {
            if let Some(n) = node {
                let n = n.borrow();
                let s = s + n.val as i64;
                let ans = cnt.get(&(s - target)).copied().unwrap_or(0);
                *cnt.entry(s).or_insert(0) += 1;
                let ans = ans + dfs(n.left.clone(), s, target, cnt) + dfs(n.right.clone(), s, target, cnt);
                *cnt.get_mut(&s).unwrap() -= 1;
                ans
            } else {
                0
            }
        }

        dfs(root, 0, target_sum as i64, &mut cnt)
    }
}
```

---

**Tags:** Tree, Depth-First Search, Binary Tree  
**Difficulty:** Medium  
**Related Topics:** Prefix Sum, Recursion  
**Link:** [437. Path Sum III](https://leetcode.com/problems/path-sum-iii)
