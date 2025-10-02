from htmlnode import HtmlNode

# sub class of HtmlNode that always has children instead of value
class ParentNode(HtmlNode):
  def __init__(self, tag, children, props=None):
    super().__init__(tag, None, children, props)

  def to_html(self):
    if self.tag is None:
      raise ValueError("tag is required on ParentNode")
    
    if not self.children or len(self.children) == 0:
      raise ValueError("children are required on ParentNode")
    
    parts = [f"<{self.tag}>"]
    for child in self.children:
      parts.append(child.to_html())
    parts.append(f"</{self.tag}>")

    return "".join(parts)