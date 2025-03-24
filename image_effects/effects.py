from PIL import Image, ImageFilter, ImageOps
import os

def apply_blur(image_path, output_path):
    img = Image.open(image_path)
    blurred = img.filter(ImageFilter.GaussianBlur(5))
    blurred.save(output_path)

def apply_grayscale(image_path, output_path):
    img = Image.open(image_path)
    gray = ImageOps.grayscale(img)
    gray.save(output_path)
