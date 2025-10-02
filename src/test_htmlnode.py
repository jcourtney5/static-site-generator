import unittest

from htmlnode import HtmlNode


class TestHtmlNode(unittest.TestCase):
  def test_repr_tag_value(self):
    node = HtmlNode(tag="tag", value="value", children=None, props=None)
    node_str = str(node)
    self.assertEqual(node_str, "tag: tag, value: value, props: ")

  def test_props_to_html_none(self):
    node = HtmlNode(tag=None, value=None, children=None, props=None)
    props_html = node.props_to_html()
    self.assertEqual(props_html, "")

  def test_props_to_html_two_items(self):
    node = HtmlNode(tag=None, value=None, children=None, props={"a": "1", "b": "2"})
    props_html = node.props_to_html()
    self.assertEqual(props_html, ' a="1" b="2"')

  def test_children_two(self):
    child1 = HtmlNode(tag="tag1", value="value1", children=None, props=None)
    child2 = HtmlNode(tag="tag2", value="value2", children=None, props=None)
    node = HtmlNode(tag=None, value=None, children=[child1, child2], props=None)
    
    node_str = str(node)
    expected = """tag: , value: , props: 
- child: tag: tag1, value: value1, props: 
- child: tag: tag2, value: value2, props: """

    self.assertEqual(node_str, expected)

if __name__ == "__main__":
  unittest.main()