import unittest

from markdown_to_html_node import markdown_to_html_node

class TestMarkdownToHtmlNode(unittest.TestCase):
  def test_paragraph_simple(self):
    md = """
Simple paragraph with one line
"""
    node = markdown_to_html_node(md)
    html = node.to_html()
    self.assertEqual(
        html,
        "<div><p>Simple paragraph with one line</p></div>",
    )

  def test_paragraph_complex(self):
    md = md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""
    node = markdown_to_html_node(md)
    html = node.to_html()
    self.assertEqual(
        html,
        "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
    )

  def test_heading_1_simple(self):
    md = """
# Heading
"""
    node = markdown_to_html_node(md)
    html = node.to_html()
    self.assertEqual(
        html,
        "<div><h1>Heading</h1></div>",
    )

  def test_heading_3_simple(self):
    md = """
### Heading
"""
    node = markdown_to_html_node(md)
    html = node.to_html()
    self.assertEqual(
        html,
        "<div><h3>Heading</h3></div>",
    )

  def test_heading_6_simple(self):
    md = """
###### Heading
"""
    node = markdown_to_html_node(md)
    html = node.to_html()
    self.assertEqual(
        html,
        "<div><h6>Heading</h6></div>",
    )

  def test_heading_1_inline_elements(self):
    md = """
# Heading **bold text** _italics text_ `code here`
"""
    node = markdown_to_html_node(md)
    html = node.to_html()
    self.assertEqual(
        html,
        "<div><h1>Heading <b>bold text</b> <i>italics text</i> <code>code here</code></h1></div>",
    )

  def test_codeblock(self):
    md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""
    node = markdown_to_html_node(md)
    html = node.to_html()
    self.assertEqual(
        html,
        "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
    )

  def test_quote_single_line(self):
    md = """
> This is a quote line
"""
    node = markdown_to_html_node(md)
    html = node.to_html()
    self.assertEqual(
        html,
        "<div><blockquote>This is a quote line</blockquote></div>",
    )

  def test_quote_multiple_lines_inline_elements(self):
    md = """
> Quote line 1 **bold text**
> Quote line 2 _italics text_
> Quote line 3 `code here`
> Quote line 4
"""
    node = markdown_to_html_node(md)
    html = node.to_html()
    self.assertEqual(
        html,
        "<div><blockquote>Quote line 1 <b>bold text</b> Quote line 2 <i>italics text</i> Quote line 3 <code>code here</code> Quote line 4</blockquote></div>",
    )

  def test_unordered_list(self):
    md = """
- Item 1
- Item 2
- Item 3
"""
    node = markdown_to_html_node(md)
    html = node.to_html()
    self.assertEqual(
        html,
        "<div><ul><li>Item 1</li><li>Item 2</li><li>Item 3</li></ul></div>",
    )

  def test_unordered_list_inline_elements(self):
    md = """
- **Bold** Item
- _Italics_ Item
- Item 3 `code here`
"""
    node = markdown_to_html_node(md)
    html = node.to_html()
    self.assertEqual(
        html,
        "<div><ul><li><b>Bold</b> Item</li><li><i>Italics</i> Item</li><li>Item 3 <code>code here</code></li></ul></div>",
    )

  def test_ordered_list(self):
    md = """
1. Item 1
2. Item 2
3. Item 3
"""
    node = markdown_to_html_node(md)
    html = node.to_html()
    self.assertEqual(
        html,
        "<div><ol><li>Item 1</li><li>Item 2</li><li>Item 3</li></ol></div>",
    )

  def test_ordered_list_inline_elements(self):
    md = """
1. **Bold** Item
2. _Italics_ Item
3. Item 3 `code here`
"""
    node = markdown_to_html_node(md)
    html = node.to_html()
    self.assertEqual(
        html,
        "<div><ol><li><b>Bold</b> Item</li><li><i>Italics</i> Item</li><li>Item 3 <code>code here</code></li></ol></div>",
    )