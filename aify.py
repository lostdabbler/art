# This script adds invisible AI markers to a text file and replaces
# all hyphens with em dashes, preserving the original formatting.
#
# The output is saved to a new file with "_ai" added to the name.
#
# Usage: python aiify.py <path_to_file>

import sys
import os

def process_file(file_path):
    """
    Processes a file to add invisible markers and replace hyphens.

    Args:
        file_path (str): The path to the file to be processed.
    """
    print(f"✅ Starting script for file: '{file_path}'")

    # Check if the file exists and is readable
    if not os.path.exists(file_path) or not os.access(file_path, os.R_OK):
        print(f"❌ Error: File '{file_path}' not found or is not readable.")
        sys.exit(1)

    print("✅ File found. Proceeding with marking and dash replacement.")

    # Define the invisible characters and the em dash
    invisible_marker_a = "\u200b" # Zero-Width Space
    invisible_marker_b = "\u200c" # Zero-Width Non-Joiner
    em_dash = "—"

    # Create the new filename
    base, ext = os.path.splitext(file_path)
    output_file_path = f"{base}_ai{ext}"
    print(f"✅ New output file name generated: '{output_file_path}'")

    try:
        # Open the input and output files
        with open(file_path, 'r', encoding='utf-8') as infile, \
             open(output_file_path, 'w', encoding='utf-8') as outfile:

            counter = 0
            # Read the file line by line to preserve formatting
            for line in infile:
                # Iterate through each character in the line
                for char in line:
                    # Replace hyphen with em dash
                    if char == "-":
                        char = em_dash
                    
                    # Write the character and an invisible marker
                    outfile.write(char)
                    
                    if counter % 2 == 0:
                        outfile.write(invisible_marker_a)
                    else:
                        outfile.write(invisible_marker_b)
                    
                    counter += 1

        print("✅ All characters processed and written to the new file.")
        print(f"✅ Success! A new file has been created at:\n{output_file_path}")

    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Error: Please provide a single file path as an argument.")
        print("Usage: python aiify.py <path_to_file>")
        sys.exit(1)
    
    file_to_process = sys.argv[1]
    process_file(file_to_process)
