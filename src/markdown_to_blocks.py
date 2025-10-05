

def markdown_to_blocks(markdown):
  blocks = []

  parts = markdown.split("\n\n")

  for part in parts:
    stripped = part.strip()
    if len(stripped) > 0:
      blocks.append(stripped)

  return blocks