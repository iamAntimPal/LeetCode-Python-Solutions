
# 735. Asteroid Collision

> Difficulty: Medium  
> Tags: Stack, Array, Simulation  
> Source: [LeetCode](https://leetcode.com/problems/asteroid-collision)  
> Related Topics: Stack, Simulation

## Problem Description

We are given an array `asteroids` of integers representing asteroids in a row. The indices of the asteroids represent their relative position in space.

For each asteroid:
- The **absolute value** represents its size.
- The **sign** represents its direction (`positive` means right, `negative` means left).
- All asteroids move at the **same speed**.

We need to simulate their movement and collisions:
- When two asteroids collide, the smaller one **explodes**.
- If they are the same size, **both explode**.
- Asteroids moving in the same direction **never meet**.

Return the state of the asteroids after all collisions.

---

## Examples

### Example 1

**Input:**  
`asteroids = [5,10,-5]`  
**Output:**  
`[5,10]`  
**Explanation:**  
- `10` and `-5` collide → `10` survives  
- `5` and `10` do not collide  

### Example 2

**Input:**  
`asteroids = [8,-8]`  
**Output:**  
`[]`  
**Explanation:**  
- Both `8` and `-8` collide and explode  

### Example 3

**Input:**  
`asteroids = [10,2,-5]`  
**Output:**  
`[10]`  
**Explanation:**  
- `2` and `-5` collide → `-5` survives  
- `10` and `-5` collide → `10` survives  

---

## Constraints

- `2 <= asteroids.length <= 10⁴`
- `-1000 <= asteroids[i] <= 1000`
- `asteroids[i] != 0`

---

## Explanation

We can use a **stack** to simulate the collisions. While traversing the array:
- If the current asteroid is positive (`>0`), push it onto the stack.
- If it's negative (`<0`), pop from the stack until either:
  - The stack is empty,
  - The top of the stack is also negative, or
  - The top of the stack is larger (in absolute value) and survives.
- Equal magnitude causes both to explode.

---

## Solutions

### Python

```python
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stk = []
        for x in asteroids:
            if x > 0:
                stk.append(x)
            else:
                while stk and stk[-1] > 0 and stk[-1] < -x:
                    stk.pop()
                if stk and stk[-1] == -x:
                    stk.pop()
                elif not stk or stk[-1] < 0:
                    stk.append(x)
        return stk
```

### Java

```java
class Solution {
    public int[] asteroidCollision(int[] asteroids) {
        Deque<Integer> stk = new ArrayDeque<>();
        for (int x : asteroids) {
            if (x > 0) {
                stk.offerLast(x);
            } else {
                while (!stk.isEmpty() && stk.peekLast() > 0 && stk.peekLast() < -x) {
                    stk.pollLast();
                }
                if (!stk.isEmpty() && stk.peekLast() == -x) {
                    stk.pollLast();
                } else if (stk.isEmpty() || stk.peekLast() < 0) {
                    stk.offerLast(x);
                }
            }
        }
        return stk.stream().mapToInt(Integer::valueOf).toArray();
    }
}
```

### C++

```cpp
class Solution {
public:
    vector<int> asteroidCollision(vector<int>& asteroids) {
        vector<int> stk;
        for (int x : asteroids) {
            if (x > 0) {
                stk.push_back(x);
            } else {
                while (!stk.empty() && stk.back() > 0 && stk.back() < -x) {
                    stk.pop_back();
                }
                if (!stk.empty() && stk.back() == -x) {
                    stk.pop_back();
                } else if (stk.empty() || stk.back() < 0) {
                    stk.push_back(x);
                }
            }
        }
        return stk;
    }
};
```

### Go

```go
func asteroidCollision(asteroids []int) []int {
    var stk []int
    for _, x := range asteroids {
        if x > 0 {
            stk = append(stk, x)
        } else {
            for len(stk) > 0 && stk[len(stk)-1] > 0 && stk[len(stk)-1] < -x {
                stk = stk[:len(stk)-1]
            }
            if len(stk) > 0 && stk[len(stk)-1] == -x {
                stk = stk[:len(stk)-1]
            } else if len(stk) == 0 || stk[len(stk)-1] < 0 {
                stk = append(stk, x)
            }
        }
    }
    return stk
}
```

### TypeScript

```ts
function asteroidCollision(asteroids: number[]): number[] {
    const stk: number[] = [];
    for (const x of asteroids) {
        if (x > 0) {
            stk.push(x);
        } else {
            while (stk.length && stk.at(-1)! > 0 && stk.at(-1)! < -x) {
                stk.pop();
            }
            if (stk.length && stk.at(-1) === -x) {
                stk.pop();
            } else if (!stk.length || stk.at(-1)! < 0) {
                stk.push(x);
            }
        }
    }
    return stk;
}
```

### Rust

```rust
impl Solution {
    pub fn asteroid_collision(asteroids: Vec<i32>) -> Vec<i32> {
        let mut stk = Vec::new();
        for &x in &asteroids {
            if x > 0 {
                stk.push(x);
            } else {
                while let Some(&top) = stk.last() {
                    if top < 0 || top > -x {
                        break;
                    }
                    if top == -x {
                        stk.pop();
                        break;
                    }
                    stk.pop();
                }
                if stk.is_empty() || *stk.last().unwrap() < 0 {
                    stk.push(x);
                }
            }
        }
        stk
    }
}
```
