
import os
from PIL import Image

def add_logo_to_image(image_path, logo_path, output_path, position=(0, 0)):
    base_image = Image.open(image_path).convert("RGB")    
    logo = Image.open(logo_path).convert("RGBA")    
    base_width, base_height = base_image.size    
    # 计算logo高度为图片高度的1/6    
    logo_height = int(base_height / 6 )   
    # 保持logo比例缩放    
    logo_width = int(logo_height * (logo.width / logo.height))    
    logo = logo.resize((logo_width, logo_height), Image.LANCZOS )    
    # 动态计算logo位置    
    if position == "bottom_right":        
        position = (base_width - logo_width, base_height - logo_height)    
    elif position == "center":        
        position = ((base_width - logo_width) // 2, (base_height - logo_height) // 2)    
    elif position == "top_left":        
        position = (0, 0)    
    base_image.paste(logo, position, logo)    
    base_image.save(output_path)

def batch_add_logo(input_dir, logo_path, output_dir, position):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    for filename in os.listdir(input_dir):
        print(f"Processing: {filename}")
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            input_path = os.path.join(input_dir, filename)
            output_path = os.path.join(output_dir, filename)
            add_logo_to_image(input_path, logo_path, output_path, position)

if __name__ == "__main__":
    input_directory = "D:\\GitHub\\t002"
    #input_directory = "D:\\GitHub\\t001_border"
    logo_image = "D:\\GitHub\\logo128.png"
    logo_image = "D:\\GitHub\\logotext2.png"
    output_directory = input_directory+"_logo"
    #batch_add_logo(input_directory, logo_image, output_directory,"top_left")
    batch_add_logo(input_directory, logo_image, output_directory,position = (35, 25))
    logo_image = "D:\\GitHub\\logotext2.png"
    logo_image = "D:\\GitHub\\logo128.png"
    input_directory=output_directory
    batch_add_logo(input_directory, logo_image, output_directory,"bottom_right")
