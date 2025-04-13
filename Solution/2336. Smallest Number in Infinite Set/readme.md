Sure! Here's the complete LeetCode-style `README.md` for **2336. Smallest Number in Infinite Set**, following the style you're using (e.g., from the `doocs/leetcode` GitHub repo).

---

```markdown
# 2336. Smallest Number in Infinite Set

## Description

You have a set which contains all positive integers `[1, 2, 3, 4, 5, ...]`.

Implement the `SmallestInfiniteSet` class:

- `SmallestInfiniteSet()` Initializes the `SmallestInfiniteSet` object to contain all positive integers.
- `int popSmallest()` Removes and returns the smallest integer contained in the infinite set.
- `void addBack(int num)` Adds a positive integer `num` back into the infinite set, if it is not already in the infinite set.

### Example 1:

```
Input
["SmallestInfiniteSet", "addBack", "popSmallest", "popSmallest", "popSmallest", "addBack", "popSmallest", "popSmallest", "popSmallest"]
[[], [2], [], [], [], [1], [], [], []]
Output
[null, null, 1, 2, 3, null, 1, 4, 5]
```

**Explanation**

```python
SmallestInfiniteSet smallestInfiniteSet = new SmallestInfiniteSet();
smallestInfiniteSet.addBack(2);    # 2 is already in the set, so no change is made.
smallestInfiniteSet.popSmallest(); # return 1, and remove it from the set
smallestInfiniteSet.popSmallest(); # return 2, and remove it from the set
smallestInfiniteSet.popSmallest(); # return 3, and remove it from the set
smallestInfiniteSet.addBack(1);    # 1 is added back to the set
smallestInfiniteSet.popSmallest(); # return 1, and remove it from the set
smallestInfiniteSet.popSmallest(); # return 4, and remove it from the set
smallestInfiniteSet.popSmallest(); # return 5, and remove it from the set
```

## Constraints

- `1 <= num <= 1000`
- At most `1000` calls will be made in total to `popSmallest` and `addBack`.

---

## Solutions

### 🧠 Solution 1: Min Heap + Set

We simulate the infinite set using:

- A variable `current` which tracks the next number not yet popped (starting from 1).
- A min-heap `heap` for any added-back elements smaller than `current`.
- A set `in_heap` to avoid duplicate elements in the heap.

### Python

```python
import heapq

class SmallestInfiniteSet:
    def __init__(self):
        self.current = 1
        self.heap = []
        self.in_heap = set()

    def popSmallest(self) -> int:
        if self.heap:
            smallest = heapq.heappop(self.heap)
            self.in_heap.remove(smallest)
            return smallest
        else:
            res = self.current
            self.current += 1
            return res

    def addBack(self, num: int) -> None:
        if num < self.current and num not in self.in_heap:
            heapq.heappush(self.heap, num)
            self.in_heap.add(num)
```

### Java

```java
import java.util.*;

class SmallestInfiniteSet {
    private int current;
    private PriorityQueue<Integer> heap;
    private Set<Integer> set;

    public SmallestInfiniteSet() {
        current = 1;
        heap = new PriorityQueue<>();
        set = new HashSet<>();
    }

    public int popSmallest() {
        if (!heap.isEmpty()) {
            int smallest = heap.poll();
            set.remove(smallest);
            return smallest;
        }
        return current++;
    }

    public void addBack(int num) {
        if (num < current && !set.contains(num)) {
            heap.offer(num);
            set.add(num);
        }
    }
}
```

### C++

```cpp
#include <set>
#include <queue>
#include <unordered_set>

class SmallestInfiniteSet {
private:
    int current;
    priority_queue<int, vector<int>, greater<int>> heap;
    unordered_set<int> in_heap;

public:
    SmallestInfiniteSet() {
        current = 1;
    }

    int popSmallest() {
        if (!heap.empty()) {
            int res = heap.top();
            heap.pop();
            in_heap.erase(res);
            return res;
        }
        return current++;
    }

    void addBack(int num) {
        if (num < current && !in_heap.count(num)) {
            heap.push(num);
            in_heap.insert(num);
        }
    }
};
```

### Go

```go
import (
    "container/heap"
)

type SmallestInfiniteSet struct {
    current int
    pq      IntHeap
    inHeap  map[int]bool
}

func Constructor() SmallestInfiniteSet {
    return SmallestInfiniteSet{current: 1, inHeap: make(map[int]bool)}
}

func (this *SmallestInfiniteSet) PopSmallest() int {
    if len(this.pq) > 0 {
        smallest := heap.Pop(&this.pq).(int)
        delete(this.inHeap, smallest)
        return smallest
    }
    this.current++
    return this.current - 1
}

func (this *SmallestInfiniteSet) AddBack(num int) {
    if num < this.current && !this.inHeap[num] {
        heap.Push(&this.pq, num)
        this.inHeap[num] = true
    }
}

type IntHeap []int

func (h IntHeap) Len() int            { return len(h) }
func (h IntHeap) Less(i, j int) bool  { return h[i] < h[j] }
func (h IntHeap) Swap(i, j int)       { h[i], h[j] = h[j], h[i] }
func (h *IntHeap) Push(x interface{}) { *h = append(*h, x.(int)) }
func (h *IntHeap) Pop() interface{} {
    old := *h
    n := len(old)
    val := old[n-1]
    *h = old[:n-1]
    return val
}
```

### TypeScript

```ts
class SmallestInfiniteSet {
    private current = 1;
    private heap: number[] = [];
    private inHeap = new Set<number>();

    popSmallest(): number {
        if (this.heap.length > 0) {
            const smallest = this.heap.shift()!;
            this.inHeap.delete(smallest);
            return smallest;
        }
        return this.current++;
    }

    addBack(num: number): void {
        if (num < this.current && !this.inHeap.has(num)) {
            this.heap.push(num);
            this.heap.sort((a, b) => a - b);
            this.inHeap.add(num);
        }
    }
}
```

---

## Complexity Analysis

| Operation      | Time Complexity | Space Complexity |
|----------------|------------------|------------------|
| `popSmallest`  | O(log n)         | O(n)             |
| `addBack`      | O(log n)         | O(n)             |

---

## Tags

- 🔢 Heap (Priority Queue)
- 📊 Simulation
- 🧠 Design
```

