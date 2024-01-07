import os
import random
import csv

def randomly_select_lines(folder_path, num_lines):
    selected_lines = []

    # Get a list of all text files in the specified folder
    txt_files = [file for file in os.listdir(folder_path) if file.endswith(".txt")]

    # Check if there are any text files in the folder
    if not txt_files:
        print("No text files found in the specified folder.")
        return selected_lines

    total_unique_lines = 0  # Counter for total unique non-empty lines in all text files

    # Iterate through each text file
    for txt_file in txt_files:
        file_path = os.path.join(folder_path, txt_file)

        # Read the lines from the text file
        with open(file_path, 'r', encoding='ISO-8859-1') as file:
            lines = file.readlines()

            # Filter out empty lines
            non_empty_lines = [line.strip() for line in lines if line.strip()]

            # Update the counter for total unique non-empty lines
            total_unique_lines += len(set(non_empty_lines))

            # Update the list with tuples containing file name and non-empty lines from the current file
            selected_lines.extend([(txt_file, line) for line in non_empty_lines])

    # Randomly select lines from the combined list of file name and non-empty lines
    random_lines = random.sample(selected_lines, min(num_lines, len(selected_lines)))

    # Print the total number of unique non-empty lines in all text files
    print(f"Total unique non-empty lines in all text files: {total_unique_lines}")

    # Print the number of files selected
    print(f"Number of files selected: {len(txt_files)}")

    # Print the number of lines randomly selected
    print(f"Number of lines randomly selected: {len(random_lines)}")

    return random_lines

# Specify the folder path and the number of lines to randomly select
folder_path = "/mnt/d/github/user_story/Data/All_Text_Files"
num_lines_to_select = 100

# Call the function to get the randomly selected lines
random_lines = randomly_select_lines(folder_path, num_lines_to_select)

# Specify the output CSV file path
csv_output_file_path = "/mnt/d/github/user_story/Data/randomly_selected_lines.csv"
# Specify the output text file path
text_output_file_path = "/mnt/d/github/user_story/Data/randomly_selected_lines.txt"

# Open the CSV file in write mode
with open(csv_output_file_path, 'w', newline='', encoding='utf-8') as csv_output_file:
    # Create a CSV writer
    csv_writer = csv.writer(csv_output_file)

    # Write the header
    csv_writer.writerow(['File Name', 'Line'])

    # Write each randomly selected line along with the file name to the CSV file
    csv_writer.writerows(random_lines)

print(f"Randomly selected lines with file names have been written to CSV: {csv_output_file_path}")

# Open the text file in write mode
with open(text_output_file_path, 'w', encoding='utf-8') as text_output_file:
    # Write each randomly selected line along with the file name to the text file
    for file_name, line in random_lines:
        text_output_file.write(f"{file_name}: {line}\n")

print(f"Randomly selected lines with file names have been written to text file: {text_output_file_path}")

import csv

# Input CSV file path (previous output file)
input_csv_path = "/mnt/d/github/user_story/Data/randomly_selected_lines.csv"

# Output CSV file path (new modified file)
output_csv_path = "/mnt/d/github/user_story/Data/modified_selected_lines.csv"

# Read the input CSV file
with open(input_csv_path, 'r', encoding='utf-8') as input_csv_file:
    csv_reader = csv.reader(input_csv_file)
    header = next(csv_reader)  # Read the header

    # Initialize lists for the modified columns
    modified_first_column = []
    modified_second_column = []
    original_third_column = []

    # Process each row in the CSV file
    for row in csv_reader:
        # Modify the content of the first column
        original_file_name = row[0]
        modified_first_column.append(original_file_name)

        # Modify the content of the second column
        modified_second_column.append(original_file_name.replace(".txt", "").split('-')[-1])

        # Store the content of the second column in the third column list
        original_third_column.append(row[1])

# Write the modified data to the new CSV file
with open(output_csv_path, 'w', newline='', encoding='utf-8') as output_csv_file:
    csv_writer = csv.writer(output_csv_file)

    # Write the header
    csv_writer.writerow(['Original First Column', 'Modified Second Column', 'Original Third Column'])

    # Write the modified data to the CSV file
    csv_writer.writerows(zip(modified_first_column, modified_second_column, original_third_column))

print(f"Modified data has been written to: {output_csv_path}")


import csv

# Input CSV file path (new modified file)
input_csv_path = "/mnt/d/github/user_story/Data/modified_selected_lines.csv"

# Output CSV file path (final modified file)
output_csv_path = "/mnt/d/github/user_story/Data/final_modified_lines.csv"

# Read the input CSV file
with open(input_csv_path, 'r', encoding='utf-8') as input_csv_file:
    csv_reader = csv.reader(input_csv_file)
    header = next(csv_reader)  # Read the header

    # Initialize lists for the modified columns
    original_first_column = []
    modified_second_column = []
    original_third_column = []

    # Process each row in the CSV file
    for row in csv_reader:
        # Store the content of the first column in the list
        original_first_column.append(row[0])

        # Modify the content of the second column
        modified_second_column.append(row[1].replace("User Stories for Library Management System", "Library Management System").replace("User Stories for Restaurant Management System", "Restaurant Management System"))

        # Store the content of the third column in the list
        original_third_column.append(row[2])

# Write the final modified data to the new CSV file
with open(output_csv_path, 'w', newline='', encoding='utf-8') as output_csv_file:
    csv_writer = csv.writer(output_csv_file)

    # Write the header
    csv_writer.writerow(['Original First Column', 'Modified Second Column', 'Original Third Column'])

    # Write the final modified data to the CSV file
    csv_writer.writerows(zip(original_first_column, modified_second_column, original_third_column))

print(f"Final modified data has been written to: {output_csv_path}")



# Input CSV file path (final modified file)
input_csv_path = "/mnt/d/github/user_story/Data/final_modified_lines.csv"

# Output CSV file path (renamed final modified file)
output_csv_path = "/mnt/d/github/user_story/Data/renamed_final_modified_lines.csv"

# Read the final modified CSV file
with open(input_csv_path, 'r', encoding='utf-8') as input_csv_file:
    csv_reader = csv.reader(input_csv_file)
    header = next(csv_reader)  # Read the header

    # Initialize lists for the modified columns
    original_first_column = []
    modified_second_column = []
    original_third_column = []

    # Process each row in the CSV file
    for row in csv_reader:
        # Store the content of the first column in the list
        original_first_column.append(row[0])

        # Store the content of the second column in the list
        modified_second_column.append(row[1])

        # Store the content of the third column in the list
        original_third_column.append(row[2])

# Write the renamed final modified data to the new CSV file
with open(output_csv_path, 'w', newline='', encoding='utf-8') as output_csv_file:
    csv_writer = csv.writer(output_csv_file)

    # Write the updated header
    csv_writer.writerow(['File Name', 'Project Name', 'Random Line'])

    # Write the renamed final modified data to the CSV file
    csv_writer.writerows(zip(original_first_column, modified_second_column, original_third_column))

print(f"Renamed final modified data has been written to: {output_csv_path}")