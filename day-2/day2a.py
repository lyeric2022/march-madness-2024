# Declare the file paths
input_file_path = 'day-2\day2_input.txt'
output_file_path = 'day-2\day2a_result.txt'

# Initialize a counter for the empty spaces
empty_spaces = 0

# Open the input file and read line by line
with open(input_file_path, 'r') as file:
    for line in file:
        # Count the number of empty spaces
        empty_spaces += line.count('.')


print(f"Number of empty spaces: {empty_spaces}")

with open(output_file_path, 'w') as file:
    file.write(str(empty_spaces))