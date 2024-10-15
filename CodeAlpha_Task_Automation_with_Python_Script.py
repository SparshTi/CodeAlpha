import os
import shutil

def organize_files(directory):
    for filename in os.listdir(directory):
        if os.path.isdir(os.path.join(directory, filename)):
            continue
        
        file_extension = filename.split('.')[-1]
        new_directory = os.path.join(directory, file_extension)
        
        if not os.path.exists(new_directory):
            os.makedirs(new_directory)
        
        old_file_path = os.path.join(directory, filename)
        new_file_path = os.path.join(new_directory, filename)
        shutil.move(old_file_path, new_file_path)
        print(f'Moved: {filename} to {new_directory}')

if __name__ == "__main__":
    directory = "/Users/sparshtyagi/Documents/python vs code/untitled folder"
    organize_files(directory)
    print("File organization complete!")
