import os

i = 1
filesRenamed = False

directoryInput = input('Enter path to your folder: ')
directory = directoryInput.replace("\\", "/")
print(f"Your path is: {directory}")

fileType = input('\nWhat file type do you want to rename? ')
print(f"You selected .{fileType}")

name = input('What do you want to call the file? ')
print(f"The name of the file(s) will now be: {name}")

print()

for filename in os.listdir(directory):
    file_name, file_ext = os.path.splitext(filename)

    if file_ext.lower() == f".{fileType}":
        old_file_path = os.path.join(directory, filename)
        # new_file_path = os.path.join(directory, f"{name}-{file_name}.{fileType}")
        new_file_path = os.path.join(directory, f"{name}-{i}-old.{fileType}")
        os.rename(old_file_path, new_file_path)
        i += 1
        print(f"Renamed: {filename}")
        filesRenamed = True


if filesRenamed == True:
    print("\nRenaming complete!")
else:
    print(f'No files were renamed. Make sure the file type you selected exists in the folder')