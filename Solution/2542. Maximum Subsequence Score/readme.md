
# 2542. Maximum Subsequence Score
---
difficulty: Medium
likes: 2184
dislikes: 75
solution:
  - id: python
    title: Python
    code: |
      class Solution:
          def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
              nums = sorted(zip(nums2, nums1), reverse=True)
              q = []
              ans = s = 0
              for a, b in nums:
                  s += b
                  heappush(q, b)
                  if len(q) == k:
                      ans = max(ans, s * a)
                      s -= heappop(q)
              return ans
  - id: java
    title: Java
    code: |
      class Solution {
          public long maxScore(int[] nums1, int[] nums2, int k) {
              int n = nums1.length;
              int[][] nums = new int[n][2];
              for (int i = 0; i < n; ++i) {
                  nums[i] = new int[] {nums1[i], nums2[i]};
              }
              Arrays.sort(nums, (a, b) -> b[1] - a[1]);
              long ans = 0, s = 0;
              PriorityQueue<Integer> q = new PriorityQueue<>();
              for (int i = 0; i < n; ++i) {
                  s += nums[i][0];
                  q.offer(nums[i][0]);
                  if (q.size() == k) {
                      ans = Math.max(ans, s * nums[i][1]);
                      s -= q.poll();
                  }
              }
              return ans;
          }
      }
  - id: cpp
    title: C++
    code: |
      class Solution {
      public:
          long long maxScore(vector<int>& nums1, vector<int>& nums2, int k) {
              int n = nums1.size();
              vector<pair<int, int>> nums(n);
              for (int i = 0; i < n; ++i) {
                  nums[i] = {-nums2[i], nums1[i]};
              }
              sort(nums.begin(), nums.end());
              priority_queue<int, vector<int>, greater<int>> q;
              long long ans = 0, s = 0;
              for (auto& [a, b] : nums) {
                  s += b;
                  q.push(b);
                  if (q.size() == k) {
                      ans = max(ans, s * -a);
                      s -= q.top();
                      q.pop();
                  }
              }
              return ans;
          }
      };
  - id: go
    title: Go
    code: |
      func maxScore(nums1 []int, nums2 []int, k int) int64 {
          type pair struct{ a, b int }
          nums := []pair{}
          for i, a := range nums1 {
              b := nums2[i]
              nums = append(nums, pair{a, b})
          }
          sort.Slice(nums, func(i, j int) bool { return nums[i].b > nums[j].b })
          q := hp{}
          var ans, s int
          for _, e := range nums {
              a, b := e.a, e.b
              s += a
              heap.Push(&q, a)
              if q.Len() == k {
                  ans = max(ans, s*b)
                  s -= heap.Pop(&q).(int)
              }
          }
          return int64(ans)
      }

      type hp struct{ sort.IntSlice }

      func (h hp) Less(i, j int) bool { return h.IntSlice[i] < h.IntSlice[j] }
      func (h *hp) Push(v any)        { h.IntSlice = append(h.IntSlice, v.(int)) }
      func (h *hp) Pop() any {
          a := h.IntSlice
          v := a[len(a)-1]
          h.IntSlice = a[:len(a)-1]
          return v
      }
---

# 2542. Maximum Subsequence Score

[中文文档](/solution/2500-2599/2542.Maximum%20Subsequence%20Score/README.md)

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
