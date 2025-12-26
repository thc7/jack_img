
import os
from PIL import Image
import json

def add_multiple_logos_to_image(image_path, logo_configs, output_path):
    """
    给单张图片添加多个logo
    logo_configs: 包含多个logo配置的列表，每个配置包含logo路径、位置、偏移量等信息
    """
    base_image = Image.open(image_path).convert("RGB")
    base_width, base_height = base_image.size
    
    for logo_config in logo_configs:
        logo_path = logo_config.get("path")
        position = logo_config.get("position", "bottom_right")
        offset_x = logo_config.get("offset_x", 0)
        offset_y = logo_config.get("offset_y", 0)
        scale = logo_config.get("scale", 1.0)  # logo缩放比例
        
        if not os.path.exists(logo_path):
            print(f"Logo文件不存在: {logo_path}")
            continue
            
        logo = Image.open(logo_path).convert("RGBA")
        
        # 按比例缩放logo
        if scale != 1.0:
            new_width = int(logo.width * scale)
            new_height = int(logo.height * scale)
            logo = logo.resize((new_width, new_height), Image.LANCZOS)
        
        logo_width, logo_height = logo.size

        print(f"Logo size: {logo_width}x{logo_height}, Scale: {scale}", logo_path)
        
        # 计算logo位置
        if position == "top_left":
            x = offset_x
            y = offset_y
        elif position == "top_right":
            x = base_width - logo_width - offset_x
            y = offset_y
        elif position == "bottom_left":
            x = offset_x
            y = base_height - logo_height - offset_y
        elif position == "bottom_right":
            x = base_width - logo_width - offset_x
            y = base_height - logo_height - offset_y
        elif position == "center":
            x = (base_width - logo_width) // 2 + offset_x
            y = (base_height - logo_height) // 2 + offset_y
        else:
            # 自定义坐标
            x = offset_x
            y = offset_y
        
        # 确保logo不会越界
        x = max(0, min(x, base_width - logo_width))
        y = max(0, min(y, base_height - logo_height))
        
        base_image.paste(logo, (int(x), int(y)), logo)
    
    base_image.save(output_path)

def batch_add_multiple_logos(input_dir, logo_configs, output_dir):
    """
    批量给目录下的图片添加多个logo
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    image_extensions = ('.png', '.jpg', '.jpeg', '.bmp', '.tiff', '.webp')
    
    for filename in os.listdir(input_dir):
        if filename.lower().endswith(image_extensions):
            input_path = os.path.join(input_dir, filename)
            output_path = os.path.join(output_dir, filename)
            try:
                add_multiple_logos_to_image(input_path, logo_configs, output_path)
                print(f"已处理: {filename}")
            except Exception as e:
                print(f"处理 {filename} 时出错: {e}")

def load_logo_configs_from_json(config_path):
    """
    从JSON文件加载logo配置
    """
    with open(config_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def create_sample_config():
    """
    创建示例配置文件
    """
    sample_config = [
        {
            "path": "logo1.png",
            "position": "bottom_right",
            "offset_x": 10,
            "offset_y": 10,
            "scale": 0.5
        },
        {
            "path": "logo2.png",
            "position": "top_left",
            "offset_x": 20,
            "offset_y": 20,
            "scale": 0.3
        },
        {
            "path": "watermark.png",
            "position": "center",
            "offset_x": 0,
            "offset_y": 0,
            "scale": 0.8
        }
    ]
    
    with open("logo_config.json", "w", encoding="utf-8") as f:
        json.dump(sample_config, f, indent=4, ensure_ascii=False)
    print("示例配置文件 'logo_config.json' 已创建")

if __name__ == "__main__":
    # 创建示例配置文件
    #create_sample_config()
    
    # 配置参数
    #input_directory = "input_images"
    #output_directory = "output_images"
    input_directory = "D:\\GitHub\\t001"
    input_directory = "D:\\GitHub\\t002"
    input_directory = "D:\\GitHub\\t003"
    output_directory = input_directory+"_logo"
    config_file = "D:\\GitHub\\logo_config.json"
    
    # 检查输入目录是否存在
    if not os.path.exists(input_directory):
        print(f"输入目录 '{input_directory}' 不存在，请创建该目录并放入图片文件")
        exit(1)
    
    # 检查配置文件是否存在
    if not os.path.exists(config_file):
        print(f"配置文件 '{config_file}' 不存在，已创建示例文件，请修改后重新运行")
        exit(1)
    
    # 加载logo配置
    try:
        logo_configs = load_logo_configs_from_json(config_file)
    except Exception as e:
        print(f"加载配置文件时出错: {e}")
        exit(1)
    
    # 执行批量处理
    batch_add_multiple_logos(input_directory, logo_configs, output_directory)
    print("批量添加logo完成！")
