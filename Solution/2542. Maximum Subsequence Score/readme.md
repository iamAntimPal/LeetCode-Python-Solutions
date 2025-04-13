Here’s the full `README.md` in LeetCode-style markdown for **2336. Smallest Number in Infinite Set**, matching the format like in `doocs/leetcode`:

---

```markdown
---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/2300-2399/2336.Smallest%20Number%20in%20Infinite%20Set/README_EN.md
tags:
  - Design
  - Heap (Priority Queue)
---

<!-- problem:start -->

# [2336. Smallest Number in Infinite Set](https://leetcode.com/problems/smallest-number-in-infinite-set)

[中文文档](/solution/2300-2399/2336.Smallest%20Number%20in%20Infinite%20Set/README.md)

## Description

<p>You have a set that contains all positive integers: <code>[1, 2, 3, 4, 5, ...]</code>.</p>

<p>Implement the <code>SmallestInfiniteSet</code> class:</p>

<ul>
  <li><code>SmallestInfiniteSet()</code> Initializes the <code>SmallestInfiniteSet</code> object to contain all positive integers.</li>
  <li><code>int popSmallest()</code> Removes and returns the smallest integer contained in the infinite set.</li>
  <li><code>void addBack(int num)</code> Adds a positive integer <code>num</code> back into the infinite set if it is not already in the set.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong>
["SmallestInfiniteSet", "addBack", "popSmallest", "popSmallest", "popSmallest", "addBack", "popSmallest", "popSmallest", "popSmallest"]
[[], [2], [], [], [], [1], [], [], []]

<strong>Output:</strong>
[null, null, 1, 2, 3, null, 1, 4, 5]

<strong>Explanation:</strong>
SmallestInfiniteSet smallestInfiniteSet = new SmallestInfiniteSet();
smallestInfiniteSet.addBack(2);    // 2 is already in the set, so nothing happens
smallestInfiniteSet.popSmallest(); // return 1 and remove it from the set
smallestInfiniteSet.popSmallest(); // return 2 and remove it from the set
smallestInfiniteSet.popSmallest(); // return 3 and remove it from the set
smallestInfiniteSet.addBack(1);    // add 1 back into the set
smallestInfiniteSet.popSmallest(); // return 1 and remove it again
smallestInfiniteSet.popSmallest(); // return 4 and remove it from the set
smallestInfiniteSet.popSmallest(); // return 5 and remove it from the set
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
  <li><code>1 &le; num &le; 1000</code></li>
  <li>At most <code>1000</code> calls will be made in total to <code>popSmallest</code> and <code>addBack</code>.</li>
</ul>

<!-- problem:end -->

## Solutions

### Solution 1: Min Heap + Hash Set

We can simulate the infinite set with an integer pointer `current` initialized to 1, and a min heap to manage elements that are "added back" and are smaller than `current`. A hash set tracks what’s already in the heap to avoid duplicates.

Time Complexity:
- `popSmallest`: O(log n)
- `addBack`: O(log n)
- Space Complexity: O(n)

<!-- tabs:start -->

### Python3

```python
from heapq import heappush, heappop

class SmallestInfiniteSet:
    def __init__(self):
        self.current = 1
        self.heap = []
        self.set = set()

    def popSmallest(self) -> int:
        if self.heap:
            val = heappop(self.heap)
            self.set.remove(val)
            return val
        val = self.current
        self.current += 1
        return val

    def addBack(self, num: int) -> None:
        if num < self.current and num not in self.set:
            heappush(self.heap, num)
            self.set.add(num)
```

### Java

```java
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
            int val = heap.poll();
            set.remove(val);
            return val;
        }
        return current++;
    }

    public void addBack(int num) {
        if (num < current && set.add(num)) {
            heap.offer(num);
        }
    }
}
```

### C++

```cpp
class SmallestInfiniteSet {
private:
    int current = 1;
    priority_queue<int, vector<int>, greater<int>> heap;
    unordered_set<int> inHeap;

public:
    int popSmallest() {
        if (!heap.empty()) {
            int val = heap.top();
            heap.pop();
            inHeap.erase(val);
            return val;
        }
        return current++;
    }

    void addBack(int num) {
        if (num < current && !inHeap.count(num)) {
            heap.push(num);
            inHeap.insert(num);
        }
    }
};
```

### Go

```go
type SmallestInfiniteSet struct {
	current int
	heap    *IntHeap
	set     map[int]bool
}

func Constructor() SmallestInfiniteSet {
	h := &IntHeap{}
	heap.Init(h)
	return SmallestInfiniteSet{current: 1, heap: h, set: map[int]bool{}}
}

func (this *SmallestInfiniteSet) PopSmallest() int {
	if this.heap.Len() > 0 {
		val := heap.Pop(this.heap).(int)
		delete(this.set, val)
		return val
	}
	val := this.current
	this.current++
	return val
}

func (this *SmallestInfiniteSet) AddBack(num int) {
	if num < this.current && !this.set[num] {
		heap.Push(this.heap, num)
		this.set[num] = true
	}
}

type IntHeap []int

func (h IntHeap) Len() int           { return len(h) }
func (h IntHeap) Less(i, j int) bool { return h[i] < h[j] }
func (h IntHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }
func (h *IntHeap) Push(x interface{}) { *h = append(*h, x.(int)) }
func (h *IntHeap) Pop() interface{} {
	n := len(*h)
	val := (*h)[n-1]
	*h = (*h)[:n-1]
	return val
}
```

### TypeScript

```ts
class SmallestInfiniteSet {
    private current: number;
    private heap: number[];
    private set: Set<number>;

    constructor() {
        this.current = 1;
        this.heap = [];
        this.set = new Set();
    }

    popSmallest(): number {
        if (this.heap.length > 0) {
            const val = this.heap.shift()!;
            this.set.delete(val);
            return val;
        }
        return this.current++;
    }

    addBack(num: number): void {
        if (num < this.current && !this.set.has(num)) {
            this.set.add(num);
            this.heap.push(num);
            this.heap.sort((a, b) => a - b);
        }
    }
}
```

<!-- tabs:end -->
