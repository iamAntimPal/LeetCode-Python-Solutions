
# 872. Leaf-Similar Trees

> **Difficulty**: Easy  
> **Tags**: Tree, Depth-First Search, Binary Tree  
> **Link**: [LeetCode Problem](https://leetcode.com/problems/leaf-similar-trees)

## Description

Consider all the leaves of a binary tree. From left to right order, the values of those leaves form a **leaf value sequence**.

Two binary trees are considered **leaf-similar** if their leaf value sequences are the same.

Return `true` if and only if the two given trees with head nodes `root1` and `root2` are leaf-similar.

### Example 1:

![example1](https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0800-0899/0872.Leaf-Similar%20Trees/images/leaf-similar-1.jpg)

```
Input: root1 = [3,5,1,6,2,9,8,null,null,7,4], root2 = [3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]
Output: true
```

### Example 2:

![example2](https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0800-0899/0872.Leaf-Similar%20Trees/images/leaf-similar-2.jpg)

```
Input: root1 = [1,2,3], root2 = [1,3,2]
Output: false
```

## Constraints

- The number of nodes in each tree will be in the range `[1, 200]`.
- Both of the given trees will have values in the range `[0, 200]`.

---

## Solutions

### Approach 1: DFS

We can perform a depth-first search (DFS) to collect the leaf values of each tree. If the leaf value sequences of both trees are the same, then the trees are leaf-similar.

**Time Complexity:** O(n)  
**Space Complexity:** O(n)

---

### Python3

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def dfs(root: Optional[TreeNode], nums: List[int]) -> None:
            if root.left == root.right:
                nums.append(root.val)
                return
            if root.left:
                dfs(root.left, nums)
            if root.right:
                dfs(root.right, nums)

        l1, l2 = [], []
        dfs(root1, l1)
        dfs(root2, l2)
        return l1 == l2
```

---

### Java

```java
class Solution {
    public boolean leafSimilar(TreeNode root1, TreeNode root2) {
        List<Integer> l1 = new ArrayList<>();
        List<Integer> l2 = new ArrayList<>();
        dfs(root1, l1);
        dfs(root2, l2);
        return l1.equals(l2);
    }

    private void dfs(TreeNode root, List<Integer> nums) {
        if (root.left == root.right) {
            nums.add(root.val);
            return;
        }
        if (root.left != null) dfs(root.left, nums);
        if (root.right != null) dfs(root.right, nums);
    }
}
```

---

### C++

```cpp
class Solution {
public:
    bool leafSimilar(TreeNode* root1, TreeNode* root2) {
        vector<int> l1, l2;
        dfs(root1, l1);
        dfs(root2, l2);
        return l1 == l2;
    }

    void dfs(TreeNode* root, vector<int>& nums) {
        if (root->left == root->right) {
            nums.push_back(root->val);
            return;
        }
        if (root->left) dfs(root->left, nums);
        if (root->right) dfs(root->right, nums);
    }
};
```

---

### Go

```go
func leafSimilar(root1 *TreeNode, root2 *TreeNode) bool {
	l1, l2 := []int{}, []int{}
	var dfs func(*TreeNode, *[]int)
	dfs = func(root *TreeNode, nums *[]int) {
		if root.Left == root.Right {
			*nums = append(*nums, root.Val)
			return
		}
		if root.Left != nil {
			dfs(root.Left, nums)
		}
		if root.Right != nil {
			dfs(root.Right, nums)
		}
	}
	dfs(root1, &l1)
	dfs(root2, &l2)
	return reflect.DeepEqual(l1, l2)
}
```

---

### Rust

```rust
use std::cell::RefCell;
use std::rc::Rc;

impl Solution {
    pub fn leaf_similar(
        root1: Option<Rc<RefCell<TreeNode>>>,
        root2: Option<Rc<RefCell<TreeNode>>>,
    ) -> bool {
        let mut l1 = Vec::new();
        let mut l2 = Vec::new();
        Self::dfs(&root1, &mut l1);
        Self::dfs(&root2, &mut l2);
        l1 == l2
    }

    fn dfs(node: &Option<Rc<RefCell<TreeNode>>>, nums: &mut Vec<i32>) {
        if let Some(n) = node {
            let n = n.borrow();
            if n.left.is_none() && n.right.is_none() {
                nums.push(n.val);
                return;
            }
            if n.left.is_some() {
                Self::dfs(&n.left, nums);
            }
            if n.right.is_some() {
                Self::dfs(&n.right, nums);
            }
        }
    }
}
```

---

### JavaScript

```javascript
var leafSimilar = function (root1, root2) {
    const l1 = [];
    const l2 = [];
    const dfs = (root, nums) => {
        if (root.left === root.right) {
            nums.push(root.val);
            return;
        }
        if (root.left) dfs(root.left, nums);
        if (root.right) dfs(root.right, nums);
    };
    dfs(root1, l1);
    dfs(root2, l2);
    return l1.join(',') === l2.join(',');
};
```

---
