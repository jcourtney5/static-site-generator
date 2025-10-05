import unittest

from split_nodes_link import split_nodes_link
from textnode import TextNode, TextType

class TestSplitNodesLink(unittest.TestCase):
  def test_no_links(self):
    node = TextNode("Text with no link", TextType.TEXT)
    actual = split_nodes_link([node])
    expected = [TextNode("Text with no link", TextType.TEXT)]
    self.assertEqual(actual, expected)

  def test_one_link_middle(self):
    node = TextNode("Before link [link1](https://link_url1) after link", TextType.TEXT)
    actual = split_nodes_link([node])
    expected = [
      TextNode("Before link ", TextType.TEXT),
      TextNode("link1", TextType.LINK, "https://link_url1"),
      TextNode(" after link", TextType.TEXT),
    ]
    self.assertEqual(actual, expected)

  def test_one_link_at_start(self):
    node = TextNode("[link1](https://link_url1) after link", TextType.TEXT)
    actual = split_nodes_link([node])
    expected = [
      TextNode("link1", TextType.LINK, "https://link_url1"),
      TextNode(" after link", TextType.TEXT),
    ]
    self.assertEqual(actual, expected)

  def test_one_link_at_end(self):
    node = TextNode("Before link [link1](https://link_url1)", TextType.TEXT)
    actual = split_nodes_link([node])
    expected = [
      TextNode("Before link ", TextType.TEXT),
      TextNode("link1", TextType.LINK, "https://link_url1"),
    ]
    self.assertEqual(actual, expected)

  def test_one_link_alone(self):
    node = TextNode("[link1](https://link_url1)", TextType.TEXT)
    actual = split_nodes_link([node])
    expected = [TextNode("link1", TextType.LINK, "https://link_url1")]
    self.assertEqual(actual, expected)

  def test_two_links(self):
    node = TextNode("Beginning [link1](https://link_url1) middle [link2](https://link_url2) end", TextType.TEXT)
    actual = split_nodes_link([node])
    expected = [
      TextNode("Beginning ", TextType.TEXT),
      TextNode("link1", TextType.LINK, "https://link_url1"),
      TextNode(" middle ", TextType.TEXT),
      TextNode("link2", TextType.LINK, "https://link_url2"),
      TextNode(" end", TextType.TEXT),
    ]
    self.assertEqual(actual, expected)