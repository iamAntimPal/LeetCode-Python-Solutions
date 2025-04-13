# 2390. Removing Stars From a String

> Difficulty: Medium  
> Source: [LeetCode](https://leetcode.com/problems/removing-stars-from-a-string)  
> Tags: Stack, String, Simulation

## Description

You are given a string `s`, which contains stars `*`.

In one operation, you can:
- Choose a star in `s`.
- Remove the closest **non-star** character to its **left**, as well as remove the star itself.

Return *the string after all stars have been removed*.

**Note:**
- The input will be generated such that the operation is always possible.
- It can be shown that the resulting string will always be unique.

---

## Examples

### Example 1:
```
Input: s = "leet**cod*e"
Output: "lecoe"
Explanation: Performing the removals from left to right:
- The closest character to the 1st star is 't' -> "lee*cod*e"
- Then remove 'e' -> "lecod*e"
- Then remove 'd' -> "lecoe"
```

### Example 2:
```
Input: s = "erase*****"
Output: ""
Explanation: All characters are removed.
```

---

## Constraints

- `1 <= s.length <= 10⁵`
- `s` consists of lowercase English letters and stars `*`.
- The operation above can be performed on `s`.

---

## Solution

### Approach: Stack Simulation

We simulate the removal process using a stack:
- Iterate through the string `s`.
- Push characters onto a stack until you encounter a `*`.
- When a `*` is found, pop the top character from the stack (removing the left character).

### Time and Space Complexity

- **Time Complexity:** O(n)  
- **Space Complexity:** O(n) in the worst case (when no `*` are present)

---

## Code

### Python

```python
class Solution:
    def removeStars(self, s: str) -> str:
        ans = []
        for c in s:
            if c == '*':
                ans.pop()
            else:
                ans.append(c)
        return ''.join(ans)
```

### Java

```java
class Solution {
    public String removeStars(String s) {
        StringBuilder ans = new StringBuilder();
        for (char c : s.toCharArray()) {
            if (c == '*') {
                ans.deleteCharAt(ans.length() - 1);
            } else {
                ans.append(c);
            }
        }
        return ans.toString();
    }
}
```

### C++

```cpp
class Solution {
public:
    string removeStars(string s) {
        string ans;
        for (char c : s) {
            if (c == '*') {
                ans.pop_back();
            } else {
                ans.push_back(c);
            }
        }
        return ans;
    }
};
```

### Go

```go
func removeStars(s string) string {
	ans := []rune{}
	for _, c := range s {
		if c == '*' {
			ans = ans[:len(ans)-1]
		} else {
			ans = append(ans, c)
		}
	}
	return string(ans)
}
```

### TypeScript

```ts
function removeStars(s: string): string {
    const ans: string[] = [];
    for (const c of s) {
        if (c === '*') {
            ans.pop();
        } else {
            ans.push(c);
        }
    }
    return ans.join('');
}
```

### Rust

```rust
impl Solution {
    pub fn remove_stars(s: String) -> String {
        let mut ans = String::new();
        for c in s.chars() {
            if c == '*' {
                ans.pop();
            } else {
                ans.push(c);
            }
        }
        ans
    }
}
```

### PHP

```php
class Solution {
    function removeStars($s) {
        $stack = [];
        for ($i = 0; $i < strlen($s); $i++) {
            if ($s[$i] === '*') {
                array_pop($stack);
            } else {
                $stack[] = $s[$i];
            }
        }
        return implode('', $stack);
    }
}
```

