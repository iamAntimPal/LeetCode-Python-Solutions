Here’s the `README.md` LeetCode-style markdown for **643. Maximum Average Subarray I**:

---

# 643. Maximum Average Subarray I

**Difficulty:** Easy  
**Tags:** Array, Sliding Window  
**Source:** [LeetCode](https://leetcode.com/problems/maximum-average-subarray-i)  

## Description

You are given an integer array `nums` consisting of `n` elements, and an integer `k`.

Find a contiguous subarray whose **length is equal to** `k` that has the maximum average value and return *this value*. Any answer with a calculation error less than `10⁻⁵` will be accepted.

### Example 1:
```
Input: nums = [1,12,-5,-6,50,3], k = 4  
Output: 12.75000  
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
```

### Example 2:
```
Input: nums = [5], k = 1  
Output: 5.00000
```

### Constraints:
- `n == nums.length`
- `1 <= k <= n <= 10⁵`
- `-10⁴ <= nums[i] <= 10⁴`

---

## Solution Explanation

We use a **sliding window** approach of size `k` to compute the sum of every contiguous subarray of length `k`. We update the maximum sum during this traversal and finally return `max_sum / k`.

- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

---

## Solutions

### Python3
```python
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        ans = s = sum(nums[:k])
        for i in range(k, len(nums)):
            s += nums[i] - nums[i - k]
            ans = max(ans, s)
        return ans / k
```

### Java
```java
class Solution {
    public double findMaxAverage(int[] nums, int k) {
        int s = 0;
        for (int i = 0; i < k; ++i) {
            s += nums[i];
        }
        int ans = s;
        for (int i = k; i < nums.length; ++i) {
            s += nums[i] - nums[i - k];
            ans = Math.max(ans, s);
        }
        return ans * 1.0 / k;
    }
}
```

### C++
```cpp
class Solution {
public:
    double findMaxAverage(vector<int>& nums, int k) {
        int s = accumulate(nums.begin(), nums.begin() + k, 0);
        int ans = s;
        for (int i = k; i < nums.size(); ++i) {
            s += nums[i] - nums[i - k];
            ans = max(ans, s);
        }
        return static_cast<double>(ans) / k;
    }
};
```

### Go
```go
func findMaxAverage(nums []int, k int) float64 {
	s := 0
	for _, x := range nums[:k] {
		s += x
	}
	ans := s
	for i := k; i < len(nums); i++ {
		s += nums[i] - nums[i-k]
		ans = max(ans, s)
	}
	return float64(ans) / float64(k)
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}
```

### TypeScript
```ts
function findMaxAverage(nums: number[], k: number): number {
    let s = 0;
    for (let i = 0; i < k; ++i) {
        s += nums[i];
    }
    let ans = s;
    for (let i = k; i < nums.length; ++i) {
        s += nums[i] - nums[i - k];
        ans = Math.max(ans, s);
    }
    return ans / k;
}
```

### Rust
```rust
impl Solution {
    pub fn find_max_average(nums: Vec<i32>, k: i32) -> f64 {
        let k = k as usize;
        let n = nums.len();
        let mut s = nums.iter().take(k).sum::<i32>();
        let mut ans = s;
        for i in k..n {
            s += nums[i] - nums[i - k];
            ans = ans.max(s);
        }
        f64::from(ans) / f64::from(k as i32)
    }
}
```

### PHP
```php
class Solution {
    /**
     * @param Integer[] $nums
     * @param Integer $k
     * @return Float
     */
    function findMaxAverage($nums, $k) {
        $s = 0;
        for ($i = 0; $i < $k; $i++) {
            $s += $nums[$i];
        }
        $ans = $s;
        for ($j = $k; $j < count($nums); $j++) {
            $s = $s - $nums[$j - $k] + $nums[$j];
            $ans = max($ans, $s);
        }
        return $ans / $k;
    }
}
```

