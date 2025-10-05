import os

from markdown_blocks import markdown_to_html_node

def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("# "):
            line = line.strip('#')
            line = line.strip()
            return line
    raise Exception("No h1 header in markdown")

def generate_page(basepath, from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    markdown_file = open(from_path, 'r')
    from_md = markdown_file.read()
    markdown_file.close()
    
    template_file = open(template_path, 'r')
    template = template_file.read()
    template_file.close()
    
    from_node = markdown_to_html_node(from_md)
    from_html = from_node.to_html()

    title = extract_title(from_md)
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", from_html)
    template = template.replace('href="/', f'href="{basepath}')
    template = template.replace('src="/', f'src="{basepath}')

    directory = os.path.dirname(dest_path)
    os.makedirs(directory, exist_ok=True)

    dest_file = open(dest_path, 'w')
    dest_file.write(template)
    dest_file.close()

