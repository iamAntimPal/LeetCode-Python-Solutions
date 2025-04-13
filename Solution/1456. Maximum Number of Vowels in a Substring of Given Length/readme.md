

# 1456. Maximum Number of Vowels in a Substring of Given Length

> Difficulty: Medium  
> Source: [Leetcode](https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length)  
> Tags: String, Sliding Window

## Description

Given a string `s` and an integer `k`, return _the maximum number of vowel letters in any substring of_ `s` _with length_ `k`.

**Vowel letters** in English are `'a'`, `'e'`, `'i'`, `'o'`, and `'u'`.

### Example 1:

```
Input: s = "abciiidef", k = 3
Output: 3
Explanation: The substring "iii" contains 3 vowel letters.
```

### Example 2:

```
Input: s = "aeiou", k = 2
Output: 2
Explanation: Any substring of length 2 contains 2 vowels.
```

### Example 3:

```
Input: s = "leetcode", k = 3
Output: 2
Explanation: "lee", "eet", and "ode" contain 2 vowels.
```

## Constraints:

- `1 <= s.length <= 10^5`
- `s` consists of lowercase English letters.
- `1 <= k <= s.length`

---

## Explanation

We use the **sliding window** technique to keep track of the number of vowels in a window of length `k`. 

1. Count vowels in the first `k` characters.
2. Slide the window one character at a time:
   - Add 1 if the new character is a vowel.
   - Subtract 1 if the character that moves out of the window is a vowel.
3. Keep track of the maximum count found.

This approach runs in **O(n)** time and uses **O(1)** space.

---

## Solutions

### Python3

```python
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set("aeiou")
        ans = cnt = sum(c in vowels for c in s[:k])
        for i in range(k, len(s)):
            cnt += int(s[i] in vowels) - int(s[i - k] in vowels)
            ans = max(ans, cnt)
        return ans
```

### Java

```java
class Solution {
    public int maxVowels(String s, int k) {
        int cnt = 0;
        for (int i = 0; i < k; ++i) {
            if (isVowel(s.charAt(i))) {
                ++cnt;
            }
        }
        int ans = cnt;
        for (int i = k; i < s.length(); ++i) {
            if (isVowel(s.charAt(i))) cnt++;
            if (isVowel(s.charAt(i - k))) cnt--;
            ans = Math.max(ans, cnt);
        }
        return ans;
    }

    private boolean isVowel(char c) {
        return "aeiou".indexOf(c) >= 0;
    }
}
```

### C++

```cpp
class Solution {
public:
    int maxVowels(string s, int k) {
        auto isVowel = [](char c) {
            return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u';
        };
        int cnt = count_if(s.begin(), s.begin() + k, isVowel);
        int ans = cnt;
        for (int i = k; i < s.size(); ++i) {
            cnt += isVowel(s[i]) - isVowel(s[i - k]);
            ans = max(ans, cnt);
        }
        return ans;
    }
};
```

### Go

```go
func maxVowels(s string, k int) int {
	isVowel := func(c byte) bool {
		return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u'
	}
	cnt := 0
	for i := 0; i < k; i++ {
		if isVowel(s[i]) {
			cnt++
		}
	}
	ans := cnt
	for i := k; i < len(s); i++ {
		if isVowel(s[i-k]) {
			cnt--
		}
		if isVowel(s[i]) {
			cnt++
		}
		if cnt > ans {
			ans = cnt
		}
	}
	return ans
}
```

### TypeScript

```ts
function maxVowels(s: string, k: number): number {
    const vowels = new Set(['a', 'e', 'i', 'o', 'u']);
    let cnt = 0;
    for (let i = 0; i < k; i++) {
        if (vowels.has(s[i])) {
            cnt++;
        }
    }
    let ans = cnt;
    for (let i = k; i < s.length; i++) {
        if (vowels.has(s[i])) {
            cnt++;
        }
        if (vowels.has(s[i - k])) {
            cnt--;
        }
        ans = Math.max(ans, cnt);
    }
    return ans;
}
```

### PHP

```php
class Solution {
    function isVowel($c) {
        return $c === 'a' || $c === 'e' || $c === 'i' || $c === 'o' || $c === 'u';
    }

    function maxVowels($s, $k) {
        $cnt = 0;
        for ($i = 0; $i < $k; $i++) {
            if ($this->isVowel($s[$i])) {
                $cnt++;
            }
        }
        $ans = $cnt;
        for ($j = $k; $j < strlen($s); $j++) {
            if ($this->isVowel($s[$j - $k])) {
                $cnt--;
            }
            if ($this->isVowel($s[$j])) {
                $cnt++;
            }
            $ans = max($ans, $cnt);
        }
        return $ans;
    }
}
```

