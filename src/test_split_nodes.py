import unittest

from split_nodes import split_nodes_delimiter, split_nodes_image, split_nodes_link
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
    

class TestSplitNodesImage(unittest.TestCase):
  def test_no_images(self):
    node = TextNode("Text with no image", TextType.TEXT)
    actual = split_nodes_image([node])
    expected = [TextNode("Text with no image", TextType.TEXT)]
    self.assertEqual(actual, expected)

  def test_one_image_middle(self):
    node = TextNode("Before image ![image](https://i.imgur.com/zjjcJKZ.png) after image", TextType.TEXT)
    actual = split_nodes_image([node])
    expected = [
      TextNode("Before image ", TextType.TEXT),
      TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
      TextNode(" after image", TextType.TEXT),
    ]
    self.assertEqual(actual, expected)

  def test_one_image_at_start(self):
    node = TextNode("![image](https://i.imgur.com/zjjcJKZ.png) after image", TextType.TEXT)
    actual = split_nodes_image([node])
    expected = [
      TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
      TextNode(" after image", TextType.TEXT),
    ]
    self.assertEqual(actual, expected)

  def test_one_image_at_end(self):
    node = TextNode("Before image ![image](https://i.imgur.com/zjjcJKZ.png)", TextType.TEXT)
    actual = split_nodes_image([node])
    expected = [
      TextNode("Before image ", TextType.TEXT),
      TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
    ]
    self.assertEqual(actual, expected)

  def test_one_image_alone(self):
    node = TextNode("![image](https://i.imgur.com/zjjcJKZ.png)", TextType.TEXT)
    actual = split_nodes_image([node])
    expected = [TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png")]
    self.assertEqual(actual, expected)

  def test_two_images(self):
    node = TextNode("Beginning ![image1](https://i.imgur.com/zjjcJKZ.png) middle ![image2](https://i.imgur.com/zxxcJKZ.png) end", TextType.TEXT)
    actual = split_nodes_image([node])
    expected = [
      TextNode("Beginning ", TextType.TEXT),
      TextNode("image1", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
      TextNode(" middle ", TextType.TEXT),
      TextNode("image2", TextType.IMAGE, "https://i.imgur.com/zxxcJKZ.png"),
      TextNode(" end", TextType.TEXT),
    ]
    self.assertEqual(actual, expected)


class TestSplitNodesLinks(unittest.TestCase):
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