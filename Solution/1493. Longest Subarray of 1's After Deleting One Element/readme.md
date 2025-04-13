
# 1493. Longest Subarray of 1's After Deleting One Element

**Difficulty:** Medium  
**Tags:** Array, Dynamic Programming, Sliding Window  
**Source:** [Biweekly Contest 29 Q3](https://leetcode.com/contest/biweekly-contest-29/problems/longest-subarray-of-1s-after-deleting-one-element/)

---

## Problem

Given a binary array `nums`, you should delete one element from it.

Return *the size of the longest non-empty subarray containing only* `1`'s *in the resulting array*. Return `0` if there is no such subarray.

### Examples

#### Example 1:
```
Input: nums = [1,1,0,1]
Output: 3
Explanation: After deleting the number at index 2, the array becomes [1,1,1].
```

#### Example 2:
```
Input: nums = [0,1,1,1,0,1,1,0,1]
Output: 5
Explanation: Delete the 0 at index 4 to get [0,1,1,1,1,1,0,1], then the longest 1's subarray is [1,1,1,1,1].
```

#### Example 3:
```
Input: nums = [1,1,1]
Output: 2
Explanation: You must delete one element.
```

---

## Constraints

- `1 <= nums.length <= 10^5`
- `nums[i]` is either `0` or `1`.

---

## Explanation

You are allowed to delete exactly **one element**, and then find the **longest subarray of only 1's**. That means:
- You can consider the entire array as long as one element is deleted.
- The deleted element can be either a 0 or a 1.
- The result is the max length of continuous 1’s possible after removing one element.

---

## Solutions

### ✅ Solution 1: Prefix and Suffix Count Arrays

Use two arrays:
- `left[i]` — the number of consecutive 1's ending at `i-1`.
- `right[i]` — the number of consecutive 1's starting at `i`.

Loop over each possible delete point and take `left[i] + right[i + 1]` as the candidate.

**Time Complexity:** O(n)  
**Space Complexity:** O(n)

<details>
<summary>Python</summary>

```python
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        left = [0] * (n + 1)
        right = [0] * (n + 1)
        for i, x in enumerate(nums, 1):
            if x:
                left[i] = left[i - 1] + 1
        for i in range(n - 1, -1, -1):
            if nums[i]:
                right[i] = right[i + 1] + 1
        return max(left[i] + right[i + 1] for i in range(n))
```

</details>

---

### ✅ Solution 2: Sliding Window (Two Pointers)

We look for the longest window containing **at most one 0**. Once we find such a window, we take its size minus 1 (since one element must be deleted).

**Time Complexity:** O(n)  
**Space Complexity:** O(1)

<details>
<summary>Python</summary>

```python
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        ans = 0
        cnt = j = 0
        for i, x in enumerate(nums):
            cnt += x ^ 1
            while cnt > 1:
                cnt -= nums[j] ^ 1
                j += 1
            ans = max(ans, i - j)
        return ans
```

</details>

---

### ✅ Solution 3: Optimized Sliding Window

In the above solution, we shrink the window when needed. This version avoids shrinking the window too much by incrementing the left pointer only when `cnt > 1`.

**Time Complexity:** O(n)  
**Space Complexity:** O(1)

<details>
<summary>Python</summary>

```python
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        cnt = l = 0
        for x in nums:
            cnt += x ^ 1
            if cnt > 1:
                cnt -= nums[l] ^ 1
                l += 1
        return len(nums) - l - 1
```