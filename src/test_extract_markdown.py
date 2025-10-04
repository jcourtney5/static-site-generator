import unittest

from extract_markdown import extract_markdown_images, extract_markdown_links

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


class TestExtractMarkdownLinks(unittest.TestCase):
  def test_two_links(self):
    text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
    actual = extract_markdown_links(text)
    expected = [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")]
    self.assertEqual(actual, expected)

  def test_one_link(self):
    text = "This is text with a link [link1](https://link.to.website/url123)"
    actual = extract_markdown_links(text)
    expected = [("link1", "https://link.to.website/url123")]
    self.assertEqual(actual, expected)

  def test_no_links(self):
    text = "This is text without a link"
    actual = extract_markdown_links(text)
    expected = []
    self.assertEqual(actual, expected)