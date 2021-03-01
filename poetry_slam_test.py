#!python

from  poetry_slam import (get_file_lines, lines_printed_backwards,
                        lines_printed_random)
import unittest
import io
import unittest.mock
from unittest.mock import patch, call

class PoetrySlamTest(unittest.TestCase):

  def test_get_file_lines_not_empty(self):
    filename = "poem.txt"
    poem_list = get_file_lines(filename)
    print(len(poem_list))
    assert len(poem_list) != 0

  def test_get_file_lines(self):
    """Tests the get_file_lines function."""
    filename = "poem.txt"
    mock_poem_list = ["Remember the sky that you were born under,\n",
                "know each of the star's stories.\n",
                "Remember the moon, know who she is.\n",
                "Remember the sun's birth at dawn, that is the\n",
                "strongest point of time. Remember sundown\n",
                "and the giving away to night.\n"]
    poem_list = get_file_lines(filename)
    assert len(poem_list) == len(mock_poem_list)
    assert poem_list == mock_poem_list

  @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
  def test_lines_printed_backwards(self, mock_stdout):
    """Tests the lines_printed_backwards function."""
    filename = "poem.txt"
    poem_list = get_file_lines(filename)
    expected_output = "5 and the giving away to night.\n\n4 strongest point of time. Remember sundown\n\n3 Remember the sun's birth at dawn, that is the\n\n2 Remember the moon, know who she is.\n\n1 know each of the star's stories.\n\n0 Remember the sky that you were born under,\n\n"
    lines_printed_backwards(poem_list)
    self.assertEqual(mock_stdout.getvalue(), expected_output)

  @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
  def test_lines_printed_random(self, mock_stdout):
    """Test the lines_printed_random function."""
    filename = "poem.txt"
    poem_list = get_file_lines(filename)
    non_random_output = "and the giving away to night.\n\nstrongest point of time. Remember sundown\n\nRemember the sun's birth at dawn, that is the\n\nRemember the moon, know who she is.\n\nknow each of the star's stories.\n\nRemember the sky that you were born under,\n\n"
    lines_printed_random(poem_list)
    self.assertNotEqual(mock_stdout.getvalue(), non_random_output)
