
# 724. Find Pivot Index

## Problem Description

There is a list of integers `nums`. The **pivot index** is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index’s right.

If the index is on the left edge of the array, then the left sum is `0` because there are no elements to the left. This also applies to the right edge of the array.

Return the **leftmost** pivot index. If no such index exists, return `-1`.

### Example 1:

```
Input: nums = [1,7,3,6,5,6]
Output: 3
Explanation:
The pivot index is 3.
Left sum = 1 + 7 + 3 = 11
Right sum = 5 + 6 = 11
```

### Example 2:

```
Input: nums = [1,2,3]
Output: -1
Explanation:
There is no index that satisfies the conditions in the problem statement.
```

### Example 3:

```
Input: nums = [2,1,-1]
Output: 0
Explanation:
Left sum = 0, Right sum = 1 + (-1) = 0
```

## Constraints

- `1 <= nums.length <= 10^4`
- `-1000 <= nums[i] <= 1000`

**Note:** This problem is the same as [1991. Find the Middle Index in Array](https://leetcode.com/problems/find-the-middle-index-in-array/).

---

## Explanation

To solve the problem efficiently, we use the **prefix sum** technique:

- Compute the total sum of the array.
- As we iterate through each index `i`, we subtract the current value from the total to get the "right sum".
- If at any point the left sum equals the right sum, return the current index as the pivot.
- Update the left sum by adding the current element for the next iteration.

Time complexity: `O(n)`  
Space complexity: `O(1)`

---

## Solutions

### Python

```python
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left, right = 0, sum(nums)
        for i, x in enumerate(nums):
            right -= x
            if left == right:
                return i
            left += x
        return -1
```

### Java

```java
class Solution {
    public int pivotIndex(int[] nums) {
        int left = 0, right = Arrays.stream(nums).sum();
        for (int i = 0; i < nums.length; ++i) {
            right -= nums[i];
            if (left == right) return i;
            left += nums[i];
        }
        return -1;
    }
}
```

### C++

```cpp
class Solution {
public:
    int pivotIndex(vector<int>& nums) {
        int left = 0, right = accumulate(nums.begin(), nums.end(), 0);
        for (int i = 0; i < nums.size(); ++i) {
            right -= nums[i];
            if (left == right) return i;
            left += nums[i];
        }
        return -1;
    }
};
```

### JavaScript

```javascript
var pivotIndex = function(nums) {
    let left = 0, right = nums.reduce((a, b) => a + b, 0);
    for (let i = 0; i < nums.length; ++i) {
        right -= nums[i];
        if (left === right) return i;
        left += nums[i];
    }
    return -1;
};
```

### TypeScript

```ts
function pivotIndex(nums: number[]): number {
    let left = 0;
    let right = nums.reduce((sum, num) => sum + num, 0);
    for (let i = 0; i < nums.length; i++) {
        right -= nums[i];
        if (left === right) return i;
        left += nums[i];
    }
    return -1;
}
```

### Go

```go
func pivotIndex(nums []int) int {
    left, right := 0, 0
    for _, x := range nums {
        right += x
    }
    for i := 0; i < len(nums); i++ {
        right -= nums[i]
        if left == right {
            return i
        }
        left += nums[i]
    }
    return -1
}
```

### Rust

```rust
impl Solution {
    pub fn pivot_index(nums: Vec<i32>) -> i32 {
        let mut left = 0;
        let mut right: i32 = nums.iter().sum();
        for (i, &x) in nums.iter().enumerate() {
            right -= x;
            if left == right {
                return i as i32;
            }
            left += x;
        }
        -1
    }
}
```

### C

```c
int pivotIndex(int* nums, int numsSize){
    int total = 0, left = 0;
    for (int i = 0; i < numsSize; i++) {
        total += nums[i];
    }
    for (int i = 0; i < numsSize; i++) {
        if (left == total - left - nums[i]) return i;
        left += nums[i];
    }
    return -1;
}
```

