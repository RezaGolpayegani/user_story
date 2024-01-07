import os
import random

def randomly_select_lines(folder_path, num_lines):
    selected_lines = set()

    # Get a list of all text files in the specified folder
    txt_files = [file for file in os.listdir(folder_path) if file.endswith(".txt")]

    # Check if there are any text files in the folder
    if not txt_files:
        print("No text files found in the specified folder.")
        return list(selected_lines)

    # Iterate through each text file
    for txt_file in txt_files:
        file_path = os.path.join(folder_path, txt_file)

        # Read the lines from the text file
        with open(file_path, 'r', encoding='ISO-8859-1') as file:
            lines = file.readlines()

            # Filter out empty lines
            non_empty_lines = [line.strip() for line in lines if line.strip()]

            # Update the set with non-empty lines from the current file
            selected_lines.update(non_empty_lines)

            # print(len(selected_lines))
            # After reading lines from each file, print the counts
            # print(f"Total lines in {txt_file}: {len(lines)}")
            # print(f"Non-empty lines in {txt_file}: {len(non_empty_lines)}")

    # Randomly select 100 lines from the combined set of non-empty lines
    selected_lines_list = list(selected_lines)
    # Print the total number of unique lines selected
    print(f"Total unique lines selected: {len(selected_lines)}")
    random_lines = random.sample(selected_lines_list, min(num_lines, len(selected_lines_list)))
    print(f"Number of lines selected: {len(random_lines)}")

    return random_lines

# Specify the folder path and the number of lines to randomly select
folder_path = "/mnt/d/github/user_story/Data/All_Text_Files"
num_lines_to_select = 100

# Call the function to get the randomly selected lines
random_lines = randomly_select_lines(folder_path, num_lines_to_select)



# Specify the output file path
output_file_path = "/mnt/d/github/user_story/Data/randomly_selected_lines.txt"



# Open the file in write mode
with open(output_file_path, 'w', encoding='utf-8') as output_file:
    # Write each randomly selected line to the file
    for line in random_lines:
        output_file.write(line + '\n')

print(f"Randomly selected lines have been written to: {output_file_path}")
