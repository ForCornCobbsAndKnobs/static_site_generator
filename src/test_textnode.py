import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    

    def test_not_eq(self):
        node = TextNode("This is a text node", TextType.LINK, url="https://www.google.com")
        node2 = TextNode("This is a differnt node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_almost_eq(self):
        node = TextNode("This is a node", TextType.TEXT)
        node2 = TextNode("This is a different node", TextType.TEXT)
        self.assertNotEqual(node, node2)
    
    def test_almost_eq_2(self):
        node = TextNode("This is a node", TextType.ITALIC)
        node2 = TextNode("This is a node", TextType.BOLD)
        self.assertNotEqual(node, node2)
if __name__ == "__main__":
    unittest.main()