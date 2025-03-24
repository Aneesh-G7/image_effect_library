import os
from image_effects import apply_blur, apply_grayscale

input_folder = "input/"
output_folder = "output/"
os.makedirs(input_folder, exist_ok=True)
os.makedirs(output_folder, exist_ok=True)

for file in os.listdir(input_folder):
    if file.endswith((".jpg", ".jpeg", ".png")):
        input_path = os.path.join(input_folder, file)
        output_path_blur = os.path.join(output_folder, f"{file.split('.')[0]}_blur.png")
        output_path_gray = os.path.join(output_folder, f"{file.split('.')[0]}_gray.png")

        apply_blur(input_path, output_path_blur)
        apply_grayscale(input_path, output_path_gray)
        print(f"Processed {file}")
