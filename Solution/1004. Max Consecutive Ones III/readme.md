# 1004. Max Consecutive Ones III

**Difficulty:** Medium  
**Tags:** Array, Binary Search, Prefix Sum, Sliding Window  
**Source:** [Leetcode](https://leetcode.com/problems/max-consecutive-ones-iii) | Weekly Contest 126 Q3

---

## Description

Given a binary array `nums` and an integer `k`, return *the maximum number of consecutive* `1`'s in the array if you can flip at most `k` `0`'s.

---

## Examples

**Example 1:**

```
Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2  
Output: 6  
Explanation: [1,1,1,0,0,1,1,1,1,1]  
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
```

**Example 2:**

```
Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3  
Output: 10  
Explanation: [1,1,1,1,1,1,1,1,1,1]
```

---

## Constraints

- `1 <= nums.length <= 10^5`
- `nums[i]` is either `0` or `1`.
- `0 <= k <= nums.length`

---

## Approach

### Sliding Window

We use a sliding window to maintain a subarray that contains at most `k` zeros. When the count of zeros exceeds `k`, we shrink the window from the left. The window size gives the count of maximum 1s after flipping at most `k` zeros.

- Time Complexity: O(n)
- Space Complexity: O(1)

---

## Solutions

### Python

```python
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = cnt = 0
        for r in range(len(nums)):
            cnt += nums[r] == 0
            if cnt > k:
                cnt -= nums[l] == 0
                l += 1
        return len(nums) - l
```

### Java

```java
class Solution {
    public int longestOnes(int[] nums, int k) {
        int l = 0, cnt = 0;
        for (int r = 0; r < nums.length; r++) {
            if (nums[r] == 0) cnt++;
            if (cnt > k) {
                if (nums[l++] == 0) cnt--;
            }
        }
        return nums.length - l;
    }
}
```

### C++

```cpp
class Solution {
public:
    int longestOnes(vector<int>& nums, int k) {
        int l = 0, cnt = 0;
        for (int r = 0; r < nums.size(); r++) {
            if (nums[r] == 0) cnt++;
            if (cnt > k) {
                if (nums[l++] == 0) cnt--;
            }
        }
        return nums.size() - l;
    }
};
```

### Go

```go
func longestOnes(nums []int, k int) int {
    l, cnt := 0, 0
    for r := 0; r < len(nums); r++ {
        if nums[r] == 0 {
            cnt++
        }
        if cnt > k {
            if nums[l] == 0 {
                cnt--
            }
            l++
        }
    }
    return len(nums) - l
}
```

### TypeScript

```ts
function longestOnes(nums: number[], k: number): number {
    let l = 0, cnt = 0;
    for (let r = 0; r < nums.length; r++) {
        if (nums[r] === 0) cnt++;
        if (cnt > k) {
            if (nums[l] === 0) cnt--;
            l++;
        }
    }
    return nums.length - l;
}
```

---
