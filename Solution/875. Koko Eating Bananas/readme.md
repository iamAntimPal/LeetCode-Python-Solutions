
<!-- problem:start -->

# [33. Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array)


---
- **comments**: true
- **difficulty**: Medium
- **tags**:
  - Array
  - Binary Search
---

## Description

<!-- description:start -->

<p>There is an integer array <code>nums</code> sorted in ascending order (with <strong>distinct</strong> values), which is rotated at an unknown pivot index <code>k</code> (0 <= k < nums.length) such that the resulting array is <code>[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]</code> (0-indexed). For example, <code>[0,1,2,4,5,6,7]</code> might be rotated at pivot index <code>3</code> and become <code>[4,5,6,7,0,1,2]</code>.</p>

<p>Given the array <code>nums</code> after the rotation and an integer <code>target</code>, return the index of <code>target</code> if it is in <code>nums</code>, or <code>-1</code> if it is not in <code>nums</code>.</p>

<p>You must write an algorithm with <code>O(log n)</code> runtime complexity.</p>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Binary Search

Since the array is rotated, we can't directly apply the standard binary search. But we can still use binary search with some modifications by identifying which half of the array is properly sorted.

At each step:

- Check if the left half is sorted.
- If it is, check whether the target is within the left half.
- If not, search the right half.
- Repeat similarly if the right half is sorted.

This approach ensures that with each iteration, we eliminate half the array, maintaining the logarithmic complexity.

Time Complexity: $O(\log n)$  
Space Complexity: $O(1)$

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1
```

#### Java

```java
class Solution {
    public int search(int[] nums, int target) {
        int l = 0, r = nums.length - 1;
        while (l <= r) {
            int mid = (l + r) / 2;
            if (nums[mid] == target) return mid;
            if (nums[l] <= nums[mid]) {
                if (nums[l] <= target && target < nums[mid]) {
                    r = mid - 1;
                } else {
                    l = mid + 1;
                }
            } else {
                if (nums[mid] < target && target <= nums[r]) {
                    l = mid + 1;
                } else {
                    r = mid - 1;
                }
            }
        }
        return -1;
    }
}
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
```
