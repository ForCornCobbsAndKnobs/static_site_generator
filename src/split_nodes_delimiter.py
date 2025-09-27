from htmlnode import *
from textnode import *
from extract_markdown_images import *


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

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        remaining = node.text
        matches = extract_markdown_images(remaining)
        while len(matches) > 0:
            alt, url = matches[0]
            token = f"![{alt}]({url})"
            before, after = remaining.split(token, 1)
            if before:
                new_nodes.append(TextNode(before, TextType.TEXT))
            new_nodes.append(TextNode(alt, TextType.IMAGE, url=url))
            remaining = after
            matches = extract_markdown_images(remaining)
        if remaining:
            new_nodes.append(TextNode(remaining, TextType.TEXT))
    return new_nodes

        


def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        remaining = node.text
        matches = extract_markdown_links(remaining)
        while len(matches) > 0:
            alt, url = matches[0]
            token = f"[{alt}]({url})"
            before, after = remaining.split(token, 1)
            if before:
                new_nodes.append(TextNode(before, TextType.TEXT))
            new_nodes.append(TextNode(alt, TextType.LINK, url=url))
            remaining = after
            matches = extract_markdown_links(remaining)
        if remaining:
            new_nodes.append(TextNode(remaining, TextType.TEXT))
    return new_nodes


def split_to_textnodes(text):
    inital_node = [TextNode(text, TextType.TEXT)]
    new_nodes = split_nodes_delimiter(inital_node, "`", TextType.CODE)
    new_nodes = split_nodes_image(new_nodes)
    new_nodes = split_nodes_link(new_nodes)
    new_nodes = split_nodes_delimiter(new_nodes, "**", TextType.BOLD)
    new_nodes = split_nodes_delimiter(new_nodes, "_", TextType.ITALIC)
    return new_nodes