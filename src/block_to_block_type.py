import re
from enum import Enum

class BlockType(Enum):
  PARAGRAPH = "paragraph"
  HEADING = "heading"
  CODE = "code"
  QUOTE = "quote"
  UNORDERED_LIST = "unordered_list"
  ORDERED_LIST = "ordered_list"

def block_to_block_type(block):
  # check heading
  match = re.match(r"^(#{1,6}) [^ ]", block)
  if match:
    return BlockType.HEADING
  
  # check code
  match = re.match(r"^```[\s\S]*```$", block)
  if match:
    return BlockType.CODE

  # # split into lines to check quote, unordered list and ordered list
  lines = block.splitlines()

  # check quote
  if all(line.startswith(">") for line in lines):
    return BlockType.QUOTE
  
  # check unorderd list
  if all(line.startswith("- ") for line in lines):
    return BlockType.UNORDERED_LIST
  
  # check ordered list
  if all(line.startswith(f"{i+1}. ") for i, line in enumerate(lines)):
    return BlockType.ORDERED_LIST

  # else, it is a paragraph
  return BlockType.PARAGRAPH