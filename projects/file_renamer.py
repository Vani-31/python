import os

def rename_text_files():
    # Get the current directory where the script is located
    # This ensures the script renames files in its own directory
    current_directory = os.getcwd()
    print(f"Working in directory: {current_directory}")

    # List all files and directories in the current folder
    files = os.listdir(current_directory)

    # Initialize a counter for the new file names
    note_number = 1

    print("Renaming files...")
    for filename in files:
        # Check if the file is a .txt file and not the script itself
        if filename.endswith(".txt") and filename != "file_renamer.py":
            old_filepath = os.path.join(current_directory, filename)
            new_filename = f"note{note_number}.txt"
            new_filepath = os.path.join(current_directory, new_filename)

            try:
                os.rename(old_filepath, new_filepath)
                print(f"Renamed '{filename}' to '{new_filename}'")
                note_number += 1
            except OSError as e:
                print(f"Error renaming '{filename}': {e}")
        elif filename == "rename_script.py":
            print(f"Skipping script file: {filename}")
        else:
            print(f"Skipping non-text file: {filename}")

    print("\nFile renaming complete!")

if __name__ == "__main__":
    rename_text_files()