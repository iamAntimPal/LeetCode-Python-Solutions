
# 1207. Unique Number of Occurrences

> Difficulty: Easy  
> Tags: Array, Hash Table  
> Source: Weekly Contest 156 Q1

## Problem

Given an array of integers `arr`, return `true` if the number of occurrences of each value in the array is **unique**, or `false` otherwise.

### Example 1:

```
Input: arr = [1,2,2,1,1,3]
Output: true
Explanation: The value 1 has 3 occurrences, 2 has 2, and 3 has 1. No two values have the same number of occurrences.
```

### Example 2:

```
Input: arr = [1,2]
Output: false
```

### Example 3:

```
Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
Output: true
```

## Constraints

- `1 <= arr.length <= 1000`
- `-1000 <= arr[i] <= 1000`

---

## Approach

The solution involves two main steps:
1. Count the frequency of each element using a hash table.
2. Check if the frequencies are unique by storing them in another hash table (or set). If there are any repeated frequencies, return `false`, otherwise return `true`.

- **Time Complexity:** O(n), where `n` is the length of the array.
- **Space Complexity:** O(n), for storing the frequency counts.

---

## Solutions

### Python

```python
from collections import Counter

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        cnt = Counter(arr)
        return len(set(cnt.values())) == len(cnt)
```

### Java

```java
import java.util.*;

class Solution {
    public boolean uniqueOccurrences(int[] arr) {
        Map<Integer, Integer> cnt = new HashMap<>();
        for (int x : arr) {
            cnt.merge(x, 1, Integer::sum);
        }
        return new HashSet<>(cnt.values()).size() == cnt.size();
    }
}
```

### C++

```cpp
#include <unordered_map>
#include <unordered_set>
#include <vector>
using namespace std;

class Solution {
public:
    bool uniqueOccurrences(vector<int>& arr) {
        unordered_map<int, int> cnt;
        for (int& x : arr) {
            ++cnt[x];
        }
        unordered_set<int> vis;
        for (auto& [_, v] : cnt) {
            if (vis.count(v)) {
                return false;
            }
            vis.insert(v);
        }
        return true;
    }
};
```

### Go

```go
func uniqueOccurrences(arr []int) bool {
	cnt := map[int]int{}
	for _, x := range arr {
		cnt[x]++
	}
	vis := map[int]bool{}
	for _, v := range cnt {
		if vis[v] {
			return false
		}
		vis[v] = true
	}
	return true
}
```

### TypeScript

```ts
function uniqueOccurrences(arr: number[]): boolean {
    const cnt: Map<number, number> = new Map();
    for (const x of arr) {
        cnt.set(x, (cnt.get(x) || 0) + 1);
    }
    return cnt.size === new Set(cnt.values()).size;
}
```
