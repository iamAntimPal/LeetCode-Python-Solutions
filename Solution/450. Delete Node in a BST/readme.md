

<!-- problem:start -->

# [450. Delete Node in a BST](https://leetcode.com/problems/delete-node-in-a-bst)


- **comments**: true
- **difficulty**: Medium
- **tags**:
  - Tree
  - Binary Search Tree
  - Binary Tree

## Description

<p>Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return <em>the <strong>root node reference</strong> (possibly updated) of the BST</em>.</p>

<p>The deletion can be divided into two stages:</p>
<ol>
  <li>Search for a node to remove.</li>
  <li>If the node is found, delete the node.</li>
</ol>

### Example 1:
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0400-0499/0450.Delete%20Node%20in%20a%20BST/images/del_node_1.jpg" style="width: 800px; height: 214px;" />

<pre>
<strong>Input:</strong> root = [5,3,6,2,4,null,7], key = 3
<strong>Output:</strong> [5,4,6,2,null,null,7]
<strong>Explanation:</strong> Given key to delete is 3. So we find the node with value 3 and delete it.
One valid answer is [5,4,6,2,null,null,7], shown in the above BST.
Another valid answer is [5,2,6,null,4,null,7].
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0400-0499/0450.Delete%20Node%20in%20a%20BST/images/del_node_supp.jpg" style="width: 350px; height: 255px;" />
</pre>

### Example 2:

<pre>
<strong>Input:</strong> root = [5,3,6,2,4,null,7], key = 0
<strong>Output:</strong> [5,3,6,2,4,null,7]
<strong>Explanation:</strong> The tree does not contain a node with value = 0.
</pre>

### Example 3:

<pre>
<strong>Input:</strong> root = [], key = 0
<strong>Output:</strong> []
</pre>

## Constraints:

- The number of nodes in the tree is in the range <code>[0, 10<sup>4</sup>]</code>.
- <code>-10<sup>5</sup> &lt;= Node.val &lt;= 10<sup>5</sup></code>
- Each node has a <strong>unique</strong> value.
- <code>root</code> is a valid binary search tree.
- <code>-10<sup>5</sup> &lt;= key &lt;= 10<sup>5</sup></code>

**Follow up:** Could you solve it with time complexity <code>O(height of tree)</code>?

<!-- problem:end -->

## Solutions

<!-- solution:start -->

### Solution 1

<!-- tabs:start -->

#### 🐍 Python3

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return None
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            # Find the inorder successor (smallest in the right subtree)
            temp = root.right
            while temp.left:
                temp = temp.left
            root.val = temp.val
            root.right = self.deleteNode(root.right, temp.val)
        return root
```

#### ☕ Java

```java
class Solution {
    public TreeNode deleteNode(TreeNode root, int key) {
        if (root == null) return null;
        if (key < root.val) {
            root.left = deleteNode(root.left, key);
        } else if (key > root.val) {
            root.right = deleteNode(root.right, key);
        } else {
            if (root.left == null) return root.right;
            if (root.right == null) return root.left;
            TreeNode minNode = getMin(root.right);
            root.val = minNode.val;
            root.right = deleteNode(root.right, root.val);
        }
        return root;
    }

    private TreeNode getMin(TreeNode node) {
        while (node.left != null) node = node.left;
        return node;
    }
}
```

#### 💻 C++

```cpp
class Solution {
public:
    TreeNode* deleteNode(TreeNode* root, int key) {
        if (!root) return nullptr;
        if (key < root->val) {
            root->left = deleteNode(root->left, key);
        } else if (key > root->val) {
            root->right = deleteNode(root->right, key);
        } else {
            if (!root->left) return root->right;
            if (!root->right) return root->left;
            TreeNode* minNode = getMin(root->right);
            root->val = minNode->val;
            root->right = deleteNode(root->right, root->val);
        }
        return root;
    }

    TreeNode* getMin(TreeNode* node) {
        while (node->left) node = node->left;
        return node;
    }
};
```

#### 🌀 Go

```go
func deleteNode(root *TreeNode, key int) *TreeNode {
    if root == nil {
        return nil
    }
    if key < root.Val {
        root.Left = deleteNode(root.Left, key)
    } else if key > root.Val {
        root.Right = deleteNode(root.Right, key)
    } else {
        if root.Left == nil {
            return root.Right
        }
        if root.Right == nil {
            return root.Left
        }
        minNode := getMin(root.Right)
        root.Val = minNode.Val
        root.Right = deleteNode(root.Right, root.Val)
    }
    return root
}

func getMin(node *TreeNode) *TreeNode {
    for node.Left != nil {
        node = node.Left
    }
    return node
}
```

#### 💠 TypeScript

```ts
function deleteNode(root: TreeNode | null, key: number): TreeNode | null {
    if (!root) return null;
    if (key < root.val) {
        root.left = deleteNode(root.left, key);
    } else if (key > root.val) {
        root.right = deleteNode(root.right, key);
    } else {
        if (!root.left) return root.right;
        if (!root.right) return root.left;
        const minNode = getMin(root.right);
        root.val = minNode.val;
        root.right = deleteNode(root.right, minNode.val);
    }
    return root;
}

function getMin(node: TreeNode): TreeNode {
    while (node.left) node = node.left;
    return node;
}
```

#### 🦀 Rust

```rust
use std::rc::Rc;
use std::cell::RefCell;

impl Solution {
    pub fn delete_node(root: Option<Rc<RefCell<TreeNode>>>, key: i32) -> Option<Rc<RefCell<TreeNode>>> {
        fn get_min(node: Rc<RefCell<TreeNode>>) -> Rc<RefCell<TreeNode>> {
            let mut cur = node;
            while cur.borrow().left.is_some() {
                cur = cur.borrow().left.clone().unwrap();
            }
            cur
        }

        match root {
            None => None,
            Some(node) => {
                let val = node.borrow().val;
                if key < val {
                    let left = Self::delete_node(node.borrow().left.clone(), key);
                    node.borrow_mut().left = left;
                    Some(node)
                } else if key > val {
                    let right = Self::delete_node(node.borrow().right.clone(), key);
                    node.borrow_mut().right = right;
                    Some(node)
                } else {
                    let left = node.borrow_mut().left.take();
                    let right = node.borrow_mut().right.take();
                    if left.is_none() {
                        return right;
                    }
                    if right.is_none() {
                        return left;
                    }
                    let min_node = get_min(right.clone().unwrap());
                    node.borrow_mut().val = min_node.borrow().val;
                    node.borrow_mut().right = Self::delete_node(right, node.borrow().val);
                    Some(node)
                }
            }
        }
    }
}
```

<!-- tabs:end -->

<!-- solution:end -->