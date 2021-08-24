from typing import List, Optional


class TrieNode():
    def __init__(self,
                 parent: Optional['TrieNode'] = None,
                 prefix: str = ''):
        self.children = {}
        self.parent = parent
        self.prefix = prefix
        self.failure_link = None

    def __repr__(self):
        return f"<TrieNode '{self.prefix}' edges={set(self.children.keys())}>"

    def __str__(self):
        return self.prefix

    def __getitem__(self, key: str) -> str:
        return self.children[key]

    def __setitem__(self, key: str, value: str):
        assert len(key) == 1
        self.childgren[key] = value

    def __contains__(self, word: str) -> bool:
        # TODO test!
        # TODO correct complexity?
        if not word:
            return True  # TODO correct?
        if len(word) == 1:
            return word in self.children
        else:
            char, suffix = word[0], word[1:]
            if char in self.children:
                return any(suffix in child for child in self.children)
        return False

    def add_word(self, word: str):
        if not word:
            return

        char, suffix = word[0], word[1:]

        if char not in self.children:
            self.children[char] = TrieNode(parent=self,
                                           prefix=self.prefix + char)
        self.children[char].add_word(suffix)

    def calculate_failure_links(self, root: Optional['TrieNode'] = None):
        if not root:
            root = self

        for child in self.children:
            child.calculate_failure_links(root=root)

        if self is root:
            self.failure_link = self
        else:
            # TODO
            # when does it stop
            # how does it find back to the root node
            # complexity
            current = root
            suffix = self.parent.prefix
            while suffix:
                for char in suffix:
                    if char in current:
                        current = current[char]
                        self.failure_link = root
                    else:
                        break
                suffix = suffix[1:]

    def view(self,
             dot: Optional['graphviz.Digraph'] = None) -> 'graphviz.Digraph':
        import graphviz

        if not dot:
            dot = graphviz.Digraph()
            dot.node('')
            dot.edge('', '', style='dashed')

        for edge, node in self.children.items():
            dot.node(node.prefix)
            dot.edge(self.prefix, node.prefix, edge)
            if node.failure_link:
                dot.edge(node.prefix, node.failure_link.prefix, style='dashed')
            dot = node.view(dot)

        if not self.parent:
            dot.view()

        return dot


def substr(haystack: str, needles: List[str]):
    trie = TrieNode()
    for word in needles:
        trie.add_word(word)
    trie.calculate_failure_links()

    # calculate failurelinks
    # walk haystack, mark matches
    # gather and return matches
