from textnode import TextNode, TextType
from htmlnode import HtmlNode
from leafnode import LeafNode

def text_node_to_html_node(text_node):
  if text_node is None:
    raise ValueError("Text Node is required")
  
  match text_node.text_type:
    case TextType.TEXT:
      return LeafNode(tag=None, value=text_node.text)
    case TextType.BOLD:
      return LeafNode(tag="b", value=text_node.text)
    case TextType.ITALIC:
      return LeafNode(tag="i", value=text_node.text)
    case TextType.CODE:
      return LeafNode(tag="code", value=text_node.text)
    case TextType.LINK:
      return LeafNode(tag="a", value=text_node.text, props={"href": text_node.url})
    case TextType.IMAGE:
      return LeafNode(tag="img", value="", props={"alt": text_node.text, "src": text_node.url})
    case _:
      raise Exception(f"Unknown text_type: {text_node.text_type}")