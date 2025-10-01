import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
  def test_eq(self):
    node = TextNode("This is a text node", TextType.BOLD)
    node2 = TextNode("This is a text node", TextType.BOLD)
    self.assertEqual(node, node2)

  def test_eq_with_url(self):
    node = TextNode("Link", TextType.LINK, "http://link_url.html")
    node2 = TextNode("Link", TextType.LINK, "http://link_url.html")
    self.assertEqual(node, node2)

  def test_text_not_eq(self):
    node = TextNode("Text1", TextType.BOLD)
    node2 = TextNode("Text2", TextType.BOLD)
    self.assertNotEqual(node, node2)

  def test_type_not_eq(self):
    node = TextNode("Text", TextType.BOLD)
    node2 = TextNode("Text", TextType.ITALIC)
    self.assertNotEqual(node, node2)

  def test_url_not_eq(self):
    node = TextNode("Link", TextType.LINK, "http://link_url1.html")
    node2 = TextNode("Link", TextType.LINK, "http://link_url2.html")
    self.assertNotEqual(node, node2)


if __name__ == "__main__":
  unittest.main()