from textnode import TextNode, TextType

def main():
  # test creating a TextNode
  textNode1 = TextNode("sample text", TextType.ITALIC, None)
  print(f"textNode1: {textNode1}")

  textNode2 = TextNode("link to an image", TextType.IMAGE, "http://imageurl.jpg")
  print(f"textNode2: {textNode2}")

if __name__ == "__main__":
    main()