import os

from markdown_to_html_node import markdown_to_html_node
from extract_title import extract_title


def generate_page(from_path, template_path, dest_path):
  print(f"Generating page from {from_path} to {dest_path} using {template_path}")

  # read markdown file
  markdown = None
  with open(from_path, 'r') as file:
    markdown = file.read()

  # read template file
  template = None
  with open(template_path, 'r') as file:
    template = file.read()

  # convert markdown to html
  node = markdown_to_html_node(markdown)
  html = node.to_html()

  # get the title
  title = extract_title(markdown)

  # replace template content with title and html
  template_filled = template.replace("{{ Title }}", title).replace("{{ Content }}", html)

  # make sure dest dir exists
  dest_path_dir = os.path.dirname(dest_path)
  os.makedirs(dest_path_dir, exist_ok=True)

  # output file to dest_path
  with open(dest_path, "w") as file:
    file.write(template_filled)
