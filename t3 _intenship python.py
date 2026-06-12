import os
import shutil

source_folder = "source_images"
destination_folder = "destination_images"

os.makedirs(source_folder, exist_ok=True)
os.makedirs(destination_folder, exist_ok=True)

for file in os.listdir(source_folder):
    if file.lower().endswith(".jpg"):
        shutil.move(
            os.path.join(source_folder, file),
            os.path.join(destination_folder, file)
        )
        print("Moved:", file)

print("Done!")