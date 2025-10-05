import unittest

from extract_markdown_images import extract_markdown_images

class TestExtractMarkdownImages(unittest.TestCase):
  def test_two_images(self):
    text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
    actual = extract_markdown_images(text)
    expected = [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]
    self.assertEqual(actual, expected)

  def test_one_image(self):
    text = "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
    actual = extract_markdown_images(text)
    expected = [("image", "https://i.imgur.com/zjjcJKZ.png")]
    self.assertEqual(actual, expected)

  def test_no_images(self):
    text = "This is text with no image"
    actual = extract_markdown_images(text)
    expected = []
    self.assertEqual(actual, expected)
