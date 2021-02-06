

# Create a function called get_file_lines():

# It should have 1 parameter called filename, which is a string of the filename.
# It should return a list of strings containing the lines of the file.
def get_file_lines(filename):
  file = open(filename, "r")
  lines = file.readlines()
  file.close()
  return lines


lines_list = get_file_lines("poem.txt")
# Create a function called lines_printed_backwards():
# It should have 1 parameter called lines_list, which is a list of strings 
# containing lines of your poem.
# It should print the lines of the poem in reverse. Include the original line
#  number at the beginning of each line.
def lines_printed_backwards(lines_list):
  for i in reversed(range(len(lines_list))):
    print(f"{i} {lines_list[i]}")


lines_printed_backwards(lines_list)
# Create a function called lines_printed_random():
# It should have 1 parameter called lines_list, which is a 
# list of strings containing lines of your poem.
# It should print the lines of your poem in randomly order. 
# Repeats are ok, but make sure the number of lines printed is 
# equal to the original lines in the poem (Line numbers do not need
# to be printed.) Hint: try using a loop and randint() from the random module.
def lines_printed_random(lines_list):
  return

