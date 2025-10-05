from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
  new_nodes = []

  for old_node in old_nodes:
    # just add any non text nodes to the new list, no splitting needed
    if old_node.text_type != TextType.TEXT:
      new_nodes.append(old_node)
      continue

    parts = old_node.text.split(delimiter)
    
    for i, part in enumerate(parts):
      # even indexes should be the regular text, odd the text_type
      if i % 2 == 0:
        if len(part) > 0:
          new_nodes.append(TextNode(part, TextType.TEXT))
      else:
        # if we reached the end, that means it is missing a closing tag so throw an error
        if i == len(parts) - 1:
          raise Exception(f"Error: malformed markup is missing end tag for {delimiter}")
        new_nodes.append(TextNode(part, text_type))

  return new_nodes
