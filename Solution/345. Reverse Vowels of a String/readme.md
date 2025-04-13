
<!-- problem:start -->

# [345. Reverse Vowels of a String](https://leetcode.com/problems/reverse-vowels-of-a-string)

## Description

<!-- description:start -->

<p>Given a string <code>s</code>, reverse only all the vowels in the string and return it.</p>

<p>The vowels are <code>'a'</code>, <code>'e'</code>, <code>'i'</code>, <code>'o'</code>, and <code>'u'</code>, and they can appear in both lower and upper cases, more than once.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = "IceCreAm"</span></p>
<p><strong>Output:</strong> <span class="example-io">"AceCreIm"</span></p>
<p><strong>Explanation:</strong> The vowels in <code>s</code> are <code>['I', 'e', 'e', 'A']</code>. On reversing the vowels, s becomes <code>"AceCreIm"</code>.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = "leetcode"</span></p>
<p><strong>Output:</strong> <span class="example-io">"leotcede"</span></p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
    <li><code>1 <= s.length <= 3 * 10<sup>5</sup></code></li>
    <li><code>s</code> consists of <strong>printable ASCII</strong> characters.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Two Pointers

We use two pointers <code>i</code> and <code>j</code> starting at the beginning and end of the string, respectively.

- Move <code>i</code> forward until it points to a vowel.
- Move <code>j</code> backward until it points to a vowel.
- If <code>i < j</code>, swap the characters at <code>i</code> and <code>j</code>.
- Repeat until <code>i >= j</code>.

**Time Complexity:** <code>O(n)</code>  
**Space Complexity:** <code>O(1)</code> (ignoring the space for the result string)

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = "aeiouAEIOU"
        s = list(s)
        i, j = 0, len(s) - 1
        while i < j:
            while i < j and s[i] not in vowels:
                i += 1
            while i < j and s[j] not in vowels:
                j -= 1
            if i < j:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1
        return ''.join(s)
```

#### Java

```java
class Solution {
    public String reverseVowels(String s) {
        Set<Character> vowels = Set.of('a','e','i','o','u','A','E','I','O','U');
        char[] arr = s.toCharArray();
        int i = 0, j = arr.length - 1;
        while (i < j) {
            while (i < j && !vowels.contains(arr[i])) i++;
            while (i < j && !vowels.contains(arr[j])) j--;
            if (i < j) {
                char tmp = arr[i];
                arr[i++] = arr[j];
                arr[j--] = tmp;
            }
        }
        return new String(arr);
    }
}
```

#### C++

```cpp
class Solution {
public:
    string reverseVowels(string s) {
        string vowels = "aeiouAEIOU";
        int i = 0, j = s.size() - 1;
        while (i < j) {
            while (i < j && vowels.find(s[i]) == string::npos) i++;
            while (i < j && vowels.find(s[j]) == string::npos) j--;
            if (i < j) swap(s[i++], s[j--]);
        }
        return s;
    }
};
```

#### Go

```go
func reverseVowels(s string) string {
    vowels := map[byte]bool{'a':true, 'e':true, 'i':true, 'o':true, 'u':true, 'A':true, 'E':true, 'I':true, 'O':true, 'U':true}
    cs := []byte(s)
    i, j := 0, len(cs)-1
    for i < j {
        for i < j && !vowels[cs[i]] { i++ }
        for i < j && !vowels[cs[j]] { j-- }
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
    const chars = s.split('');
    let i = 0, j = chars.length - 1;
    while (i < j) {
        while (i < j && !vowels.has(chars[i])) i++;
        while (i < j && !vowels.has(chars[j])) j--;
        if (i < j) {
            [chars[i], chars[j]] = [chars[j], chars[i]];
            i++;
            j--;
        }
    }
    return chars.join('');
}
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->