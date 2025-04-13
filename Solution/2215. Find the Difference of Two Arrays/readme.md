# 2215. Find the Difference of Two Arrays

> Difficulty: Easy  
> Tags: Array, Hash Table  
> Source: Weekly Contest 286 Q1

## Problem

Given two **0-indexed** integer arrays `nums1` and `nums2`, return a list `answer` of size `2` where:

- `answer[0]` is a list of all **distinct** integers in `nums1` which are **not** present in `nums2`.
- `answer[1]` is a list of all **distinct** integers in `nums2` which are **not** present in `nums1`.

Return the integers in **any** order.

### Example 1:

```
Input: nums1 = [1,2,3], nums2 = [2,4,6]
Output: [[1,3],[4,6]]
Explanation: 
- 1 and 3 are only in nums1.
- 4 and 6 are only in nums2.
```

### Example 2:

```
Input: nums1 = [1,2,3,3], nums2 = [1,1,2,2]
Output: [[3],[]]
Explanation: 
- 3 is only in nums1.
- Every element in nums2 is also in nums1.
```

## Constraints

- `1 <= nums1.length, nums2.length <= 1000`
- `-1000 <= nums1[i], nums2[i] <= 1000`

---

## Approach

We use sets to store the distinct elements from each array. Then compute the differences:

- `set(nums1) - set(nums2)` gives all elements in `nums1` not in `nums2`
- `set(nums2) - set(nums1)` gives all elements in `nums2` not in `nums1`

This approach ensures we only consider unique values and runs efficiently.

- **Time Complexity:** O(n), where n is the length of the input arrays.
- **Space Complexity:** O(n), due to set storage.

---

## Solutions

### Python

```python
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        s1, s2 = set(nums1), set(nums2)
        return [list(s1 - s2), list(s2 - s1)]
```

### Java

```java
class Solution {
    public List<List<Integer>> findDifference(int[] nums1, int[] nums2) {
        Set<Integer> s1 = new HashSet<>();
        Set<Integer> s2 = new HashSet<>();
        for (int n : nums1) s1.add(n);
        for (int n : nums2) s2.add(n);

        List<Integer> res1 = new ArrayList<>();
        for (int n : s1) if (!s2.contains(n)) res1.add(n);

        List<Integer> res2 = new ArrayList<>();
        for (int n : s2) if (!s1.contains(n)) res2.add(n);

        return Arrays.asList(res1, res2);
    }
}
```

### C++

```cpp
class Solution {
public:
    vector<vector<int>> findDifference(vector<int>& nums1, vector<int>& nums2) {
        unordered_set<int> s1(nums1.begin(), nums1.end());
        unordered_set<int> s2(nums2.begin(), nums2.end());
        vector<int> res1, res2;

        for (int n : s1)
            if (!s2.count(n)) res1.push_back(n);

        for (int n : s2)
            if (!s1.count(n)) res2.push_back(n);

        return {res1, res2};
    }
};
```

### JavaScript

```js
var findDifference = function(nums1, nums2) {
    const set1 = new Set(nums1);
    const set2 = new Set(nums2);

    const res1 = [...set1].filter(x => !set2.has(x));
    const res2 = [...set2].filter(x => !set1.has(x));

    return [res1, res2];
};
```

### Go

```go
func findDifference(nums1 []int, nums2 []int) [][]int {
    s1 := make(map[int]bool)
    s2 := make(map[int]bool)

    for _, n := range nums1 {
        s1[n] = true
    }
    for _, n := range nums2 {
        s2[n] = true
    }

    var res1, res2 []int
    for n := range s1 {
        if !s2[n] {
            res1 = append(res1, n)
        }
    }
    for n := range s2 {
        if !s1[n] {
            res2 = append(res2, n)
        }
    }
    return [][]int{res1, res2}
}
```

### Rust

```rust
use std::collections::HashSet;
impl Solution {
    pub fn find_difference(nums1: Vec<i32>, nums2: Vec<i32>) -> Vec<Vec<i32>> {
        let s1: HashSet<_> = nums1.iter().cloned().collect();
        let s2: HashSet<_> = nums2.iter().cloned().collect();

        let res1: Vec<i32> = s1.difference(&s2).cloned().collect();
        let res2: Vec<i32> = s2.difference(&s1).cloned().collect();

        vec![res1, res2]
    }
}
```

### PHP

```php
class Solution {
    function findDifference($nums1, $nums2) {
        $set1 = array_flip($nums1);
        $set2 = array_flip($nums2);

        $diff1 = array_diff_key($set1, $set2);
        $diff2 = array_diff_key($set2, $set1);

        return [array_keys($diff1), array_keys($diff2)];
    }
}
```
