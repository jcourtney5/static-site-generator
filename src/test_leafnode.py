import unittest

from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
  def test_leaf_to_html_value_only(self):
    node = LeafNode(tag=None, value="test value")
    self.assertEqual(node.to_html(), "test value")


  def test_leaf_to_html_no_value_error(self):
    node = LeafNode(tag="p", value=None)
    self.assertRaises(ValueError, node.to_html)
      

  def test_leaf_to_html_p(self):
    node = LeafNode("p", "Hello, world!")
    self.assertEqual(node.to_html(), "<p>Hello, world!</p>")


  def test_leaf_to_html_link(self):
    node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
    self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')


  def test_leaf_to_html_label(self):
    node = LeafNode("label", "Name:", {"for": "name"})
    self.assertEqual(node.to_html(), '<label for="name">Name:</label>')


  def test_leaf_to_html_input(self):
    node = LeafNode("input", "", {"type": "text", "id": "name", "name": "name", "placeholder": "Enter your name"})
    self.assertEqual(node.to_html(), '<input type="text" id="name" name="name" placeholder="Enter your name"></input>')