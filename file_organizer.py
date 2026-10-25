import os
import shutil
from pathlib import Path
from datetime import datetime

def organize_directory(target_dir):
    path = Path(target_dir)
    
    # Check if directory exists and is valid
    if not path.exists() or not path.is_dir():
        print(f"Error: The directory '{target_dir}' does not exist or is not a valid directory.")
        return

    print(f"Scanning and organizing directory: {path.resolve()}\n")
    
    file_count = 0
    
    try:
        # Scan files in the target directory
        for item in path.iterdir():
            # Skip directories, only process files
            if item.is_file():
                file_count += 1
                file_extension = item.suffix.lower()
                
                # If file has no extension, put it in 'No_Extension' folder
                if not file_extension:
                    folder_name = "No_Extension"
                else:
                    # Remove the dot from extension (e.g., '.jpg' becomes 'jpg')
                    folder_name = file_extension[1:] + "_files"
                
                # Create destination subfolder path
                subfolder_path = path / folder_name
                subfolder_path.mkdir(exist_ok=True)
                
                destination_path = subfolder_path / item.name
                
                # Handle filename conflicts (Never overwrite existing files)
                if destination_path.exists():
                    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                    new_filename = f"{item.stem}_{timestamp}{item.suffix}"
                    destination_path = subfolder_path / new_filename
                
                # Move the file safely
                try:
                    shutil.move(str(item), str(destination_path))
                    # Print clear summary of the move operation
                    print(f"[SUCCESS] Moved: '{item.name}'")
                    print(f"   Source      : {item}")
                    print(f"   Destination : {destination_path}\n")
                except PermissionError:
                    print(f"[ERROR] Permission denied for file: {item.name}\n")
                except Exception as e:
                    print(f"[ERROR] Could not move {item.name}. Reason: {e}\n")
                    
        if file_count == 0:
            print("The directory is empty. No files to organize.")
        else:
            print("File organization completed successfully!")

    except PermissionError:
        print(f"Error: Permission denied while accessing '{target_dir}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    target_folder = input("Enter the full path of the folder you want to organize: ")
    organize_directory(target_folder)