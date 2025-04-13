

<!-- problem:start -->

# [394. Decode String](https://leetcode.com/problems/decode-string)


---
- **comments**: true
- **difficulty**: Medium

- **tags**:
    - Stack
    - Recursion
    - String
---

## Description

<!-- description:start -->

Given an encoded string, return its decoded string.

The encoding rule is: `k[encoded_string]`, where the `encoded_string` inside the square brackets is being repeated exactly `k` times. Note that `k` is guaranteed to be a positive integer.

You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc. Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, `k`.

The test cases are generated so that the length of the output will never exceed `10^5`.

&nbsp;

**Example 1:**
```
Input: s = "3[a]2[bc]"
Output: "aaabcbc"
```

**Example 2:**
```
Input: s = "3[a2[c]]"
Output: "accaccacc"
```

**Example 3:**
```
Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"
```

&nbsp;

**Constraints:**

- `1 <= s.length <= 30`
- `s` consists of lowercase English letters, digits, and square brackets `'[]'`.
- `s` is guaranteed to be a valid input.
- All the integers in `s` are in the range `[1, 300]`.

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Stack

We iterate through the string and process characters one by one:

- If it's a digit, we calculate the full number.
- If we encounter `'['`, we push the current number and partial result to the stack, then reset.
- If we encounter `']'`, we pop the last number and string from the stack and repeat the current string that many times, then append.
- Otherwise, we add the character to the current result.

Time complexity: O(n)  
Space complexity: O(n)

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def decodeString(self, s: str) -> str:
        s1, s2 = [], []
        num, res = 0, ''
        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)
            elif c == '[':
                s1.append(num)
                s2.append(res)
                num, res = 0, ''
            elif c == ']':
                res = s2.pop() + res * s1.pop()
            else:
                res += c
        return res
```

#### Java

```java
class Solution {
    public String decodeString(String s) {
        Deque<Integer> s1 = new ArrayDeque<>();
        Deque<String> s2 = new ArrayDeque<>();
        int num = 0;
        String res = "";
        for (char c : s.toCharArray()) {
            if (Character.isDigit(c)) {
                num = num * 10 + c - '0';
            } else if (c == '[') {
                s1.push(num);
                s2.push(res);
                num = 0;
                res = "";
            } else if (c == ']') {
                StringBuilder t = new StringBuilder();
                int times = s1.pop();
                for (int i = 0; i < times; ++i) {
                    t.append(res);
                }
                res = s2.pop() + t.toString();
            } else {
                res += c;
            }
        }
        return res;
    }
}
```

#### TypeScript

```ts
function decodeString(s: string): string {
    let ans = '';
    let stack = [];
    let count = 0;
    for (let ch of s) {
        if (/\d/.test(ch)) {
            count = count * 10 + Number(ch);
        } else if (ch === '[') {
            stack.push([ans, count]);
            ans = '';
            count = 0;
        } else if (ch === ']') {
            let [prev, num] = stack.pop();
            ans = prev + ans.repeat(num);
        } else {
            ans += ch;
        }
    }
    return ans;
}
```

#### C++

```cpp
class Solution {
public:
    string decodeString(string s) {
        stack<int> countStack;
        stack<string> strStack;
        string currentStr = "";
        int k = 0;
        for (char c : s) {
            if (isdigit(c)) {
                k = k * 10 + c - '0';
            } else if (c == '[') {
                countStack.push(k);
                strStack.push(currentStr);
                currentStr = "";
                k = 0;
            } else if (c == ']') {
                string temp = currentStr;
                currentStr = strStack.top();
                strStack.pop();
                int repeat = countStack.top();
                countStack.pop();
                while (repeat--) currentStr += temp;
            } else {
                currentStr += c;
            }
        }
        return currentStr;
    }
};
```

#### Go

```go
func decodeString(s string) string {
    stack := []string{}
    numStack := []int{}
    res := ""
    num := 0
    for _, c := range s {
        switch {
        case c >= '0' && c <= '9':
            num = num*10 + int(c-'0')
        case c == '[':
            numStack = append(numStack, num)
            stack = append(stack, res)
            res = ""
            num = 0
        case c == ']':
            n := numStack[len(numStack)-1]
            numStack = numStack[:len(numStack)-1]
            prev := stack[len(stack)-1]
            stack = stack[:len(stack)-1]
            res = prev + strings.Repeat(res, n)
        default:
            res += string(c)
        }
    }
    return res
}
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
