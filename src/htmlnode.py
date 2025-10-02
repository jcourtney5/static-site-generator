

class HtmlNode:
  def __init__(self, tag=None, value=None, children=None, props=None):
    self.tag = tag
    self.value = value
    self.children = children
    self.props = props

  def to_html(self):
    raise NotImplementedError()
  
  def props_to_html(self):
    parts = []

    if self.props:
      for key, value in self.props.items():
        parts.append(f" {key}=\"{value}\"")

    return "".join(parts)

  def __repr__(self):
    result = f"tag: {self.tag or ''}, value: {self.value or ''}, props: {self.props_to_html()}"

    if self.children and len(self.children) > 0:
      for child in self.children:
        result += f"\n- child: {str(child)}"

    return result