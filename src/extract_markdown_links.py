import re

def extract_markdown_links(text):
  # from course tips: r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
  matches = re.findall(r"\[(.*?)\]\((.*?)\)", text)
  return matches