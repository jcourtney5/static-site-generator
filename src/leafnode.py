from htmlnode import HtmlNode

# sub class of HtmlNode with no children
class LeafNode(HtmlNode):
  def __init__(self, tag, value, props=None):
    super().__init__(value=value, tag=tag, props=props)

  def to_html(self):
    if self.value is None:
      raise ValueError("value is required on LeafNode")

    # if no tag, just return value as raw text
    if self.tag is None:
      return self.value

    # render to html
    return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"