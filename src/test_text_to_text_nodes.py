import unittest

from text_to_text_nodes import text_to_text_nodes
from textnode import TextNode, TextType

class TestTextToTextNodes(unittest.TestCase):
  def test_text_with_all_types(self):
    text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
    actual = text_to_text_nodes(text)
    expected = [
      TextNode("This is ", TextType.TEXT),
      TextNode("text", TextType.BOLD),
      TextNode(" with an ", TextType.TEXT),
      TextNode("italic", TextType.ITALIC),
      TextNode(" word and a ", TextType.TEXT),
      TextNode("code block", TextType.CODE),
      TextNode(" and an ", TextType.TEXT),
      TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
      TextNode(" and a ", TextType.TEXT),
      TextNode("link", TextType.LINK, "https://boot.dev"),
    ]
    self.assertEqual(actual, expected)

  def test_text_with_all_types_no_text_between(self):
    text = "**text**_italic_`code block`![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg)[link](https://boot.dev)"
    actual = text_to_text_nodes(text)
    expected = [
      TextNode("text", TextType.BOLD),
      TextNode("italic", TextType.ITALIC),
      TextNode("code block", TextType.CODE),
      TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
      TextNode("link", TextType.LINK, "https://boot.dev"),
    ]
    self.assertEqual(actual, expected)

  def test_text_with_no_types(self):
    text = "Plain text block with no other types"
    actual = text_to_text_nodes(text)
    expected = [TextNode("Plain text block with no other types", TextType.TEXT)]
    self.assertEqual(actual, expected)
    