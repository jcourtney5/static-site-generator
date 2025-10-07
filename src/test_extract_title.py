import unittest

from extract_title import extract_title


class TestExtractTitle(unittest.TestCase):
  def test_no_h1(self):
    md = "Title, No H1"
    self.assertRaises(Exception, extract_title, md)
  
  def test_has_h1(self):
    md = "# Title"
    actual = extract_title(md)
    expected = "Title"
    self.assertEqual(actual, expected)

  def test_has_h2(self):
    md = "## Title"
    self.assertRaises(Exception, extract_title, md)

  def test_no_space(self):
    md = "#Title"
    self.assertRaises(Exception, extract_title, md)

  def test_mutli_line(self):
    md = """
# Title
more content1
more contnet2
"""
    actual = extract_title(md)
    expected = "Title"
    self.assertEqual(actual, expected)