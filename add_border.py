
import os
from PIL import Image

def add_border(image_path, output_path, border_width_ratio=0.1):
    base_image = Image.open(image_path).convert("RGB")
    base_width, base_height = base_image.size
    border_width = int(min(base_width, base_height) * border_width_ratio)
    new_width = base_width + 2 * border_width
    new_height = base_height + 2 * border_width
    border_color = (197, 197, 197, 255)  # 白色透明度100%
    new_image = Image.new("RGB", (new_width, new_height), border_color)
    new_image.paste(base_image, (border_width, border_width))
    new_image.save(output_path)

def batch_add_border(input_dir, output_dir, border_width_ratio=0.1):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    for filename in os.listdir(input_dir):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            input_path = os.path.join(input_dir, filename)
            output_path = os.path.join(output_dir, filename)
            add_border(input_path, output_path, border_width_ratio)

if __name__ == "__main__":
    input_directory = "D:\\GitHub\\t001"
    output_directory = "D:\\GitHub\\t001_border"
    batch_add_border(input_directory, output_directory, border_width_ratio=0.1)
