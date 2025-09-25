class HTMLNode():

    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag, self.value, self.children, self.props = tag, value, children, props
    
    def to_html(self):
        raise NotImplementedError

# python
    def props_to_html(self):
        if not self.props:
            return ""
        return "".join(f' {k}="{v}"' for k, v in self.props.items())
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag=tag, value=value, children=None, props=props)

    def to_html(self):
        if self.value is None:
            raise ValueError("LeafNodes must have a value")
        if self.tag is None:
            return self.value
        props_html = self.props_to_html()  # "" or ' key="val"...'
        return f"<{self.tag}{props_html}>{self.value}</{self.tag}>"
        

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, children=children, props=props, value=None)
    
    def to_html(self):
        if self.tag is None:
            raise ValueError("Parent Nodes must have tags")
        if self.children is None:
            raise ValueError("Parent Nodes must have children")
        props_html = self.props_to_html()
        children_html = ''
        for child in self.children:
            children_html += child.to_html()
        return f'<{self.tag}{props_html}>{children_html}</{self.tag}>'
