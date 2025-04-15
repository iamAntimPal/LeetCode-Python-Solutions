---
comments: true
difficulty: Medium
edit_url: Antim
tags:
    - Design
    - Trie
    - Hash Table
    - String
---

<!-- problem:start -->

# [208. Implement Trie (Prefix Tree)](https://leetcode.com/problems/implement-trie-prefix-tree)


## Description

<!-- description:start -->

<p>A <a href="https://en.wikipedia.org/wiki/Trie" target="_blank"><strong>trie</strong></a> (pronounced as &quot;try&quot;) or <strong>prefix tree</strong> is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.</p>

<p>Implement the Trie class:</p>

<ul>
	<li><code>Trie()</code> Initializes the trie object.</li>
	<li><code>void insert(String word)</code> Inserts the string <code>word</code> into the trie.</li>
	<li><code>boolean search(String word)</code> Returns <code>true</code> if the string <code>word</code> is in the trie (i.e., was inserted before), and <code>false</code> otherwise.</li>
	<li><code>boolean startsWith(String prefix)</code> Returns <code>true</code> if there is a previously inserted string <code>word</code> that has the prefix <code>prefix</code>, and <code>false</code> otherwise.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input</strong>
[&quot;Trie&quot;, &quot;insert&quot;, &quot;search&quot;, &quot;search&quot;, &quot;startsWith&quot;, &quot;insert&quot;, &quot;search&quot;]
[[], [&quot;apple&quot;], [&quot;apple&quot;], [&quot;app&quot;], [&quot;app&quot;], [&quot;app&quot;], [&quot;app&quot;]]
<strong>Output</strong>
[null, null, true, false, true, null, true]

<strong>Explanation</strong>
Trie trie = new Trie();
trie.insert(&quot;apple&quot;);
trie.search(&quot;apple&quot;);   // return True
trie.search(&quot;app&quot;);     // return False
trie.startsWith(&quot;app&quot;); // return True
trie.insert(&quot;app&quot;);
trie.search(&quot;app&quot;);     // return True
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= word.length, prefix.length &lt;= 2000</code></li>
	<li><code>word</code> and <code>prefix</code> consist only of lowercase English letters.</li>
	<li>At most <code>3 * 10<sup>4</sup></code> calls <strong>in total</strong> will be made to <code>insert</code>, <code>search</code>, and <code>startsWith</code>.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1

<!-- tabs:start -->

#### Python3

```python
class Trie:
    def __init__(self):
        self.children = [None] * 26
        self.is_end = False

    def insert(self, word: str) -> None:
        node = self
        for c in word:
            idx = ord(c) - ord('a')
            if node.children[idx] is None:
                node.children[idx] = Trie()
            node = node.children[idx]
        node.is_end = True

    def search(self, word: str) -> bool:
        node = self._search_prefix(word)
        return node is not None and node.is_end

    def startsWith(self, prefix: str) -> bool:
        node = self._search_prefix(prefix)
        return node is not None

    def _search_prefix(self, prefix: str):
        node = self
        for c in prefix:
            idx = ord(c) - ord('a')
            if node.children[idx] is None:
                return None
            node = node.children[idx]
        return node


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
```

#### Java

```java
class Trie {
    private Trie[] children;
    private boolean isEnd;

    public Trie() {
        children = new Trie[26];
    }

    public void insert(String word) {
        Trie node = this;
        for (char c : word.toCharArray()) {
            int idx = c - 'a';
            if (node.children[idx] == null) {
                node.children[idx] = new Trie();
            }
            node = node.children[idx];
        }
        node.isEnd = true;
    }

    public boolean search(String word) {
        Trie node = searchPrefix(word);
        return node != null && node.isEnd;
    }

    public boolean startsWith(String prefix) {
        Trie node = searchPrefix(prefix);
        return node != null;
    }

    private Trie searchPrefix(String s) {
        Trie node = this;
        for (char c : s.toCharArray()) {
            int idx = c - 'a';
            if (node.children[idx] == null) {
                return null;
            }
            node = node.children[idx];
        }
        return node;
    }
}

/**
 * Your Trie object will be instantiated and called as such:
 * Trie obj = new Trie();
 * obj.insert(word);
 * boolean param_2 = obj.search(word);
 * boolean param_3 = obj.startsWith(prefix);
 */
```

#### C++

```cpp
class Trie {
private:
    vector<Trie*> children;
    bool isEnd;

    Trie* searchPrefix(string s) {
        Trie* node = this;
        for (char c : s) {
            int idx = c - 'a';
            if (!node->children[idx]) return nullptr;
            node = node->children[idx];
        }
        return node;
    }

public:
    Trie()
        : children(26)
        , isEnd(false) {}

    void insert(string word) {
        Trie* node = this;
        for (char c : word) {
            int idx = c - 'a';
            if (!node->children[idx]) node->children[idx] = new Trie();
            node = node->children[idx];
        }
        node->isEnd = true;
    }

    bool search(string word) {
        Trie* node = searchPrefix(word);
        return node != nullptr && node->isEnd;
    }

    bool startsWith(string prefix) {
        Trie* node = searchPrefix(prefix);
        return node != nullptr;
    }
};

/**
 * Your Trie object will be instantiated and called as such:
 * Trie* obj = new Trie();
 * obj->insert(word);
 * bool param_2 = obj->search(word);
 * bool param_3 = obj->startsWith(prefix);
 */
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->