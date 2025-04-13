<!-- problem:start -->

# [345. Reverse Vowels of a String](https://leetcode.com/problems/reverse-vowels-of-a-string)

## Description

<!-- description:start -->

<p>Given a string <code>s</code>, reverse only all the vowels in the string and return it.</p>

<p>The vowels are <code>&#39;a&#39;</code>, <code>&#39;e&#39;</code>, <code>&#39;i&#39;</code>, <code>&#39;o&#39;</code>, and <code>&#39;u&#39;</code>, and they can appear in both lower and upper cases, more than once.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = "IceCreAm"
<strong>Output:</strong> "AceCreIm"
<strong>Explanation:</strong> The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = "leetcode"
<strong>Output:</strong> "leotcede"
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 3 * 10<sup>5</sup></code></li>
	<li><code>s</code> consists of <strong>printable ASCII</strong> characters.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Two Pointers

We can use two pointers $i$ and $j$, initially pointing to the start and end of the string respectively.

In each iteration, we move the pointers inward until both $i$ and $j$ point to vowels. Then we swap the vowels and continue until $i \ge j$.

Time Complexity: $O(n)$  
Space Complexity: $O(n)$ due to list conversion.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = "aeiouAEIOU"
        i, j = 0, len(s) - 1
        cs = list(s)
        while i < j:
            while i < j and cs[i] not in vowels:
                i += 1
            while i < j and cs[j] not in vowels:
                j -= 1
            if i < j:
                cs[i], cs[j] = cs[j], cs[i]
                i, j = i + 1, j - 1
        return "".join(cs)
```

#### Java

```java
class Solution {
    public String reverseVowels(String s) {
        boolean[] vowels = new boolean[128];
        for (char c : "aeiouAEIOU".toCharArray()) {
            vowels[c] = true;
        }
        char[] cs = s.toCharArray();
        int i = 0, j = cs.length - 1;
        while (i < j) {
            while (i < j && !vowels[cs[i]]) i++;
            while (i < j && !vowels[cs[j]]) j--;
            if (i < j) {
                char temp = cs[i];
                cs[i] = cs[j];
                cs[j] = temp;
                i++;
                j--;
            }
        }
        return new String(cs);
    }
}
```

#### C++

```cpp
class Solution {
public:
    string reverseVowels(string s) {
        unordered_set<char> vowels = {'a','e','i','o','u','A','E','I','O','U'};
        int i = 0, j = s.length() - 1;
        while (i < j) {
            while (i < j && !vowels.count(s[i])) i++;
            while (i < j && !vowels.count(s[j])) j--;
            if (i < j) {
                swap(s[i], s[j]);
                i++;
                j--;
            }
        }
        return s;
    }
};
```

#### Go

```go
func reverseVowels(s string) string {
    vowels := [128]bool{}
    for _, c := range "aeiouAEIOU" {
        vowels[c] = true
    }
    cs := []byte(s)
    i, j := 0, len(cs)-1
    for i < j {
        for i < j && !vowels[cs[i]] {
            i++
        }
        for i < j && !vowels[cs[j]] {
            j--
        }
        if i < j {
            cs[i], cs[j] = cs[j], cs[i]
            i++
            j--
        }
    }
    return string(cs)
}
```

#### TypeScript

```ts
function reverseVowels(s: string): string {
    const vowels = new Set('aeiouAEIOU');
    const arr = s.split('');
    let i = 0, j = arr.length - 1;
    while (i < j) {
        while (i < j && !vowels.has(arr[i])) i++;
        while (i < j && !vowels.has(arr[j])) j--;
        [arr[i], arr[j]] = [arr[j], arr[i]];
        i++;
        j--;
    }
    return arr.join('');
}
```

#### Rust

```rust
impl Solution {
    pub fn reverse_vowels(s: String) -> String {
        let vowels = "aeiouAEIOU".chars().collect::<std::collections::HashSet<_>>();
        let mut chars: Vec<char> = s.chars().collect();
        let (mut i, mut j) = (0, chars.len() - 1);
        while i < j {
            while i < j && !vowels.contains(&chars[i]) {
                i += 1;
            }
            while i < j && !vowels.contains(&chars[j]) {
                j -= 1;
            }
            if i < j {
                chars.swap(i, j);
                i += 1;
                j -= 1;
            }
        }
        chars.into_iter().collect()
    }
}
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
