Sure! Here's the `README.md` for **1732. Find the Highest Altitude** in full LeetCode-style markdown format, including problem description, examples, constraints, explanation, and multi-language solutions.

---

# 1732. Find the Highest Altitude

## Description

There is a biker going on a road trip. The road trip consists of `n + 1` points at different altitudes. The biker starts his trip on point `0` with altitude equal to `0`.

You are given an integer array `gain` of length `n` where `gain[i]` is the **net gain in altitude** between points `i` and `i + 1`. Return _the **highest altitude** of a point_.

---

## Examples

**Example 1:**

```
Input: gain = [-5,1,5,0,-7]
Output: 1
Explanation: The altitudes are [0, -5, -4, 1, 1, -6]. The highest is 1.
```

**Example 2:**

```
Input: gain = [-4,-3,-2,-1,4,3,2]
Output: 0
Explanation: The altitudes are [0, -4, -7, -9, -10, -6, -3, -1]. The highest is 0.
```

---

## Constraints

- `n == gain.length`
- `1 <= n <= 100`
- `-100 <= gain[i] <= 100`

---

## Explanation

We are given the altitude gains from one point to the next. Since the initial altitude is 0, we can compute the actual altitudes at each step using a prefix sum.

Let `h0 = 0`. Then for each `i`, the altitude at point `i+1` is `h0 + gain[0] + gain[1] + ... + gain[i]`.

We just need to track the maximum altitude encountered while accumulating the gains.

---

## Solution

### Time Complexity

- O(n), where n is the length of the input array `gain`.

### Space Complexity

- O(1), constant space used.

---

## Code

### Python

```python
from itertools import accumulate

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        return max(accumulate(gain, initial=0))
```

### Java

```java
class Solution {
    public int largestAltitude(int[] gain) {
        int ans = 0, h = 0;
        for (int v : gain) {
            h += v;
            ans = Math.max(ans, h);
        }
        return ans;
    }
}
```

### C++

```cpp
class Solution {
public:
    int largestAltitude(vector<int>& gain) {
        int ans = 0, h = 0;
        for (int v : gain) {
            h += v;
            ans = max(ans, h);
        }
        return ans;
    }
};
```

### JavaScript

```javascript
/**
 * @param {number[]} gain
 * @return {number}
 */
var largestAltitude = function(gain) {
    let maxAlt = 0, current = 0;
    for (let g of gain) {
        current += g;
        maxAlt = Math.max(maxAlt, current);
    }
    return maxAlt;
};
```

### Go

```go
func largestAltitude(gain []int) int {
    maxAlt, h := 0, 0
    for _, v := range gain {
        h += v
        if h > maxAlt {
            maxAlt = h
        }
    }
    return maxAlt
}
```

### Rust

```rust
impl Solution {
    pub fn largest_altitude(gain: Vec<i32>) -> i32 {
        let mut max_alt = 0;
        let mut current = 0;
        for g in gain {
            current += g;
            max_alt = max_alt.max(current);
        }
        max_alt
    }
}
```

### PHP

```php
class Solution {
    /**
     * @param Integer[] $gain
     * @return Integer
     */
    function largestAltitude($gain) {
        $max = 0;
        $current = 0;
        foreach ($gain as $g) {
            $current += $g;
            $max = max($max, $current);
        }
        return $max;
    }
}
```

### C

```c
int largestAltitude(int* gain, int gainSize) {
    int maxAlt = 0, h = 0;
    for (int i = 0; i < gainSize; ++i) {
        h += gain[i];
        if (h > maxAlt) {
            maxAlt = h;
        }
    }
    return maxAlt;
}
```

---

Let me know if you'd like a separate version of this as a downloadable `.md` file or need the solution in a different language!