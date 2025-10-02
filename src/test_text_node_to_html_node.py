import unittest

from text_node_to_html_node import text_node_to_html_node
from textnode import TextNode, TextType

class TestTextNodeToHtmlNode(unittest.TestCase):
  def test_text(self):
    node = TextNode("This is a text node", TextType.TEXT)
    html_node = text_node_to_html_node(node)
    self.assertEqual(html_node.tag, None)
    self.assertEqual(html_node.value, "This is a text node")
    self.assertEqual(html_node.to_html(), "This is a text node")

  def test_bold(self):
    node = TextNode("bold text", TextType.BOLD)
    html_node = text_node_to_html_node(node)
    self.assertEqual(html_node.tag, "b")
    self.assertEqual(html_node.value, "bold text")
    self.assertEqual(html_node.to_html(), "<b>bold text</b>")

  def test_italics(self):
    node = TextNode("italic text", TextType.ITALIC)
    html_node = text_node_to_html_node(node)
    self.assertEqual(html_node.tag, "i")
    self.assertEqual(html_node.value, "italic text")
    self.assertEqual(html_node.to_html(), "<i>italic text</i>")

  def test_code(self):
    node = TextNode("some code here", TextType.CODE)
    html_node = text_node_to_html_node(node)
    self.assertEqual(html_node.tag, "code")
    self.assertEqual(html_node.value, "some code here")
    self.assertEqual(html_node.to_html(), "<code>some code here</code>")

  def test_link(self):
    node = TextNode("link to another page", TextType.LINK, "http://other_url")
    html_node = text_node_to_html_node(node)
    self.assertEqual(html_node.tag, "a")
    self.assertEqual(html_node.value, "link to another page")
    self.assertEqual(html_node.props['href'], "http://other_url")
    self.assertEqual(html_node.to_html(), '<a href="http://other_url">link to another page</a>')

  def test_image(self):
    node = TextNode("image text", TextType.IMAGE, "http://image.jpg")
    html_node = text_node_to_html_node(node)
    self.assertEqual(html_node.tag, "img")
    self.assertEqual(html_node.value, "")
    self.assertEqual(html_node.props['alt'], "image text")
    self.assertEqual(html_node.props['src'], "http://image.jpg")
    self.assertEqual(html_node.to_html(), '<img alt="image text" src="http://image.jpg"></img>')

  def text_bad_text_type(self):
    node = TextNode("bad type", "unknown_type")
    self.assertRaises(Exception, text_node_to_html_node, node)
    