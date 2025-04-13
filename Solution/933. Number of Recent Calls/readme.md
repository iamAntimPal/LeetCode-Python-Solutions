

# 933. Number of Recent Calls
---
- **difficulty**: Easy
- **title**: Number of Recent Calls
- **leetcode_id**: 933
- **tags**:
  - Design
  - Queue
  - Data Stream
---

## Description

You have a `RecentCounter` class which counts the number of recent requests within a certain time frame.

Implement the `RecentCounter` class:

- `RecentCounter()` Initializes the counter with zero recent requests.
- `int ping(int t)` Adds a new request at time `t`, where `t` represents some time in milliseconds, and returns the number of requests that has happened in the past `3000` milliseconds (including the new request). Specifically, return the number of requests that have happened in the inclusive range `[t - 3000, t]`.

It is **guaranteed** that every call to `ping` uses a strictly larger value of `t` than the previous call.

**Example:**

```
Input
["RecentCounter", "ping", "ping", "ping", "ping"]
[[], [1], [100], [3001], [3002]]
Output
[null, 1, 2, 3, 3]

Explanation
RecentCounter recentCounter = new RecentCounter();
recentCounter.ping(1);     // requests = [1], range is [-2999,1], return 1
recentCounter.ping(100);   // requests = [1, 100], range is [-2900,100], return 2
recentCounter.ping(3001);  // requests = [1, 100, 3001], range is [1,3001], return 3
recentCounter.ping(3002);  // requests = [100, 3001, 3002], range is [2,3002], return 3
```

**Constraints:**

- `1 <= t <= 10⁹`
- Each test case will call `ping` with strictly increasing values of `t`.
- At most `10⁴` calls will be made to `ping`.

## Solutions

### Solution 1: Queue

We keep a queue to store timestamps and remove any timestamps outside of the range `[t - 3000, t]`.

#### Python3

```python
from collections import deque

class RecentCounter:
    def __init__(self):
        self.q = deque()

    def ping(self, t: int) -> int:
        self.q.append(t)
        while self.q[0] < t - 3000:
            self.q.popleft()
        return len(self.q)
```

#### Java

```java
class RecentCounter {
    private Queue<Integer> q;

    public RecentCounter() {
        q = new LinkedList<>();
    }

    public int ping(int t) {
        q.offer(t);
        while (q.peek() < t - 3000) {
            q.poll();
        }
        return q.size();
    }
}
```

#### C++

```cpp
class RecentCounter {
public:
    queue<int> q;

    RecentCounter() {}

    int ping(int t) {
        q.push(t);
        while (q.front() < t - 3000) q.pop();
        return q.size();
    }
};
```

#### Go

```go
type RecentCounter struct {
	q []int
}

func Constructor() RecentCounter {
	return RecentCounter{[]int{}}
}

func (this *RecentCounter) Ping(t int) int {
	this.q = append(this.q, t)
	for this.q[0] < t-3000 {
		this.q = this.q[1:]
	}
	return len(this.q)
}
```

#### TypeScript

```ts
class RecentCounter {
    private queue: number[];

    constructor() {
        this.queue = [];
    }

    ping(t: number): number {
        this.queue.push(t);
        while (this.queue[0] < t - 3000) {
            this.queue.shift();
        }
        return this.queue.length;
    }
}
```

#### JavaScript

```js
var RecentCounter = function () {
    this.q = [];
};

RecentCounter.prototype.ping = function (t) {
    this.q.push(t);
    while (this.q[0] < t - 3000) {
        this.q.shift();
    }
    return this.q.length;
};
```

#### C#

```cs
public class RecentCounter {
    private Queue<int> q = new Queue<int>();

    public RecentCounter() {}

    public int Ping(int t) {
        q.Enqueue(t);
        while (q.Peek() < t - 3000) {
            q.Dequeue();
        }
        return q.Count;
    }
}
```

#### Rust

```rust
use std::collections::VecDeque;

struct RecentCounter {
    queue: VecDeque<i32>,
}

impl RecentCounter {
    fn new() -> Self {
        Self {
            queue: VecDeque::new(),
        }
    }

    fn ping(&mut self, t: i32) -> i32 {
        self.queue.push_back(t);
        while let Some(&v) = self.queue.front() {
            if v >= t - 3000 {
                break;
            }
            self.queue.pop_front();
        }
        self.queue.len() as i32
    }
}
```

---

### Solution 2: Binary Search

We use a list and binary search (via `bisect`) to find the count of requests in range.

#### Python3

```python
from bisect import bisect_left

class RecentCounter:
    def __init__(self):
        self.s = []

    def ping(self, t: int) -> int:
        self.s.append(t)
        return len(self.s) - bisect_left(self.s, t - 3000)
```

#### C++

```cpp
class RecentCounter {
public:
    vector<int> s;

    RecentCounter() {}

    int ping(int t) {
        s.push_back(t);
        return s.size() - (lower_bound(s.begin(), s.end(), t - 3000) - s.begin());
    }
};
```

#### Go

```go
type RecentCounter struct {
	s []int
}

func Constructor() RecentCounter {
	return RecentCounter{[]int{}}
}

func (this *RecentCounter) Ping(t int) int {
	this.s = append(this.s, t)
	search := func(x int) int {
		left, right := 0, len(this.s)
		for left < right {
			mid := (left + right) >> 1
			if this.s[mid] >= x {
				right = mid
			} else {
				left = mid + 1
			}
		}
		return left
	}
	return len(this.s) - search(t-3000)
}
```

```

