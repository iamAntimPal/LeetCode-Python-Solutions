

# 2542. Maximum Subsequence Score
---

## Description

You are given two **0-indexed** integer arrays `nums1` and `nums2` of equal length `n` and a positive integer `k`. You must choose a **subsequence** of indices from `nums1` of length `k`.

For chosen indices `i0`, `i1`, ..., `ik - 1`, your **score** is defined as:

- The sum of the selected elements from `nums1` multiplied with the **minimum** of the selected elements from `nums2`.
- Simply: `(nums1[i0] + nums1[i1] + ... + nums1[ik-1]) * min(nums2[i0], nums2[i1], ..., nums2[ik-1])`

Return the **maximum** possible score.

A **subsequence** of indices of an array is a set that can be derived from `{0, 1, ..., n-1}` by deleting some or no elements.

## Examples

**Example 1:**

```
Input: nums1 = [1,3,3,2], nums2 = [2,1,3,4], k = 3
Output: 12
Explanation: 
Possible scores:
- Indices [0,1,2] -> (1+3+3)*min(2,1,3) = 7
- Indices [0,1,3] -> (1+3+2)*min(2,1,4) = 6
- Indices [0,2,3] -> (1+3+2)*min(2,3,4) = 12
- Indices [1,2,3] -> (3+3+2)*min(1,3,4) = 8
Max score is 12.
```

**Example 2:**

```
Input: nums1 = [4,2,3,1,1], nums2 = [7,5,10,9,6], k = 1
Output: 30
Explanation: Choosing index 2 is optimal: 3*10 = 30.
```

## Constraints

- `n == nums1.length == nums2.length`
- `1 <= n <= 10⁵`
- `0 <= nums1[i], nums2[i] <= 10⁵`
- `1 <= k <= n`

## Solution

### Approach: Sorting + Min Heap

Sort the pairs `(nums2[i], nums1[i])` by `nums2[i]` in descending order. Use a min heap to keep track of the `k` largest `nums1` values encountered so far. At each step, calculate the potential score and update the answer.

- **Time Complexity:** O(n log n)
- **Space Complexity:** O(n)
```
