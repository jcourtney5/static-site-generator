import re

def extract_markdown_images(text):
  # from course tips: r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
  matches = re.findall(r"!\[(.*?)\]\((.*?)\)", text)
  return matches