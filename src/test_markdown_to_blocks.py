import unittest

from markdown_to_blocks import markdown_to_blocks

class TestMarkdownToBlocks(unittest.TestCase):
  def test_markdown_to_blocks_three(self):
    md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
    blocks = markdown_to_blocks(md)
    self.assertEqual(
      blocks,
      [
        "This is **bolded** paragraph",
        "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
        "- This is a list\n- with items",
      ],
    )

  def test_markdown_to_blocks_one(self):
    md = """
This is **bolded** paragraph
"""
    blocks = markdown_to_blocks(md)
    self.assertEqual(blocks, ["This is **bolded** paragraph"])

  def test_markdown_to_blocks_one_extra_newlines_before_and_after(self):
    md = """


This is **bolded** paragraph


"""
    blocks = markdown_to_blocks(md)
    self.assertEqual(blocks, ["This is **bolded** paragraph"])


  def test_markdown_to_blocks_empty_string(self):
    md = ""
    blocks = markdown_to_blocks(md)
    self.assertEqual(blocks, [])