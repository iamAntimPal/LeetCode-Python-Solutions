
# [649. Dota2 Senate](https://leetcode.com/problems/dota2-senate)

> Medium  
> Greedy, Queue, String

## Description

In the world of Dota2, there are two parties: the Radiant and the Dire.

The Dota2 senate consists of senators coming from two parties. Now the Senate wants to decide on a change in the Dota2 game. The voting for this change is a round-based procedure. In each round, each senator can exercise **one** of the two rights:

- **Ban one senator's right:** A senator can make another senator lose all his rights in this and all the following rounds.
- **Announce the victory:** If this senator found the senators who still have rights to vote are all from the same party, he can announce the victory and decide on the change in the game.

Given a string `senate` representing each senator's party belonging. The character `'R'` and `'D'` represent the Radiant party and the Dire party. Then if there are `n` senators, the size of the given string will be `n`.

The round-based procedure starts from the first senator to the last senator in the given order. This procedure will last until the end of voting. All the senators who have lost their rights will be skipped during the procedure.

Suppose every senator is smart enough and will play the best strategy for his own party. Predict which party will finally announce the victory and change the Dota2 game. The output should be `"Radiant"` or `"Dire"`.

## Examples

### Example 1:

```
Input: senate = "RD"
Output: "Radiant"
Explanation:
The first senator comes from Radiant and he can just ban the next senator's right in round 1.
And the second senator can't exercise any rights anymore since his right has been banned.
And in round 2, the first senator can just announce the victory since he is the only guy in the senate who can vote.
```

### Example 2:

```
Input: senate = "RDD"
Output: "Dire"
Explanation:
The first senator comes from Radiant and he can just ban the next senator's right in round 1.
And the second senator can't exercise any rights anymore since his right has been banned.
And the third senator comes from Dire and he can ban the first senator's right in round 1.
And in round 2, the third senator can just announce the victory since he is the only guy in the senate who can vote.
```

## Constraints

- `n == senate.length`
- `1 <= n <= 10⁴`
- `senate[i]` is either `'R'` or `'D'`.

## Solutions

### Approach 1: Queue + Simulation

We use two queues to store the indices of Radiant (`'R'`) and Dire (`'D'`) senators. The index helps us maintain order and simulate the round-based voting system.

In each round:
- The senator with the smaller index acts first and bans the other.
- The acting senator goes to the back of the queue with their index increased by `n` to simulate the next round.

The process continues until one party's queue is empty.

**Time Complexity:** `O(n)`  
**Space Complexity:** `O(n)`

### Python

```python
from collections import deque

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        qr = deque()
        qd = deque()
        for i, c in enumerate(senate):
            if c == "R":
                qr.append(i)
            else:
                qd.append(i)
        n = len(senate)
        while qr and qd:
            if qr[0] < qd[0]:
                qr.append(qr[0] + n)
            else:
                qd.append(qd[0] + n)
            qr.popleft()
            qd.popleft()
        return "Radiant" if qr else "Dire"
```

### Java

```java
class Solution {
    public String predictPartyVictory(String senate) {
        int n = senate.length();
        Deque<Integer> qr = new ArrayDeque<>();
        Deque<Integer> qd = new ArrayDeque<>();
        for (int i = 0; i < n; ++i) {
            if (senate.charAt(i) == 'R') {
                qr.offer(i);
            } else {
                qd.offer(i);
            }
        }
        while (!qr.isEmpty() && !qd.isEmpty()) {
            if (qr.peek() < qd.peek()) {
                qr.offer(qr.poll() + n);
                qd.poll();
            } else {
                qd.offer(qd.poll() + n);
                qr.poll();
            }
        }
        return qr.isEmpty() ? "Dire" : "Radiant";
    }
}
```

### C++

```cpp
class Solution {
public:
    string predictPartyVictory(string senate) {
        int n = senate.size();
        queue<int> qr, qd;
        for (int i = 0; i < n; ++i) {
            if (senate[i] == 'R') {
                qr.push(i);
            } else {
                qd.push(i);
            }
        }
        while (!qr.empty() && !qd.empty()) {
            int r = qr.front(), d = qd.front();
            qr.pop();
            qd.pop();
            if (r < d) {
                qr.push(r + n);
            } else {
                qd.push(d + n);
            }
        }
        return qr.empty() ? "Dire" : "Radiant";
    }
};
```

### Go

```go
func predictPartyVictory(senate string) string {
    n := len(senate)
    qr := []int{}
    qd := []int{}
    for i, c := range senate {
        if c == 'R' {
            qr = append(qr, i)
        } else {
            qd = append(qd, i)
        }
    }
    for len(qr) > 0 && len(qd) > 0 {
        r, d := qr[0], qd[0]
        qr, qd = qr[1:], qd[1:]
        if r < d {
            qr = append(qr, r+n)
        } else {
            qd = append(qd, d+n)
        }
    }
    if len(qr) > 0 {
        return "Radiant"
    }
    return "Dire"
}
```

### TypeScript

```ts
function predictPartyVictory(senate: string): string {
    const n = senate.length;
    const qr: number[] = [];
    const qd: number[] = [];
    for (let i = 0; i < n; ++i) {
        if (senate[i] === 'R') {
            qr.push(i);
        } else {
            qd.push(i);
        }
    }
    while (qr.length && qd.length) {
        const r = qr.shift()!;
        const d = qd.shift()!;
        if (r < d) {
            qr.push(r + n);
        } else {
            qd.push(d + n);
        }
    }
    return qr.length ? 'Radiant' : 'Dire';
}
```

### Rust

```rust
impl Solution {
    pub fn predict_party_victory(senate: String) -> String {
        let mut qr = std::collections::VecDeque::new();
        let mut qd = std::collections::VecDeque::new();
        let n = senate.len();
        for (i, c) in senate.chars().enumerate() {
            if c == 'R' {
                qr.push_back(i);
            } else {
                qd.push_back(i);
            }
        }
        while !qr.is_empty() && !qd.is_empty() {
            let r = qr.pop_front().unwrap();
            let d = qd.pop_front().unwrap();
            if r < d {
                qr.push_back(r + n);
            } else {
                qd.push_back(d + n);
            }
        }
        if qr.is_empty() {
            "Dire".to_string()
        } else {
            "Radiant".to_string()
        }
    }
}
```
