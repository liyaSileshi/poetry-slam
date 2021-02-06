#!python

from poetry_slam import get_file_lines, lines_printed_backwards
import unittest
import io
import unittest.mock
from unittest.mock import patch, call

class PoetrySlamTest(unittest.TestCase):
  
    def test_get_file_lines(self):
      filename = "poem.txt"
      poem_list = ['Remember the sky that you were born under,\n', "know each of the star's stories.\n", 'Remember the moon, know who she is.\n', "Remember the sun's birth at dawn, that is the\n", 'strongest point of time. Remember sundown\n', 'and the giving away to night.\n']
      assert get_file_lines(filename) == poem_list

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def assert_stdout(self, lines_list, expected_output, mock_stdout):
        lines_printed_backwards(lines_list)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_lines_printed_backwards(self):
        filename = "poem.txt"
        poem_list = get_file_lines(filename)
        poem_list = []

        # poem_list = lines_printed_backwards(lines_list)
        # for i in reversed(range(len(poem_list))):
        #   curr = f'{i} {poem_list[i]}'

        expected_output = "5 and the giving away to night.\n\n4 strongest point of time. Remember sundown\n\n3 Remember the sun's birth at dawn, that is the\n\n2 Remember the moon, know who she is.\n\n1 know each of the star's stories.\n\n0 Remember the sky that you were born under,\n\n"
        self.assert_stdout(poem_list, expected_output)




    # @patch('builtins.print')
    # def test_lines_printed_backwards(self, mocked_print):
    #   filename = "poem.txt"
    #   lines_list = get_file_lines(filename)
    #   lines_printed_backwards(lines_list)
    #   print(type(mocked_print.mock_calls))
    #   assert mocked_print.mock_calls == [call("5 and the giving away to night.\n"),
    #   call('4 strongest point of time. Remember sundown\n'),
    #  call("3 Remember the sun's birth at dawn, that is the\n"),
    # call('2 Remember the moon, know who she is.\n'),
    #      call("1 know each of the star's stories.\n"),
    #  call('0 Remember the sky that you were born under,\n'),
      # ]






      # [call('foo'), call()]
    #   print("Remember the sky that you were born under,")
    #   print("know each of the star's stories.")
    #   print("Remember the moon, know who she is.")
    #   print("Remember the sun's birth at dawn, that is the")
    #   print("strongest point of time. Remember sundown")
    #   print("and the giving away to night.")

    #   # assert mocked_print.mock_calls == [call('food'), call()]
    #   lines_list = get_file_lines(filename)
    #   assert mocked_print.mock_calls == [call(lines_printed_backwards(lines_list=lines_list))]
      
      # assert lines_printed_backwards(lines_list) == 

# @patch('builtins.print')
# def test_print(mocked_print):
#     print('foo')
#     print()

#     assert mocked_print.mock_calls == [call('food'), call()]