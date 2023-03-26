import os

# Get user input for directory path, file name, and file extension
dir_path = input("Enter directory path: ")
new_name = input("Enter new file name: ")
file_ext = input("Enter file extension to match (e.g. .txt): ")

# Loop through files in directory and rename matching files
count = 0
for filename in os.listdir(dir_path):
    if filename.endswith(file_ext):
        # Construct new file name with incremented number
        new_filename = new_name + str(count) + file_ext
        # Rename file
        os.rename(os.path.join(dir_path, filename), os.path.join(dir_path, new_filename))
        count += 1

print(f"Renamed {count} files")
