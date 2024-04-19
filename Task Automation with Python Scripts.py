import os
import shutil

def organize_files(source_dir, destination_dir):
    # Create the destination directory if it doesn't exist
    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)

    # Get a list of all files in the source directory
    files = os.listdir(source_dir)

    # Iterate through each file and move it to the appropriate folder based on its extension
    for file in files:
        if os.path.isfile(os.path.join(source_dir, file)):
            file_extension = os.path.splitext(file)[1]
            destination_folder = os.path.join(destination_dir, file_extension[1:].lower())
            if not os.path.exists(destination_folder):
                os.makedirs(destination_folder)
            shutil.move(os.path.join(source_dir, file), os.path.join(destination_folder, file))

if __name__ == "__main__":
    source_directory = "source_directory_path"
    destination_directory = "destination_directory_path"
    organize_files(source_directory, destination_directory)
    print("Files organized successfully!")
