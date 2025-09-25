from enum import Enum

from htmlnode import HTMLNode, LeafNode, ParentNode

class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = 'links'
    IMAGE = 'image'

class TextNode():

    def __init__(self, text, text_type, url=None):
        self.text, self.text_type, self.url = text, text_type, url

    
    def __eq__(self, other):
        if not isinstance(other, TextNode):
            return False
        return (self.text, self.text_type, self.url) == (other.text, other.text_type, other.url)
    

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"

    
def text_node_to_html_node(text_node):
    if text_node.text_type is TextType.TEXT:
        return LeafNode(tag=None, value=text_node.text)
    elif text_node.text_type is TextType.BOLD:
        return LeafNode(tag='b', value=text_node.text)
    elif text_node.text_type is TextType.ITALIC:
        return LeafNode(tag='i', value=text_node.text)
    elif text_node.text_type is TextType.CODE:
        return LeafNode(tag='code', value=text_node.text)
    elif text_node.text_type is TextType.LINK:
        return LeafNode(tag='a', value=text_node.text, props={'href' : text_node.url})
    elif text_node.text_type is TextType.IMAGE:
        return LeafNode(tag='img', value='', props={'src': text_node.url, 'alt': text_node.text})
    raise Exception(f"Unrecognized text type: {text_node.text_type}")