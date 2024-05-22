import os

def rename_files(directory, prefix, include_subdirs=False):
  """
  Renames files in a directory with a specified prefix.

  Args:
    directory: Path to the directory containing files to rename.
    prefix: String to prepend to filenames.
    include_subdirs: Boolean flag indicating whether to rename files in subdirectories.
  """
  for filename in os.listdir(directory):
    # Skip hidden files and directories
    if filename.startswith('.'):
      continue
    filepath = os.path.join(directory, filename)
    # Construct new filename with prefix
    new_filename = os.path.join(directory, prefix + filename)
    # Rename the file
    os.rename(filepath, new_filename)

    # Recursively rename files in subdirectories (if enabled)
    if include_subdirs and os.path.isdir(filepath):
      rename_files(filepath, prefix, include_subdirs)

if __name__ == "__main__":
  # Get user input
  directory = input("Enter directory path: ")
  prefix = input("Enter prefix to add: ")
  include_subdirs = input("Rename files in subdirectories? (y/n): ").lower() == 'y'

  # Validate input (optional)

  # Call rename function
  rename_files(directory, prefix, include_subdirs)
  print("Files renamed successfully!")
  
