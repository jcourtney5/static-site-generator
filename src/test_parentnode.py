import unittest

from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
  def test_to_html_four_children(self):
    node = ParentNode(
      "p",
      [
          LeafNode("b", "Bold text"),
          LeafNode(None, "Normal text"),
          LeafNode("i", "italic text"),
          LeafNode(None, "Normal text"),
      ],
    )
    expected = "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
    self.assertEqual(node.to_html(), expected)


  def test_to_html_one_child(self):
    child_node = LeafNode("span", "child")
    parent_node = ParentNode("div", [child_node])
    self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")


  def test_to_html_with_grandchildren(self):
    grandchild_node = LeafNode("b", "grandchild")
    child_node = ParentNode("span", [grandchild_node])
    parent_node = ParentNode("div", [child_node])
    self.assertEqual(
        parent_node.to_html(),
        "<div><span><b>grandchild</b></span></div>",
    )


  def test_to_html_no_tag(self):
    child_node = LeafNode("b", "child")
    node = ParentNode(None, [child_node])
    self.assertRaises(ValueError, node.to_html)


  def test_to_html_no_children_none(self):
    node = ParentNode("div", None)
    self.assertRaises(ValueError, node.to_html)


  def test_to_html_no_children_empty_array(self):
    node = ParentNode("div", [])
    self.assertRaises(ValueError, node.to_html)