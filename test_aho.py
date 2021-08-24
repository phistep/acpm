import unittest

from aho import TrieNode, substr


class TestTrie(unittest.TestCase):
    def test_TrieNode(self):
        trie = TrieNode()
        self.assertEqual(len(trie.children), 0)

    def test_add_word(self):
        trie = TrieNode()
        word = 'fo'
        trie.add_word(word)

        self.assertIn('f', trie.children)
        f = trie.children['f']
        self.assertTrue(isinstance(f, TrieNode))

        self.assertIn('o', f.children)
        o = f.children['o']
        self.assertTrue(isinstance(o, TrieNode))
        self.assertFalse(o.children)

    def test_add_word_recursive(self):
        trie = TrieNode()
        for word in ['foo', 'foobar', 'foot']:
            trie.add_word(word)

        self.assertIn('f', trie.children)
        f = trie.children['f']
        self.assertTrue(isinstance(f, TrieNode))

        self.assertIn('o', f.children)
        o = f.children['o']
        self.assertTrue(isinstance(o, TrieNode))

        self.assertIn('o', o.children)
        o2 = o.children['o']
        self.assertTrue(isinstance(o2, TrieNode))

        self.assertIn('b', o2.children)
        b = o2.children['b']
        self.assertTrue(isinstance(b, TrieNode))

        self.assertIn('a', b.children)
        a = b.children['a']
        self.assertTrue(isinstance(a, TrieNode))

        self.assertIn('r', a.children)
        r = a.children['r']
        self.assertTrue(isinstance(r, TrieNode))
        self.assertFalse(r.children)

        self.assertIn('t', o2.children)
        t = o2.children['t']
        self.assertTrue(isinstance(t, TrieNode))
        self.assertFalse(t.children)

    def test_prefix(self):
        word = 'foobar'
        trie = TrieNode()
        trie.add_word(word)
        self.assertEqual(trie['f']['o']['o']['b']['a']['r'].prefix, word)


    def test_view(self):
        trie = TrieNode()
        for word in ['foo', 'bar', 'foobar', 'foot']:
            trie.add_word(word)
        trie.view()


class TestAho(unittest.TestCase):
    def test_substr(self):
        # TODO
        for input_, expected in []:
            with self.subTest(input_=input_):
                result = substr(*input_)
                self.assertEqual(set(result), set(expected))
