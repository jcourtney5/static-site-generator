import re

def extract_title(markdown):
  lines = markdown.splitlines()

  # check all lines until we find it
  for line in lines:
    if line.startswith("# "):
        return line[2:]

  # if not found, raise an error
  raise Exception("Could not find h1 title that starts with '# '")