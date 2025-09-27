from htmlnode import ParentNode, LeafNode
from textnode import TextType, TextNode

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type is not TextType.TEXT:
            new_nodes.append(node)
            continue
        split_nodes = node.text.split(delimiter)
        if len(split_nodes) % 2 == 0:
            raise Exception(f"Unmatched delimiter")
        for index in range(len(split_nodes)):
            if len(split_nodes[index])==0:
                continue
            elif index % 2 == 0:
                new_node = TextNode(split_nodes[index], TextType.TEXT)
                new_nodes.append(new_node)
            else:
                new_node = TextNode(split_nodes[index], text_type)
                new_nodes.append(new_node)
    return new_nodes

            