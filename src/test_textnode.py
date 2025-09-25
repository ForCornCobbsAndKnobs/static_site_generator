import unittest

from textnode import TextNode, TextType, text_node_to_html_node
from htmlnode import HTMLNode, LeafNode, ParentNode


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

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")
if __name__ == "__main__":
    unittest.main()