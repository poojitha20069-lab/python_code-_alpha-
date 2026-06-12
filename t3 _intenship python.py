import os
import shutil

source_folder = r"C:\Users\pooji\OneDrive\Pictures\Camera Roll"
destination_folder = r"C:\Users\pooji\OneDrive\Pictures\destination"

os.makedirs(destination_folder, exist_ok=True)

for file in os.listdir(source_folder):
    if file.lower().endswith(".jpg"):
        shutil.move(
            os.path.join(source_folder, file),
            os.path.join(destination_folder, file)
        )
        print("Moved:", file)
        
print("All JPG files moved successfully!")