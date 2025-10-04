import unittest

from split_nodes import split_nodes_delimiter
from textnode import TextNode, TextType

class TestSplitNodesDelimiter(unittest.TestCase):
  def test_bold_single(self):
    node = TextNode("This is text with a **bold text** word", TextType.TEXT)
    actual = split_nodes_delimiter([node], "**", TextType.BOLD)
    expected = [
      TextNode("This is text with a ", TextType.TEXT),
      TextNode("bold text", TextType.BOLD),
      TextNode(" word", TextType.TEXT),
    ]
    self.assertEqual(actual, expected)
  
  def test_italics_single(self):
    node = TextNode("This is text with an _italics text_ word", TextType.TEXT)
    actual = split_nodes_delimiter([node], "_", TextType.ITALIC)
    expected = [
      TextNode("This is text with an ", TextType.TEXT),
      TextNode("italics text", TextType.ITALIC),
      TextNode(" word", TextType.TEXT),
    ]
    self.assertEqual(actual, expected)

  def test_code_single(self):
    node = TextNode("This is text with a `code block` word", TextType.TEXT)
    actual = split_nodes_delimiter([node], "`", TextType.CODE)
    expected = [
      TextNode("This is text with a ", TextType.TEXT),
      TextNode("code block", TextType.CODE),
      TextNode(" word", TextType.TEXT),
    ]
    self.assertEqual(actual, expected)

  def test_code_multiple(self):
    node = TextNode("Start `code1``code2` middle `code3`", TextType.TEXT)
    actual = split_nodes_delimiter([node], "`", TextType.CODE)
    expected = [
      TextNode("Start ", TextType.TEXT),
      TextNode("code1", TextType.CODE),
      TextNode("code2", TextType.CODE),
      TextNode(" middle ", TextType.TEXT),
      TextNode("code3", TextType.CODE),
    ]
    self.assertEqual(actual, expected)

  def test_code_alone(self):
    node = TextNode("`code1`", TextType.TEXT)
    actual = split_nodes_delimiter([node], "`", TextType.CODE)
    expected = [TextNode("code1", TextType.CODE)]
    self.assertEqual(actual, expected)

  def test_code_missing_end_tag(self):
    node = TextNode("Start `code1` middle `code2", TextType.TEXT)
    self.assertRaises(Exception, split_nodes_delimiter, [node], "`", TextType.CODE)
    
