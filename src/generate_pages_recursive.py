import os

from generate_page import generate_page

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
  items = os.listdir(dir_path_content)
  for item in items:
    item_full_path = os.path.join(dir_path_content, item)

    if os.path.isfile(item_full_path):
      # if it is a markdown file, convert it
      if item.endswith(".md"):
        # get filename with no extension
        item_no_ext = item[:-3]

        # get destination file as html and make sure directory is created
        dest_file_full_path = os.path.join(dest_dir_path, item_no_ext + ".html")
        os.makedirs(dest_dir_path, exist_ok=True)

        # call generate_path
        generate_page(item_full_path, template_path, dest_file_full_path)
    else:
      # if it is a folder, call generate_pages_recursive on sub folder
      dest_dir_full_path = os.path.join(dest_dir_path, item) 
      generate_pages_recursive(item_full_path, template_path, dest_dir_full_path)