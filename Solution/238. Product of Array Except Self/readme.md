
# [238. Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self)


## Description

<!-- description:start -->

<p>Given an integer array <code>nums</code> of length <code>n</code>, return an array <code>answer</code> such that <code>answer[i]</code> is equal to the product of all the elements of <code>nums</code> except <code>nums[i]</code>.</p>

<p>The product of any prefix or suffix of <code>nums</code> is guaranteed to fit in a <strong>32-bit</strong> integer.</p>

<p>You must write an algorithm that runs in <code>O(n)</code> time and without using the division operation.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,2,3,4]
<strong>Output:</strong> [24,12,8,6]
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [-1,1,0,-3,3]
<strong>Output:</strong> [0,0,9,0,0]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>-30 &lt;= nums[i] &lt;= 30</code></li>
	<li>The product of any prefix or suffix of <code>nums</code> is guaranteed to fit in a <strong>32-bit</strong> integer.</li>
</ul>

<p><strong>Follow-up:</strong> Can you solve the problem in <code>O(1)</code> extra space complexity? (The output array <strong>does not count</strong> as extra space for space complexity analysis.)</p>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Prefix and Suffix Products

We first calculate the product of all elements to the left of each index and store it in the result array.  
Then, we iterate from the end to update each index by multiplying with the product of elements on the right.

Time Complexity: $O(n)$  
Space Complexity: $O(1)$ (excluding output array)

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        res = [1] * len(nums)
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        suffix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]
        return res
```

#### Java

```java
class Solution {
    public int[] productExceptSelf(int[] nums) {
        int len = nums.length;
        int[] res = new int[len];
        for (int i = 0, prefix = 1; i < len; i++) {
            res[i] = prefix;
            prefix *= nums[i];
        }
        for (int i = len - 1, suffix = 1; i >= 0; i--) {
            res[i] *= suffix;
            suffix *= nums[i];
        }
        return res;
    }
}
```

#### C++

```cpp
class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int n = nums.size();
        vector<int> res(n, 1);
        int prefix = 1, suffix = 1;
        for (int i = 0; i < n; i++) {
            res[i] = prefix;
            prefix *= nums[i];
        }
        for (int i = n - 1; i >= 0; i--) {
            res[i] *= suffix;
            suffix *= nums[i];
        }
        return res;
    }
};
```

#### Go

```go
func productExceptSelf(nums []int) []int {
    res := make([]int, len(nums))
    res[0] = 1
    for i := 1; i < len(nums); i++ {
        res[i] = res[i-1] * nums[i-1]
    }
    right := 1
    for i := len(nums) - 1; i >= 0; i-- {
        res[i] *= right
        right *= nums[i]
    }
    return res
}
```

#### TypeScript

```ts
function productExceptSelf(nums: number[]): number[] {
    const res = new Array(nums.length).fill(1);
    let prefix = 1;
    for (let i = 0; i < nums.length; i++) {
        res[i] = prefix;
        prefix *= nums[i];
    }
    let suffix = 1;
    for (let i = nums.length - 1; i >= 0; i--) {
        res[i] *= suffix;
        suffix *= nums[i];
    }
    return res;
}
```

#### Rust

```rust
impl Solution {
    pub fn product_except_self(nums: Vec<i32>) -> Vec<i32> {
        let mut res = vec![1; nums.len()];
        let mut prefix = 1;
        for i in 0..nums.len() {
            res[i] = prefix;
            prefix *= nums[i];
        }
        let mut suffix = 1;
        for i in (0..nums.len()).rev() {
            res[i] *= suffix;
            suffix *= nums[i];
        }
        res
    }
}
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
