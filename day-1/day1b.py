# Declare the input and output file paths
input_file_path = 'day-1\day1_input.txt'
output_file_path = 'day-1\day1b_result.txt'

# Initialize a counter for the STOP, line count and final result
line_count = 0
stop_count = 0
final_result = 0

# Open the input file and read line by line
with open(input_file_path, 'r') as file:
    for line in file:
        # Count the number of STOP statuses
        if '[STOP]' in line:
            stop_count += 1
        # Count the number of lines
        line_count += 1

# Calculate the final result
final_result = line_count + stop_count

print(f"Number of total restarts: {final_result}")

with open(output_file_path, 'w') as file:
    file.write(str(final_result))
