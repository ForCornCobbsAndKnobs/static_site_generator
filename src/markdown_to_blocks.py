from textnode import *
from htmlnode import *
from split_nodes_delimiter import *
from extract_markdown_images import *



def markdown_to_blocks(doc):
    blocks = doc.split('\n\n')
    stripped_blocks = []
    for block in blocks:
        if len(block) == 0:
            continue
        block = block.strip()
        lines = [ln.strip() for ln in block.split('\n')]
        proc_block = '\n'.join(lines)
        if proc_block:
            stripped_blocks.append(proc_block)
        
    return stripped_blocks


doc = """
            This is **bolded** paragraph

            This is another paragraph with _italic_ text and `code` here
            This is the same paragraph on a new line

            - This is a list
            - with items
"""
blocks = markdown_to_blocks(doc)
print(blocks)