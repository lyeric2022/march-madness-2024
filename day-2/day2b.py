# Declare the file paths
input_file_path = r'day-2\day2_input.txt'
output_file_path = r'day-2\day2b_result.txt'

# Initialize crate size
crate_size = 15

# Initialize floor plan
floor_plan = []

# Open the input file and read line by line
with open(input_file_path, 'r') as file:
    floor_plan = [line.strip() for line in file]

# Define a function to count the number of different places to fit the crate   
def num_fit_crate(floor_plan, crate_size):
    result = 0
    
    rows = len(floor_plan)
    cols = len(floor_plan[0])
    
    for x in range(0, rows - crate_size + 1):
        for y in range(0, cols - crate_size + 1):
            # Assume the crate fits
            crate_fits = True
            
            # Check if the crate fits
            for i in range(crate_size):
                for j in range(crate_size):
                    if floor_plan[x + i][y + j] != '.':
                        crate_fits = False
                        break
                if not crate_fits:
                    break
                
            # If the crate fits, increase the result
            if crate_fits:
                result += 1

    return result


# Call the function to count the number of different places to fit the crate
result = num_fit_crate(floor_plan, crate_size)

# Print the result
print(f"Number of different places to fit crate: {result}")

with open(output_file_path, 'w') as file:
    file.write(str(result))  # Write each line followed by a newline character
