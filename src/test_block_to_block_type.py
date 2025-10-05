import unittest

from block_to_block_type import block_to_block_type, BlockType

class TestBlockToBlockType(unittest.TestCase):
  def test_paragraph(self):
    block = "normal paragraph text"
    block_type = block_to_block_type(block)
    self.assertEqual(block_type, BlockType.PARAGRAPH)

  def test_heading_level_1(self):
    block = "# heading level 1"
    block_type = block_to_block_type(block)
    self.assertEqual(block_type, BlockType.HEADING)

  def test_heading_level_3(self):
    block = "### heading level 3"
    block_type = block_to_block_type(block)
    self.assertEqual(block_type, BlockType.HEADING)

  def test_heading_level_6(self):
    block = "###### heading level 6"
    block_type = block_to_block_type(block)
    self.assertEqual(block_type, BlockType.HEADING)

  def test_not_heading_no_space(self):
    block = "###heading level 3"
    block_type = block_to_block_type(block)
    self.assertEqual(block_type, BlockType.PARAGRAPH)

  def test_not_heading_two_spaces(self):
    block = "###  heading level 3"
    block_type = block_to_block_type(block)
    self.assertEqual(block_type, BlockType.PARAGRAPH)

  def test_not_heading_too_many_hashes(self):
    block = "####### heading level 6"
    block_type = block_to_block_type(block)
    self.assertEqual(block_type, BlockType.PARAGRAPH)


  def test_code_basic(self):
    block = "```code```"
    block_type = block_to_block_type(block)
    self.assertEqual(block_type, BlockType.CODE)

  def test_not_code_only_two_ticks_at_start(self):
    block = "``code```"
    block_type = block_to_block_type(block)
    self.assertEqual(block_type, BlockType.PARAGRAPH)

  def test_not_code_only_two_ticks_at_end(self):
    block = "```code``"
    block_type = block_to_block_type(block)
    self.assertEqual(block_type, BlockType.PARAGRAPH)

  def test_code_newlines(self):
    block = "```line1\nline2\nline3```"
    block_type = block_to_block_type(block)
    self.assertEqual(block_type, BlockType.CODE)

  def test_code_blank_spaces(self):
    block = "```  ```"
    block_type = block_to_block_type(block)
    self.assertEqual(block_type, BlockType.CODE)

  def test_not_code_ticks_not_at_start(self):
    block = "before```code```"
    block_type = block_to_block_type(block)
    self.assertEqual(block_type, BlockType.PARAGRAPH)

  def test_not_code_ticks_not_at_end(self):
    block = "```code```after"
    block_type = block_to_block_type(block)
    self.assertEqual(block_type, BlockType.PARAGRAPH)

  def test_quote_single_line(self):
    block = "> line1"
    block_type = block_to_block_type(block)
    self.assertEqual(block_type, BlockType.QUOTE)

  def test_quote_multiple_lines(self):
    block = "> line1\n> line2\n> line3"
    block_type = block_to_block_type(block)
    self.assertEqual(block_type, BlockType.QUOTE)

  def test_not_quote_one_line_missing_gt(self):
    block = "> line1\n line2\n> line3"
    block_type = block_to_block_type(block)
    self.assertEqual(block_type, BlockType.PARAGRAPH)

  def test_unordered_list_singlie_line(self):
    block = "- line1"
    block_type = block_to_block_type(block)
    self.assertEqual(block_type, BlockType.UNORDERED_LIST)

  def test_unordered_list_multiple_lines(self):
    block = "- line1\n- line2\n- line3"
    block_type = block_to_block_type(block)
    self.assertEqual(block_type, BlockType.UNORDERED_LIST)

  def test_not_unordered_list_missing_space(self):
    block = "- line1\n-line2\n- line3"
    block_type = block_to_block_type(block)
    self.assertEqual(block_type, BlockType.PARAGRAPH)

  def test_not_unordered_list_missing_dash(self):
    block = "- line1\n- line2\n line3"
    block_type = block_to_block_type(block)
    self.assertEqual(block_type, BlockType.PARAGRAPH)

  def test_ordered_list_singlie_line(self):
    block = "1. line1"
    block_type = block_to_block_type(block)
    self.assertEqual(block_type, BlockType.ORDERED_LIST)

  def test_ordered_list_multiple_lines(self):
    block = "1. line1\n2. line2\n3. line3"
    block_type = block_to_block_type(block)
    self.assertEqual(block_type, BlockType.ORDERED_LIST)

  def test_not_ordered_list_missing_space(self):
    block = "1. line1\n2.line2\n3. line3"
    block_type = block_to_block_type(block)
    self.assertEqual(block_type, BlockType.PARAGRAPH)

  def test_not_ordered_list_missing_number(self):
    block = "1. line1\n. line2\n3. line3"
    block_type = block_to_block_type(block)
    self.assertEqual(block_type, BlockType.PARAGRAPH)

  def test_not_ordered_list_missing_period(self):
    block = "1. line1\n2 line2\n3. line3"
    block_type = block_to_block_type(block)
    self.assertEqual(block_type, BlockType.PARAGRAPH)

  def test_not_ordered_list_bad_number_sequence(self):
    block = "1. line1\n3. line2\n2. line3"
    block_type = block_to_block_type(block)
    self.assertEqual(block_type, BlockType.PARAGRAPH)