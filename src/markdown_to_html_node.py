import re

from markdown_to_blocks import markdown_to_blocks
from block_to_block_type import block_to_block_type, BlockType
from text_to_text_nodes import text_to_text_nodes
from text_node_to_html_node import text_node_to_html_node
from parentnode import ParentNode
from textnode import TextNode, TextType


def markdown_to_html_node(markdown):
  # split the markdown into blocks
  blocks = markdown_to_blocks(markdown)

  # get html node for each block
  htmlnodes = []
  for block in blocks:
    htmlnode = block_to_html_node(block)
    htmlnodes.append(htmlnode)

  # wrap all nodes in a root parent div
  return ParentNode("div", htmlnodes)


def block_to_html_node(block):
  block_type = block_to_block_type(block)

  if block_type not in block_to_html_converters:
    raise Exception(f"block_to_html_node, unknown block_type: {block_type}")

  return block_to_html_converters[block_type](block)


# splits inline text into list of html child nodes 
def text_to_children(block):
  # split text into any markdown nodes
  text_nodes = text_to_text_nodes(block)

  # convert each markdown node into htmlnodes
  htmlnodes = []
  for text_node in text_nodes:
    htmlnode = text_node_to_html_node(text_node)
    htmlnodes.append(htmlnode)

  return htmlnodes


def paragraph_to_html_node(block):
  # replace newline chars with spaces
  block_no_line_breaks = block.replace("\n", " ")

  # convert text to inline list of child nodes
  htmlnodes = text_to_children(block_no_line_breaks)

  # wrap in a parent <p> tag
  return ParentNode("p", htmlnodes)


def heading_to_html_node(block):
  # count number of #'s at the beginning
  match = re.match(r'^(#{1,6}) ', block)  # up to 6 hashes followed by exactly one space
  num_hashes = len(match.group(1)) if match else 0

  # get remaining text
  text = block[num_hashes+1:]

  # convert text to inline list of child nodes
  htmlnodes = text_to_children(text)

  # wrap in a heading <h> tag
  return ParentNode(f"h{num_hashes}", htmlnodes)


def code_to_html_node(block):
  # remove first and last lines which contain the code fenct (ex: ```)
  lines = block.splitlines()
  lines_first_last_removed = lines[1:-1]
  code_text = "\n".join(lines_first_last_removed) + "\n"

  # don't split any inline formatting elements, use text in code block as is
  text_node = TextNode(code_text, TextType.TEXT)
  htmlnode = text_node_to_html_node(text_node)

  # wrap in <pre> and <code> nodes
  code_node = ParentNode("code", [htmlnode])
  return ParentNode("pre", [code_node])


def quote_to_html_node(block):
  # remove ">" and whitespace from each line, 
  lines = block.splitlines()
  new_lines = [line[1:].strip() for line in lines]

  # combine all lines with " " to remove nelines (\n)
  quote_text = " ".join(new_lines)

  # convert text to inline list of child nodes
  htmlnodes = text_to_children(quote_text)

  # wrap in a heading <h> tag
  return ParentNode("blockquote", htmlnodes)


def unordered_list_to_html_node(block):
  lines = block.splitlines()

  li_nodes = []
  for line in lines:
    # remove "- ", split to child elements and put in li node
    line_text = line[2:]
    htmlnodes = text_to_children(line_text) 
    li_nodes.append(ParentNode("li", htmlnodes))

  # wrap in a heading <ul> tag
  return ParentNode("ul", li_nodes)


def ordered_list_to_html_node(block):
  lines = block.splitlines()

  li_nodes = []
  for i, line in enumerate(lines):
    # remove "<num>. ", split to child elements and put in li node
    line_text = line.removeprefix(f"{i+1}. ")
    htmlnodes = text_to_children(line_text) 
    li_nodes.append(ParentNode("li", htmlnodes))

  # wrap in a heading <ol> tag
  return ParentNode("ol", li_nodes)


block_to_html_converters = {
  BlockType.PARAGRAPH: paragraph_to_html_node,
  BlockType.HEADING: heading_to_html_node,
  BlockType.CODE: code_to_html_node,
  BlockType.QUOTE: quote_to_html_node,
  BlockType.UNORDERED_LIST: unordered_list_to_html_node,
  BlockType.ORDERED_LIST: ordered_list_to_html_node,
}