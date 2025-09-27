import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode
from textnode import TextNode, TextType, text_node_to_html_node
from split_nodes_delimiter import split_nodes_delimiter


class TestTextNode(unittest.TestCase):

    def test_delimiter(self):
        nodes = [
        TextNode("This has `code`", TextType.TEXT),
        TextNode("This is bold", TextType.BOLD),  # already processed, leave as-is
        TextNode("This has more `code blocks` here", TextType.TEXT)
    ]
        new_nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
        self.assertEqual(
            new_nodes,
            [
                TextNode("This has ", TextType.TEXT),
                TextNode("code", TextType.CODE),
                TextNode("This is bold", TextType.BOLD),
                TextNode("This has more ", TextType.TEXT),
                TextNode("code blocks", TextType.CODE),
                TextNode(" here", TextType.TEXT)
            ]
        )

    def test_unmatched_delimiter_raises_exception(self):
        node = TextNode("This has `unclosed delimiter", TextType.TEXT)
        
        with self.assertRaises(Exception):
            split_nodes_delimiter([node], "`", TextType.CODE)

        