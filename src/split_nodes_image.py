from textnode import TextNode, TextType
from extract_markdown_images import extract_markdown_images

def split_nodes_image(old_nodes):
  new_nodes = []

  for old_node in old_nodes:
    # just add any non text nodes to the new list, no splitting needed
    if old_node.text_type != TextType.TEXT:
      new_nodes.append(old_node)
      continue

    images = extract_markdown_images(old_node.text)

    if len(images) == 0:
      new_nodes.append(old_node)
      continue

    remaining_text = old_node.text

    for image_alt, image_link in images:
      # get any text before and after image
      parts = remaining_text.split(f"![{image_alt}]({image_link})", 1)

      # get text before if any
      if len(parts) > 0 and len(parts[0]) > 0:
        new_nodes.append(TextNode(parts[0], TextType.TEXT))

      # add the actual image node
      new_nodes.append(TextNode(image_alt, TextType.IMAGE, image_link))

      # set rest of text to remaining_text for next loop
      if len(parts) > 1:
        remaining_text = parts[1]
      else:
        # set to blank in case there are more loops with more images
        remaining_text = ""

    # add any remaining text as a final TEXT node
    if len(remaining_text) > 0:
      new_nodes.append(TextNode(remaining_text, TextType.TEXT))

  return new_nodes