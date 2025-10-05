import unittest

from split_nodes_image import split_nodes_image
from textnode import TextNode, TextType

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
