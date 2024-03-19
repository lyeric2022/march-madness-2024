# Declare the input and output file paths
input_file_path = 'day-1\day1_input.txt'
output_file_path = 'day-1\day1a_result.txt'

# Initialize a counter for the STOP statuses
stop_count = 0

# Open the input file and read line by line
with open(input_file_path, 'r') as file:
    for line in file:
        # Count the number of STOP statuses
        if '[STOP]' in line:
            stop_count += 1

print(f"Number of services to boot up: {stop_count}")

with open(output_file_path, 'w') as file:
    file.write(str(stop_count))
