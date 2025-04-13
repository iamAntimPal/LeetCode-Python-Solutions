

# 1679. Max Number of K-Sum Pairs

## Tags

- Array
- Hash Table
- Two Pointers
- Sorting

## Description

You are given an integer array `nums` and an integer `k`.

In one operation, you can pick two numbers from the array whose sum equals `k` and remove them from the array.

Return *the maximum number of operations* you can perform on the array.

### Example 1:
```
Input: nums = [1,2,3,4], k = 5
Output: 2
Explanation:
- Remove (1,4) -> nums = [2,3]
- Remove (2,3) -> nums = []
Total operations = 2
```

### Example 2:
```
Input: nums = [3,1,3,4,3], k = 6
Output: 1
Explanation:
- Remove (3,3) -> nums = [1,4,3]
Total operations = 1
```

## Constraints

- `1 <= nums.length <= 10^5`
- `1 <= nums[i] <= 10^9`
- `1 <= k <= 10^9`

---

## Solutions

### Solution 1: Two Pointers (After Sorting)

**Idea:**  
Sort the array and use two pointers from both ends. If the sum is `k`, count the operation and move both pointers inward. Otherwise, adjust the pointers based on the sum.

**Complexity:**  
- Time: O(n log n)  
- Space: O(1)

#### Python
```python
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        l, r = 0, len(nums) - 1
        count = 0
        while l < r:
            total = nums[l] + nums[r]
            if total == k:
                count += 1
                l += 1
                r -= 1
            elif total < k:
                l += 1
            else:
                r -= 1
        return count
```

#### Java
```java
class Solution {
    public int maxOperations(int[] nums, int k) {
        Arrays.sort(nums);
        int l = 0, r = nums.length - 1, count = 0;
        while (l < r) {
            int sum = nums[l] + nums[r];
            if (sum == k) {
                count++;
                l++;
                r--;
            } else if (sum < k) {
                l++;
            } else {
                r--;
            }
        }
        return count;
    }
}
```

---

### Solution 2: Hash Map (Frequency Counter)

**Idea:**  
Use a hash map to store how many times you've seen each number. For each `x`, if `k - x` exists in the map, it forms a valid pair.

**Complexity:**  
- Time: O(n)  
- Space: O(n)

#### Python
```python
from collections import Counter

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        counter = Counter()
        ops = 0
        for num in nums:
            if counter[k - num] > 0:
                counter[k - num] -= 1
                ops += 1
            else:
                counter[num] += 1
        return ops
```

#### Java
```java
class Solution {
    public int maxOperations(int[] nums, int k) {
        Map<Integer, Integer> map = new HashMap<>();
        int count = 0;
        for (int num : nums) {
            if (map.getOrDefault(k - num, 0) > 0) {
                map.put(k - num, map.get(k - num) - 1);
                count++;
            } else {
                map.put(num, map.getOrDefault(num, 0) + 1);
            }
        }
        return count;
    }
}
```

---



