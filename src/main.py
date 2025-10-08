import os
import shutil

from generate_pages_recursive import generate_pages_recursive

def main():
  build_public_folder()
  build_html_from_content()


def build_public_folder():
  root_dir = os.getcwd()

  # get full paths
  public_folder = os.path.join(root_dir, 'public')
  static_folder = os.path.join(root_dir, 'static')

  # delete public folder and recreate it
  if os.path.exists(public_folder):
    shutil.rmtree(public_folder)
  os.mkdir(public_folder)
  print("cleared public folder")

  # copy entire contents from static to public
  copy_files(static_folder, public_folder)


def copy_files(source_dir, dest_dir):
  items = os.listdir(source_dir)
  for item in items:
    # get full paths
    item_source_full_path = os.path.join(source_dir, item)
    item_dest_full_path = os.path.join(dest_dir, item)

    if os.path.isfile(item_source_full_path):
      # if it is a file, just copy it
      print(f"copying {item_source_full_path} to {item_dest_full_path}")
      shutil.copy(item_source_full_path, item_dest_full_path)
    else:
      # if it is a folder, then create dest folder and recursively call copy_files
      print(f"making dir {item_dest_full_path}")
      os.mkdir(item_dest_full_path)
      copy_files(item_source_full_path, item_dest_full_path)


def build_html_from_content():
  root_dir = os.getcwd()

  dir_path_content = os.path.join(root_dir, 'content')
  template_path = os.path.join(root_dir, 'template.html')
  dest_dir_path = os.path.join(root_dir, 'public')

  generate_pages_recursive(dir_path_content, template_path, dest_dir_path)

if __name__ == "__main__":
    main()