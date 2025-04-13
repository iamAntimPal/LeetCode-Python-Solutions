- **comments**: true
- **difficulty**: Easy
- **tags**:
  - Tree
  - Binary Search Tree
  - Binary Tree
---

<!-- problem:start -->

# [700. Search in a Binary Search Tree](https://leetcode.com/problems/search-in-a-binary-search-tree)

## Description

<!-- description:start -->

You are given the `root` of a binary search tree (BST) and an integer `val`.

Find the node in the BST whose value equals `val` and return the subtree rooted with that node. If such a node does not exist, return `null`.

<!-- description:end -->

## Examples

<!-- examples:start -->

### Example 1:

![example1](https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0700-0799/0700.Search%20in%20a%20Binary%20Search%20Tree/images/tree1.jpg)

```
Input: root = [4,2,7,1,3], val = 2
Output: [2,1,3]
```

### Example 2:

![example2](https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0700-0799/0700.Search%20in%20a%20Binary%20Search%20Tree/images/tree2.jpg)

```
Input: root = [4,2,7,1,3], val = 5
Output: []
```

<!-- examples:end -->

## Constraints

- The number of nodes in the tree is in the range `[1, 5000]`.
- `1 <= Node.val <= 10⁷`
- `root` is a binary search tree.
- `1 <= val <= 10⁷`

## Solutions

<!-- solution:start -->

### Solution 1: Recursion

Since the tree is a binary search tree, we can utilize the BST property:

- If `val` < `root.val`, we search the left subtree.
- If `val` > `root.val`, we search the right subtree.
- If `val` == `root.val`, we return the node.

This approach has:

- Time Complexity: O(h), where `h` is the height of the tree.
- Space Complexity: O(h), due to recursive call stack.

<!-- tabs:start -->

### Python3

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None or root.val == val:
            return root
        return self.searchBST(root.left, val) if val < root.val else self.searchBST(root.right, val)
```

### Java

```java
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public TreeNode searchBST(TreeNode root, int val) {
        if (root == null || root.val == val) return root;
        return val < root.val ? searchBST(root.left, val) : searchBST(root.right, val);
    }
}
```

### C++

```cpp
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    TreeNode* searchBST(TreeNode* root, int val) {
        if (!root || root->val == val) return root;
        return val < root->val ? searchBST(root->left, val) : searchBST(root->right, val);
    }
};
```

### Go

```go
/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func searchBST(root *TreeNode, val int) *TreeNode {
    if root == nil || root.Val == val {
        return root
    }
    if val < root.Val {
        return searchBST(root.Left, val)
    }
    return searchBST(root.Right, val)
}
```

### TypeScript

```ts
/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     val: number
 *     left: TreeNode | null
 *     right: TreeNode | null
 *     constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.left = (left===undefined ? null : left)
 *         this.right = (right===undefined ? null : right)
 *     }
 * }
 */

function searchBST(root: TreeNode | null, val: number): TreeNode | null {
    if (root === null || root.val === val) {
        return root;
    }
    return val < root.val ? searchBST(root.left, val) : searchBST(root.right, val);
}
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
