# 1657. Determine if Two Strings Are Close

> Difficulty: Medium  
> Tags: Hash Table, String, Counting, Sorting  
> Source: Weekly Contest 215 Q2

## Problem

Two strings are considered **close** if you can attain one from the other using the following operations:

1. **Swap any two existing characters.**  
   - For example, `a<u>b</u>cd<u>e</u> → a<u>e</u>cd<u>b</u>`
   
2. **Transform every occurrence of one existing character into another existing character, and do the same with the other character.**  
   - For example, `<u>aa</u>c<u>abb</u> → <u>bb</u>c<u>baa</u>` (all `a`'s turn into `b`'s, and all `b`'s turn into `a`'s)

You can use the operations on either string as many times as necessary.

Given two strings, `word1` and `word2`, return `true` if `word1` and `word2` are **close**, and `false` otherwise.

### Example 1:

```
Input: word1 = "abc", word2 = "bca"
Output: true
Explanation: You can attain word2 from word1 in 2 operations.
Apply Operation 1: "a<u>bc</u>" → "a<u>cb</u>"
Apply Operation 1: "<u>a</u>c<u>b</u>" → "<u>b</u>c<u>a</u>"
```

### Example 2:

```
Input: word1 = "a", word2 = "aa"
Output: false
Explanation: It is impossible to attain word2 from word1, or vice versa, in any number of operations.
```

### Example 3:

```
Input: word1 = "cabbba", word2 = "abbccc"
Output: true
Explanation: You can attain word2 from word1 in 3 operations.
Apply Operation 1: "ca<u>b</u>bb<u>a</u>" → "ca<u>a</u>bb<u>b</u>"
Apply Operation 2: "<u>c</u>aa<u>bbb</u>" → "<u>b</u>aa<u>ccc</u>"
Apply Operation 2: "<u>baa</u>ccc" → "<u>abb</u>ccc"
```

## Constraints

- `1 <= word1.length, word2.length <= 10^5`
- `word1` and `word2` contain only lowercase English letters.

---

## Approach

To determine if two strings are **close**, we need to check two main conditions:
1. Both strings must contain the same types of characters.
2. The frequency of characters in both strings must be the same after sorting the counts.

- **Time Complexity:** $O(m + n + C \times \log C)$, where `m` and `n` are the lengths of `word1` and `word2`, respectively, and `C` is the number of letter types (26 in this case).
- **Space Complexity:** $O(C)$, where `C` is the number of unique characters (26).

---

## Solutions

### Python

```python
from collections import Counter

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        cnt1, cnt2 = Counter(word1), Counter(word2)
        return sorted(cnt1.values()) == sorted(cnt2.values()) and set(
            cnt1.keys()
        ) == set(cnt2.keys())
```

### Java

```java
import java.util.*;

class Solution {
    public boolean closeStrings(String word1, String word2) {
        int[] cnt1 = new int[26];
        int[] cnt2 = new int[26];
        for (int i = 0; i < word1.length(); ++i) {
            ++cnt1[word1.charAt(i) - 'a'];
        }
        for (int i = 0; i < word2.length(); ++i) {
            ++cnt2[word2.charAt(i) - 'a'];
        }
        for (int i = 0; i < 26; ++i) {
            if ((cnt1[i] == 0) != (cnt2[i] == 0)) {
                return false;
            }
        }
        Arrays.sort(cnt1);
        Arrays.sort(cnt2);
        return Arrays.equals(cnt1, cnt2);
    }
}
```

### C++

```cpp
#include <unordered_map>
#include <unordered_set>
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    bool closeStrings(string word1, string word2) {
        int cnt1[26]{};
        int cnt2[26]{};
        for (char& c : word1) {
            ++cnt1[c - 'a'];
        }
        for (char& c : word2) {
            ++cnt2[c - 'a'];
        }
        for (int i = 0; i < 26; ++i) {
            if ((cnt1[i] == 0) != (cnt2[i] == 0)) {
                return false;
            }
        }
        sort(cnt1, cnt1 + 26);
        sort(cnt2, cnt2 + 26);
        return equal(cnt1, cnt1 + 26, cnt2);
    }
};
```

### Go

```go
import "sort"

func closeStrings(word1 string, word2 string) bool {
	cnt1 := make([]int, 26)
	cnt2 := make([]int, 26)
	for _, c := range word1 {
		cnt1[c-'a']++
	}
	for _, c := range word2 {
		cnt2[c-'a']++
	}
	for i := 0; i < 26; i++ {
		if (cnt1[i] == 0) != (cnt2[i] == 0) {
			return false
		}
	}
	sort.Ints(cnt1)
	sort.Ints(cnt2)
	return slices.Equal(cnt1, cnt2)
}
```

### TypeScript

```ts
function closeStrings(word1: string, word2: string): boolean {
    const cnt1 = Array(26).fill(0);
    const cnt2 = Array(26).fill(0);
    for (const c of word1) {
        ++cnt1[c.charCodeAt(0) - 'a'.charCodeAt(0)];
    }
    for (const c of word2) {
        ++cnt2[c.charCodeAt(0) - 'a'.charCodeAt(0)];
    }
    for (let i = 0; i < 26; ++i) {
        if ((cnt1[i] === 0) !== (cnt2[i] === 0)) {
            return false;
        }
    }
    cnt1.sort((a, b) => a - b);
    cnt2.sort((a, b) => a - b);
    return cnt1.join('.') === cnt2.join('.');
}
```

### Rust

```rust
impl Solution {
    pub fn close_strings(word1: String, word2: String) -> bool {
        let mut cnt1 = vec![0; 26];
        let mut cnt2 = vec![0; 26];
        for c in word1.chars() {
            cnt1[((c as u8) - b'a') as usize] += 1;
        }
        for c in word2.chars() {
            cnt2[((c as u8) - b'a') as usize] += 1;
        }
        for i in 0..26 {
            if (cnt1[i] == 0) != (cnt2[i] == 0) {
                return false;
            }
        }
        cnt1.sort();
        cnt2.sort();
        cnt1 == cnt2
    }
}
```
