Here's the full LeetCode-style `README.md` for **215. Kth Largest Element in an Array**, formatted exactly like the `doocs/leetcode` style:

---

# 215. Kth Largest Element in an Array

> Difficulty: Medium  
> Tag: `Array`, `Heap (Priority Queue)`, `Divide and Conquer`, `Quickselect`, `Sorting`

## Description

Given an integer array `nums` and an integer `k`, return the `k`th largest element in the array.

Note that it is the `k`th largest element in the sorted order, not the `k`th distinct element.

You must solve it in `O(n)` time complexity on average.

## Example

**Example 1:**

```
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
```

**Example 2:**

```
Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
```

## Constraints

- `1 <= k <= nums.length <= 10⁵`
- `-10⁴ <= nums[i] <= 10⁴`

---

## Solutions

### 🟦 Python

```python
import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return heapq.nlargest(k, nums)[-1]
```

### ☕ Java

```java
import java.util.PriorityQueue;

class Solution {
    public int findKthLargest(int[] nums, int k) {
        PriorityQueue<Integer> heap = new PriorityQueue<>();
        for (int num : nums) {
            heap.offer(num);
            if (heap.size() > k) {
                heap.poll();
            }
        }
        return heap.peek();
    }
}
```

### 💻 C++

```cpp
#include <queue>
#include <vector>
using namespace std;

class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        priority_queue<int, vector<int>, greater<int>> minHeap;
        for (int num : nums) {
            minHeap.push(num);
            if (minHeap.size() > k) {
                minHeap.pop();
            }
        }
        return minHeap.top();
    }
};
```

### 🐹 Go

```go
import "container/heap"

type IntHeap []int

func (h IntHeap) Len() int            { return len(h) }
func (h IntHeap) Less(i, j int) bool  { return h[i] < h[j] }
func (h IntHeap) Swap(i, j int)       { h[i], h[j] = h[j], h[i] }
func (h *IntHeap) Push(x any)         { *h = append(*h, x.(int)) }
func (h *IntHeap) Pop() (v any) {
	n := len(*h)
	*h, v = (*h)[:n-1], (*h)[n-1]
	return
}

func findKthLargest(nums []int, k int) int {
	h := &IntHeap{}
	for _, num := range nums {
		heap.Push(h, num)
		if h.Len() > k {
			heap.Pop(h)
		}
	}
	return (*h)[0]
}
```

### 🟨 TypeScript

```ts
function findKthLargest(nums: number[], k: number): number {
    const heap: number[] = [];

    for (let num of nums) {
        heap.push(num);
        heap.sort((a, b) => a - b);
        if (heap.length > k) heap.shift();
    }

    return heap[0];
}
```

### 🦀 Rust

```rust
use std::collections::BinaryHeap;
use std::cmp::Reverse;

impl Solution {
    pub fn find_kth_largest(nums: Vec<i32>, k: i32) -> i32 {
        let mut heap = BinaryHeap::new();
        for &num in &nums {
            heap.push(Reverse(num));
            if heap.len() > k as usize {
                heap.pop();
            }
        }
        heap.peek().unwrap().0
    }
}
```

---

Let me know if you'd like a version using Quickselect instead of heaps, or if you want to add performance comparisons.